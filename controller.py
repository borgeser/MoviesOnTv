def get_non_empty_matches(movies_to_search, programs):
    response = dict()
    for movie in movies_to_search:
        results = find_movie(movie, programs)
        if len(results) > 0:
            response[movie] = results
    return response


def find_movie(title, programmes):
    return [prog for prog in programmes if is_title_equal(title, prog.title)]


def is_title_equal(search, title):
    return search.lower() in title.lower()
