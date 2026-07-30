from conversation import conversation
from llm import ask_llm


class DataAnalystAgent:

    def process_message(self, chat_id: int, user_message: str) -> str:
        """
        Main entry point for every Telegram message.
        """

        # Save user message
        conversation.add_user_message(chat_id, user_message)

        # Get conversation history
        history = conversation.get_history(chat_id)

        # Ask the LLM
        answer = ask_llm(history)

        # Save assistant response
        conversation.add_assistant_message(chat_id, answer)

        return answer


agent = DataAnalystAgent()