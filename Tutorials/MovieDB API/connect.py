import requests
import pprint
import pandas as pd
import os

api_key = "d3e419ba144071197eec1afad72bb303"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkM2U0MTliYTE0NDA3MTE5N2VlYzFhZmFkNzJiYjMwMyIsInN1YiI6IjYwMzUxZGU3NmNmM2Q1MDA0MGZjNzdkOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.l_oAREKB1Y4PZymxWc9RXHAnUqQwC76lWFqyPaUW1HQ"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# HTTP Requests METHODS
"""
GET --> Grab Data
POST --> add/update data

PATCH
PUT
DELETE
"""

# What's our endpoint (or a url)

# what is the HTTP method that we need?

"""
Endpoint
/movie/{movie_id}
f"https://api.themoviedb.org/3/movie/550?api_key{api_key}}"
"""
movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"

endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
# print(endpoint)
# r = requests.get(endpoint)

# print(r.status_code)
# print(r.text)

# using v4
movie_id = 501
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"

endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
headers = {
      'Authorization': f"Bearer {api_key_v4}",
      'Content-Type': "application/json;charset=utf-8"
}
# print(endpoint)
# print(headers)

# r = requests.get(endpoint, headers=headers)

# print(r.status_code)
# print(r.text)


# Search movies
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
query = "query=The Matrix"

endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&{query}"
#print(endpoint)
r = requests.get(endpoint)

#print(r.status_code)
#pprint.pprint(r.json())

if r.status_code in range(200, 300):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        print("Found results")
        #print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result['id']
            #print(result['title'], _id)
            movie_ids.add(_id)
        #print(list(movie_ids))

output = os.path.join(BASE_DIR, "movie.csv")
movie_data = []

for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"

    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    # print(endpoint)
    r = requests.get(endpoint)

    # print(r.status_code)
    # print(r.text)
    if r.status_code in range(200, 300):
        data = r.json()
        movie_data.append(data) 
    
df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index=False)