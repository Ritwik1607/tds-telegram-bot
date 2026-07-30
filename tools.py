import os
import requests

DOWNLOAD_DIR = "datasets"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def download_file(url: str):

    filename = url.split("/")[-1]

    filepath = os.path.join(
        DOWNLOAD_DIR,
        filename
    )

    response = requests.get(url, timeout=60)

    response.raise_for_status()

    with open(filepath, "wb") as f:
        f.write(response.content)

    return filepath