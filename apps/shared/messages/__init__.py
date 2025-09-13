from .common import COMMON_MESSAGES
from .blogs import BLOGS_MESSAGES

MESSAGES = {
    **COMMON_MESSAGES,
    **BLOGS_MESSAGES,
"UNKNOWN_ERROR": {
        "id": "unknown_error",
        "messages": {
            "ru": "Неизвестная ошибка",
            "en": "Unknown error",
        },
        "status_code": 500,
    },
}
