import os

from dotenv import load_dotenv

from controller import get_xml, get_programmes, find_movie
from mailer import send_mail
from movies_to_search import get_movies_to_search


def execute():
    load_dotenv()
    movies_to_search = get_movies_to_search()
    print(f"Trying to search movies: {movies_to_search}")
    matches_dict = get_non_empty_matches(movies_to_search)
    if len(matches_dict) > 0:
        print(f"New movies found! Sending them by email. Detail: {matches_dict}")
        send_email_for_movies(matches_dict)
    else:
        print("No movie found on TV.")


def get_non_empty_matches(movies_to_search):
    xml = get_xml()
    programmes = get_programmes(xml)
    response = dict()
    for movie in movies_to_search:
        results = find_movie(movie, programmes)
        if len(results) > 0:
            response[movie] = results
    return response


def send_email_for_movies(matches):
    text = get_email_body(matches)
    send_mail(text, "[MoviesOnTvBot] New movies found on TV!", os.getenv("EMAIL_RECIPIENT"))


def get_email_body(matches):
    text = "Here is the list of movies found:"
    for movie, programmes in matches.items():
        text += f"\nMovie '{movie}':\n"
        for prog in programmes:
            text += f"{prog}\n"
    text += "\n Don't forget to update your movie list. Bye bye :)"
    return text


if __name__ == "__main__":
    execute()
