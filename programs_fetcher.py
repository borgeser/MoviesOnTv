import urllib.request
from xml.etree import ElementTree

from mapper import map_programme


def fetch_programs():
    xml_root = get_xml()
    return get_programs(xml_root)


def get_programs(root: ElementTree):
    channels_xml = root.findall("channel")
    channels_dict = {c.get("id"): c.find("display-name").text for c in channels_xml}
    programmes_xml = root.findall("programme")
    programmes = [map_programme(el, channels_dict) for el in programmes_xml]
    return programmes


def get_xml(url="https://xmltv.ch/xmltv/xmltv-tnt.xml"):
    contents = urllib.request.urlopen(url).read()
    return ElementTree.fromstring(contents)
