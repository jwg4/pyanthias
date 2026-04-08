"""
    These functions are specifically chosen to be compatible with
    an old interface which talked to the Screenly SQLite database directly.
    
    Thus they have slightly odd functionality design and there should be
    new, more logical ways of doing the same thing in the future.
"""

import requests

from anthias.basic import write_enabled
from anthias.search import find_id_by_name, search_by_prefix
from anthias.util import get_root_url


def enable(name):
    write_enabled(name, True)


def disable(name):
    write_enabled(name, False)


def toggle(name):
    root_url = get_root_url()

    id_ = find_id_by_name(name, root_url)

    url = f"{root_url}/assets/{id_}"
    r = requests.get(url)
    r.raise_for_status()
    asset = r.json()

    enabled = asset["is_enabled"] == 1

    write_enabled(name, not enabled)


def schedule_image(prefix, start_time, end_time):
    root_url = get_root_url()

    for asset_id in search_by_prefix(prefix):
        url = f"{root_url}/assets/{asset_id}"
        r = requests.patch(url, json={"is_enabled": 1, "start_time": start_time, "end_time": end_time})
        r.raise_for_status()
