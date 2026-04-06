import os

import requests


def get_root_url():
    url_from_env = os.environ["ANTHIAS_ROOT_URL"]
    if url_from_env.endswith("/"):
        url_from_env = url_from_env[:-1]
    return url_from_env


def find_id_by_name(name, root_url):
    url = f"{root_url}/assets"
    r = requests.get(url)
    r.raise_for_status()
    assets = r.json()

    for asset in assets:
        if asset["name"] == name:
            return asset["asset_id"]
    
    raise ValueError(f"Could not find an asset with name '{name}'")


def write_enabled(name, enabled):
    root_url = get_root_url()
    id_ = find_id_by_name(name, root_url)
    
    url = f"{root_url}/assets/{id_}"
    r = requests.patch(url, json={"is_enabled": 1 if enabled else 0})
    r.raise_for_status()


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
