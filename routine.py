import os

from dotenv import load_dotenv

from controller import get_non_empty_matches
from mailer import send_mail
from movies_to_search import get_movies_to_search
from programs_fetcher import fetch_programs


def execute():
    load_dotenv()
    movies_to_search = get_movies_to_search()
    print(f"Trying to search movies: {movies_to_search}")
    programs = fetch_programs()
    matches_dict = get_non_empty_matches(movies_to_search, programs)
    if len(matches_dict) > 0:
        print(f"New movies found! Sending them by email. Detail: {matches_dict}")
        send_email_for_movies(matches_dict)
    else:
        print("No movie found on TV.")


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
