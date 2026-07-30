import os
import requests
import pandas as pd

DATASET_DIR = "datasets"
os.makedirs(DATASET_DIR, exist_ok=True)


class DatasetManager:

    def download(self, url: str) -> str:
        filename = url.split("/")[-1].split("?")[0]
        if not filename:
            filename = "dataset"

        filepath = os.path.join(DATASET_DIR, filename)

        response = requests.get(url, timeout=60)
        response.raise_for_status()

        with open(filepath, "wb") as f:
            f.write(response.content)

        return filepath

    def load(self, filepath: str):

        path = filepath.lower()

        if path.endswith(".csv"):
            df = pd.read_csv(filepath)

        elif path.endswith((".xlsx", ".xls")):
            df = pd.read_excel(filepath)

        elif path.endswith(".json"):
            df = pd.read_json(filepath)

        elif path.endswith((".html", ".htm")):
            tables = pd.read_html(filepath)
            if not tables:
                raise ValueError("No HTML tables found.")
            df = tables[0]

        else:
            raise ValueError(f"Unsupported file type: {filepath}")

        df.columns = (
            df.columns.astype(str)
            .str.strip()
            .str.replace('"', "", regex=False)
            .str.replace("'", "", regex=False)
        )

        return df


dataset_manager = DatasetManager()