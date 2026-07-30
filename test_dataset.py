from dataset_manager import dataset_manager

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"

path = dataset_manager.download(url)

print(path)

df = dataset_manager.load(path)

print(df.head())

print(df.columns)