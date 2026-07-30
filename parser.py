import re

URL_PATTERN = re.compile(
    r"https?://[^\s]+",
    re.IGNORECASE
)


def extract_urls(text: str):
    """
    Extract all URLs from the user's message.
    """
    return URL_PATTERN.findall(text)


def has_url(text: str):
    return len(extract_urls(text)) > 0


def detect_file_type(url: str):
    """
    Guess the file type from the URL.
    """

    url = url.lower()

    if ".csv" in url:
        return "csv"

    if ".xlsx" in url or ".xls" in url:
        return "excel"

    if ".json" in url:
        return "json"

    if ".html" in url or ".htm" in url:
        return "html"

    return "unknown"