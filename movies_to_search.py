import json
import os
import urllib.request


def get_movies_to_search():
    api_key = os.getenv("TRELLO_API_KEY")
    api_token = os.getenv("TRELLO_API_TOKEN")
    list_id = os.getenv("TRELLO_API_LIST_ID")
    url = f"https://api.trello.com/1/lists/{list_id}/cards?fields=name&key={api_key}&token={api_token}"
    body = urllib.request.urlopen(url).read()
    json_body = json.loads(body)
    movies = [obj["name"] for obj in json_body]
    return movies
