from dotenv import load_dotenv

from controller import get_xml, get_programmes, find_movie
from model import Programme

movies_to_search = [
    "Bridget Jones : l'âge de raison",
    "H2G2",
]


def execute():
    load_dotenv()
    get_matches()


def get_matches():
    xml = get_xml()
    programmes = get_programmes(xml)
    response = dict()
    for movie in movies_to_search:
        results = find_movie(movie, programmes)
        dict[movie] = results
    return response


execute()
