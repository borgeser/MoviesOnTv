from dotenv import load_dotenv

from routine import get_non_empty_matches


def main():
    load_dotenv()
    matches_dict = get_non_empty_matches()
    print(f"Results: {matches_dict}")


if __name__ == "__main__":
    main()
