from collections import defaultdict


class DatasetMemory:

    def __init__(self):
        self.datasets = defaultdict(lambda: None)

    def save(self, chat_id, df):
        self.datasets[chat_id] = df

    def get(self, chat_id):
        return self.datasets.get(chat_id)

    def has_dataset(self, chat_id):
        return self.datasets.get(chat_id) is not None

    def clear(self, chat_id):
        if chat_id in self.datasets:
            del self.datasets[chat_id]


dataset_memory = DatasetMemory()