from dotenv import load_dotenv

from movies_to_search import get_movies_to_search
from programs_fetcher import fetch_programs
from routine import get_non_empty_matches


def main():
    load_dotenv()
    movies = get_movies_to_search()
    print(f"Movies: {movies}")
    programs = fetch_programs()
    matches_dict = get_non_empty_matches(movies, programs)
    print(f"Results: {matches_dict}")


if __name__ == "__main__":
    main()
