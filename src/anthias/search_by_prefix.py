from anthias.basic import get_root_url


import requests


def search_by_prefix(search_string):
    root_url = get_root_url()
    url = f"{root_url}/assets"
    r = requests.get(url)
    r.raise_for_status()
    assets = r.json()

    return [asset['asset_id'] for asset in assets if asset["name"].startswith(search_string)]