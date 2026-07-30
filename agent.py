import json
import numpy as np

from conversation import conversation
from llm import ask_llm
from logger import logger
from parser import has_url, extract_urls
from dataset_manager import dataset_manager
from dataframe_engine import engine
from planner import create_plan
from dataset_memory import dataset_memory
from config import LOG_PUBLIC_URL


def make_json_safe(obj):
    """
    Convert numpy/pandas objects into native Python types
    so json.dumps() works.
    """

    if isinstance(obj, dict):
        return {k: make_json_safe(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return [make_json_safe(v) for v in obj]

    if isinstance(obj, tuple):
        return [make_json_safe(v) for v in obj]

    if isinstance(obj, np.integer):
        return int(obj)

    if isinstance(obj, np.floating):
        return float(obj)

    if isinstance(obj, np.bool_):
        return bool(obj)

    if isinstance(obj, np.ndarray):
        return obj.tolist()

    return obj


class DataAnalystAgent:

    def process_message(self, chat_id: int, user_message: str) -> str:
        """
        Main entry point for every Telegram message.
        """

        logger.log(
            "user_message",
            {
                "chat_id": chat_id,
                "message": user_message
            }
        )

        conversation.add_user_message(chat_id, user_message)

        df = None

        # =====================================================
        # Download dataset if URL is present
        # =====================================================

        if has_url(user_message):

            try:

                urls = extract_urls(user_message)

                dataset_path = dataset_manager.download(urls[0])

                df = dataset_manager.load(dataset_path)

                dataset_memory.save(chat_id, df)

                logger.log(
                    "dataset_loaded",
                    {
                        "path": dataset_path,
                        "rows": len(df),
                        "columns": list(df.columns)
                    }
                )

            except Exception as e:

                logger.log(
                    "dataset_error",
                    {
                        "error": str(e)
                    }
                )

                return json.dumps(
                    {
                        "answer": f"Dataset Error: {str(e)}",
                        "log_url": LOG_PUBLIC_URL
                    }
                )

        # =====================================================
        # Reuse dataset from previous messages
        # =====================================================

        elif dataset_memory.has_dataset(chat_id):

            df = dataset_memory.get(chat_id)

            logger.log(
                "dataset_reused",
                {
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        # =====================================================
        # Dataset Analysis
        # =====================================================

        if df is not None:

            try:

                plan = create_plan(
                    history=conversation.get_history(chat_id),
                    columns=list(df.columns)
                )

                logger.log(
                    "execution_plan",
                    plan
                )

                result = engine.execute(df, plan)

                result = make_json_safe(result)

                logger.log(
                    "execution_result",
                    {
                        "result": str(result)
                    }
                )

                answer = result

            except Exception as e:

                logger.log(
                    "execution_error",
                    {
                        "error": str(e)
                    }
                )

                answer = f"Analysis Error: {str(e)}"

        # =====================================================
        # Normal Conversation
        # =====================================================

        else:

            history = conversation.get_history(chat_id)

            answer = ask_llm(history)

        conversation.add_assistant_message(
            chat_id,
            str(answer)
        )

        logger.log(
            "assistant_response",
            {
                "chat_id": chat_id,
                "message": str(answer)
            }
        )

        answer = make_json_safe(answer)

        return json.dumps(
            {
                "answer": answer,
                "log_url": LOG_PUBLIC_URL
            },
            ensure_ascii=False
        )


agent = DataAnalystAgent()