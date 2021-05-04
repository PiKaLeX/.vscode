
import grequests
import gevent.monkey
gevent.monkey.patch_all()
import os
import datetime
from requests_html import HTML
import pandas as pd
import sys
from pprint import pprint
import json
import re
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(BASE_DIR, "images")
BASE_URL = "https://www.mayrand.ca/fr/nos-produits"

def url_to_txt(url, filename="world", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(os.path.join(BASE_DIR, f"{filename}.html"), "w") as f:
                f.write(html_text)
        return html_text
    return None

def url_to_txt_async(urls=[]):
    results = grequests.map((grequests.get(u) for u in urls), size=20)
    print (results)
    return results

def exception(self, request, exception):
    print(f"Problem: {request.url}: {exception}")

def parse_and_extract(base_url, catégorie="epicerie"):

    # Data list
    product_scraped_list_header = ['Brand', 'Description', 'Catérogie', 'Format (petit)', 'Prix Total', 'Prix unitaire','Format (grand)', 'Prix Total', 'Prix unitaire', 'URL']
    product_scraped_list_data = []

    # First page to scrape
    url = f"{base_url}/?page=1"
    html_txt =  url_to_txt(url) # , catégorie, True)
    if html_txt == None:
        return False

    r_html = HTML(html=html_txt)

    # Get the page number for the current category
    number_of_pages = r_html.find('.search-result-controls', first=True)
    number_of_pages = number_of_pages.find('.pagination-link')  # Get the all the pages link
    number_of_pages = number_of_pages[len(number_of_pages) - 2]  # Keep the 2nd last one to get the highest page.
    number_of_pages = number_of_pages.text  # Keep the text, which shouold be an integer value
    number_of_pages = int(number_of_pages)
    print(number_of_pages)
    # number_of_pages = 1

    # Get the data for all pages (Async)
    urls = []
    for i in range(1, number_of_pages + 1):
        urls.append(f"{base_url}/?page={i}")

    html_responses = url_to_txt_async(urls)

    # Get the data for all pages
    for i in range(1, number_of_pages + 1):
        try:

            print(f"Page {i}")
            # # url = f"{base_url}/?page={i}"
            # html_txt =  url_to_txt(url) # , catégorie, True)
            # if html_txt == None:
            #     return False

            r_html = HTML(html=html_responses[i-1].text)

            # Get all the product of the current page
            products = r_html.find(".product-line-body")

            for product in products:
                try:
                    # get product JSON details
                    product_data = product.find(".product-line-add-to-cart", first=True).attrs['props-json'] # use props-json
                    product_data = json.loads(product_data)
                    product_data = product_data['product']

                    # Extract data
                    product_brand = product_data['brand'] if 'brand' in product_data else "Not available"
                    product_description = product_data['displayName'].replace('"','')
                    product_url = product_data['url']

                    product_data = product_data['variants']

                    # print(type(product_data))
                    # pprint(product_data)
                    if len(product_data) == 0:
                        raise Exception("No product prices found")
                    if len(product_data) > 2:
                        raise Exception("Found more than 2 formats")

                    unit_product_format = "N/A"
                    unit_product_price = "N/A"
                    unit_product_unit_price = "N/A"
                    lot_product_format = "N/A"
                    lot_product_price = "N/A"
                    lot_product_unit_price = "N/A"
                    for product_details in product_data:
                        try:
                            temp_format = product_details['sellFormat']
                            temp_product_price = product_details['listingPrice']['amount']
                            compute_unit_price = True

                            if re.match('unit', temp_format):  # Unit format
                                unit_product_format = temp_format
                                unit_product_price = temp_product_price

                                if unit_product_format == 'unité ':
                                    unit_product_unit_price = "N/A"
                                    compute_unit_price = False

                                if compute_unit_price:
                                    regex_result = re.search('[\d]+[.,]*[\d]*',unit_product_format)  # Keep the X.Y decimal part of the unit. example 2.3kg will keep 2.3
                                    if regex_result is None and re.match('(un)|(chop)|(chopine)', unit_product_format.lower()):
                                        temp_quantity_decimal = 1
                                    else:
                                        temp_quantity_decimal = regex_result.group().replace(',','.')

                                    regex_result = re.findall('[a-zA-Z]+',unit_product_format)  # Keep the X.Y decimal part of the unit. example 2.3kg will keep 2.3
                                    temp_quantity_unit = regex_result[-1]  # Keep the unit part. example 2.3kg will keep kg
                                    temp_quantity_unit = temp_quantity_unit.lower()

                                    unit_divider = unit_divider_parser(temp_quantity_unit)

                                    unit_product_unit_price = float(unit_product_price) / float(temp_quantity_decimal) * unit_divider * 100
                                    unit_product_unit_price = round(unit_product_unit_price, 3)

                            elif re.match('caisse', temp_format):  # Lot format
                                lot_product_format = temp_format
                                lot_product_price = temp_product_price

                                regex_result = re.findall('[\d]+[.,]*[\d]*',lot_product_format)  # Keep the X.Y decimal part of the unit. example 12X2.3kg will keep 12 and 2.3
                                if len(regex_result) == 2:  # Caisse (20x1kg) --> Multiple time the unit size
                                    temp_quantity_per_lot = regex_result[0].replace(',','.')
                                    temp_quantity_decimal = regex_result[1].replace(',','.')
                                elif len(regex_result) == 1:  # Caisse (20kg) --> Already the total size
                                    temp_quantity_per_lot = 1
                                    temp_quantity_decimal = regex_result[0].replace(',','.')
                                elif len(regex_result) == 3:  # Caisse (3x20x1kg) --> Multiple time the unit size
                                    temp_quantity_per_lot = float(regex_result[0].replace(',','.'))
                                    temp_quantity_per_lot *= float(regex_result[1].replace(',','.'))
                                    temp_quantity_decimal = regex_result[2]
                                else:
                                    lot_product_unit_price = "N/A"
                                    compute_unit_price = False
                                    if lot_product_format != 'caisse ':
                                        raise Exception(f"regex result length unknown : {regex_result}")

                                if compute_unit_price:
                                    regex_result = re.findall('[a-zA-Z]+',lot_product_format)  # Keep the X.Y decimal part of the unit. example 2.3kg will keep 2.3
                                    temp_quantity_unit = regex_result[-1]  # Keep the unit part. example 2.3kg will keep kg
                                    temp_quantity_unit = temp_quantity_unit.lower()

                                    unit_divider = unit_divider_parser(temp_quantity_unit)

                                    lot_product_unit_price = float(lot_product_price) / float(temp_quantity_per_lot) / float(temp_quantity_decimal) * unit_divider * 100
                                    lot_product_unit_price = round(lot_product_unit_price, 3)

                            else:
                                raise Exception("New unknown format found")

                        except Exception as e:
                            print(e)

                    product_scraped_list_data.append([product_brand, product_description, catégorie, unit_product_format, unit_product_price, unit_product_unit_price, lot_product_format, lot_product_price, lot_product_unit_price, product_url])

                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)

    # Store to CSV
    df = pd.DataFrame(product_scraped_list_data,columns=product_scraped_list_header)
    df = df.sort_values(by=['Description', 'Brand'])
    path = os.path.join(BASE_DIR,"Data")
    os.makedirs(path, exist_ok=True)
    df.to_csv(os.path.join(path, f'{catégorie}.csv'), index=False, encoding='utf-8')
    return True

def unit_divider_parser(unit):
    if re.match('ml', unit):  # Find if lb unit (1 mL --> 1mL)
        return 1
    elif re.match('kg', unit):  # Find if lb unit (1 kg --> 1000g)
        return 0.001
    elif re.match('lb', unit):  # Find if lb unit (1 lb --> 453.592g)
        return 1/453.592
    elif re.match('mg', unit):  # Find if lb unit (1 mg --> 0.001g)
        return 1000
    elif re.match('l', unit):  # Find if L unit (1 L --> 1000mL)
        return 0.001
    elif re.match('g', unit):  # Find if lb unit (1 g --> 1g)
        return 1
    elif re.match('un', unit):  # Find all the unitaire unit. This has to negate the * 100 in the next formula to get the unit price instead of 100g or 100ml
        return 0.01
    elif re.match('oz', unit):  # Find if lb unit (1 oz --> 28.3495g)
        return 1/28.3495
    elif re.match('dz', unit):  # Find if lb unit (1 dz --> 12)
        return 1/12
    elif re.match('[xchop|chop|cs|caisse]', unit):  # Find all the unitaire unit. This has to negate the * 100 in the next formula to get the unit price instead of 100g or 100ml
        return 0.01
    else:
        raise Exception("New unknown unit found")

def run(catégorie='epicerie', mot_clef=None):

    url = f"{BASE_URL}/{catégorie}"
    finished = parse_and_extract(url, catégorie)
    if finished:
        print(f"Finished {catégorie}")
    else:
        print(f"Error in year {catégorie}")

if __name__ == "__main__":
    try:
        catégorie = str(sys.argv[1])
    except:
        catégorie = 'epicerie'
    try:
        mot_clef = str(sys.argv[2])
    except:
        mot_clef = None

    run(catégorie=catégorie, mot_clef=mot_clef)

    # ToDo: essayer de loader les pages Async puisque cest long.

