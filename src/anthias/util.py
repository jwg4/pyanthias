import os


def get_root_url():
    url_from_env = os.environ["ANTHIAS_ROOT_URL"]
    if url_from_env.endswith("/"):
        url_from_env = url_from_env[:-1]
    return url_from_env