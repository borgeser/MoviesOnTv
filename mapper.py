from datetime import datetime
from xml.etree import ElementTree

from model import Programme

time_format = "%Y%m%d%H%M%S %z"


def map_programme(el: ElementTree, channels_dict):
    category = el.find("category")
    return Programme(
        el.find("title").text,
        "" if category is None else category.text,
        channels_dict[el.get("channel")],
        datetime.strptime(el.get("start"), time_format),
        datetime.strptime(el.get("stop"), time_format)
    )
