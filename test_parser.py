from parser import extract_urls
from parser import detect_file_type

text = """
Download

https://example.com/data.csv

Find the average.
"""

urls = extract_urls(text)

print(urls)

print(detect_file_type(urls[0]))