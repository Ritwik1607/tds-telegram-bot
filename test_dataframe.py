from dataframe_engine import engine

df = engine.load_csv("datasets/airtravel.csv")

print(df.head())
print()
print(df.columns.tolist())