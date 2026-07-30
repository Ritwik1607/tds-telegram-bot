from tools import download_file

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"

path = download_file(url)

print(path)