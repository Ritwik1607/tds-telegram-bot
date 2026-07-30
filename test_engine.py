from dataset_manager import dataset_manager
from dataframe_engine import engine

path = dataset_manager.download(
    "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
)

df = dataset_manager.load(path)

print(engine.execute(df, {"operation": "columns"}))
print(engine.execute(df, {"operation": "shape"}))
print(engine.execute(df, {"operation": "max", "column": "1960"}))