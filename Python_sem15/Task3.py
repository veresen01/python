# 3. Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.


from typing import Callable, Any

FORMAT = "{levelname:<8} - {asctime}. {msg}"

logging.basicConfig(filename="data.log", encoding="utf-8", level=logging.INFO, style="{", format=FORMAT,)
logger = logging.getLogger(__name__)


def log(func: Callable) -> Callable:
    def wrapper(*args) -> Any:
        result = func(*args)
        json_dict = {"args": args, "res": str(result)}
        msg = f"Функция: {func.__name__}, {json_dict} "
        logger.info(msg)
        return result

    return wrapper