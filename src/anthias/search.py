from anthias.util import get_root_url


import requests


def search_by_prefix(search_string):
    root_url = get_root_url()
    url = f"{root_url}/assets"
    r = requests.get(url)
    r.raise_for_status()
    assets = r.json()

    return [asset['asset_id'] for asset in assets if asset["name"].startswith(search_string)]


def search_by_name(search_string):
    root_url = get_root_url()
    url = f"{root_url}/assets"
    r = requests.get(url)
    r.raise_for_status()
    assets = r.json()

    return [asset['asset_id'] for asset in assets if search_string in asset["name"]]


def find_id_by_name(name, root_url):
    url = f"{root_url}/assets"
    r = requests.get(url)
    r.raise_for_status()
    assets = r.json()

    for asset in assets:
        if asset["name"] == name:
            return asset["asset_id"]

    raise ValueError(f"Could not find an asset with name '{name}'")