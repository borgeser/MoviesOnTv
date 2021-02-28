from controller import get_xml, get_programmes


def main():
    xml = get_xml()
    programmes = get_programmes(xml)
    print(programmes[-1].start)


if __name__ == "__main__":
    main()
