
import requests

from anthias.util import get_root_url
from anthias.search import find_id_by_name


def write_enabled_by_id(id_, enabled, root_url):
    url = f"{root_url}/assets/{id_}"
    r = requests.patch(url, json={"is_enabled": 1 if enabled else 0})
    r.raise_for_status()


def enable_asset(id_):
    root_url = get_root_url()
    write_enabled_by_id(id_, True, root_url)


def disable_asset(id_):
    root_url = get_root_url()
    write_enabled_by_id(id_, False, root_url)


def write_enabled(name, enabled):
    root_url = get_root_url()
    id_ = find_id_by_name(name, root_url)
    
    write_enabled_by_id(id_, enabled, root_url)
