from controller import get_xml, get_programmes, find_movie


def main():
    xml = get_xml()
    programmes = get_programmes(xml)
    candidates = find_movie("un coeur en hiver", programmes)
    print(candidates)


if __name__ == "__main__":
    main()
