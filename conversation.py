from collections import defaultdict

MAX_HISTORY = 10

class ConversationManager:
    def __init__(self):
        self.history = defaultdict(list)

    def add_user_message(self, chat_id, message):
        self.history[chat_id].append(
            {
                "role": "user",
                "content": message
            }
        )
        self.trim(chat_id)

    def add_assistant_message(self, chat_id, message):
        self.history[chat_id].append(
            {
                "role": "assistant",
                "content": message
            }
        )
        self.trim(chat_id)

    def get_history(self, chat_id):
        return self.history[chat_id]

    def trim(self, chat_id):
        if len(self.history[chat_id]) > MAX_HISTORY:
            self.history[chat_id] = self.history[chat_id][-MAX_HISTORY:]

conversation = ConversationManager()