from logger import logger

logger.log(
    "test",
    {
        "message": "Logger working"
    }
)

print(logger.get_log_path())