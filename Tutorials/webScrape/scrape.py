import requests
import os
import datetime
from requests_html import HTML
import pandas as pd
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(BASE_DIR, "images")

def url_to_txt(url, filename="world.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(os.path.join(BASE_DIR, f"world-{year}.html"), "w") as f:
                f.write(html_text)
        return html_text
    return None

def parse_and_extract(url, filename="2021"):
    html_txt =  url_to_txt(url)
    if html_txt == None:
        return False
    r_html = HTML(html=html_txt)
    table_class = ".imdb-scroll-table"
    r_table = r_html.find(table_class)

    table_data = []
    header_names = []
    if len(r_table) != 1:
        return False
        
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header_row = rows[0]    
    header_cols = header_row.find("th")
    header_names = [x.text for x in header_cols]

    table_data = []
    for row in rows[1:]:
        #print(row.text)
        cols = row.find("td")
        row_data = []
        for i, col in enumerate(cols):
            #print(i, col.text, "\n\n")
            row_data.append(col.text)
        table_data.append(row_data)
    
    df = pd.DataFrame(table_data,columns=header_names)
    path = os.path.join(BASE_DIR,"Data")
    os.makedirs(path, exist_ok=True)
    df.to_csv(os.path.join(path, f'movies-{filename}.csv'),index=False)
    return True


def run(start_year=None, years_ago=0):
    
    if start_year == None:
        start_year = datetime.datetime.now().year
    else:
        assert isinstance(start_year, int)
        assert len(f'{start_year}') == 4

    for year in range(start_year, start_year - years_ago - 1, -1):
        url = f"https://www.boxofficemojo.com/year/{year}"
        finished = parse_and_extract(url, f"{year}")
        if finished:
            print(f"Finished {year}")
        else:
            print(f"Error in year {year}")

if __name__ == "__main__":
    try:
        start = int(sys.argv[1])
    except:
        start = None
    try:
        count = int(sys.argv[2])
    except:
        count = 0

    run(start_year=start, years_ago=count)

