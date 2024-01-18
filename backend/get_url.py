import datetime

from backend.tree_ids import TREE_IDS

BASE_URL = "https://www.wildflowers.co.il/kkl/plant.asp?ID="


def get_todays_url() -> str:
    return BASE_URL + str(TREE_IDS[map_date_to_index(get_today_str())])


def map_date_to_index(date: str):
    hashed = hash(date)
    index = hashed % len(TREE_IDS)
    return index


def get_today_str():
    return datetime.date.today().strftime('%D')
