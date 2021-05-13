from apps.common.text import FIELDS

MODELS = {"contest": {"singular": "Конкурсный проект", "plural": "Конкурсные проекты",}}

FIELDS = {
    "fond": "Название фонда/организации",
    "program": "Название программы",
    "contest": "Название конкурса",
    "project": "Название проекта",
    "manager": "Руководитель проекта",
    "date_added": FIELDS.get("date_added"),
}

TABLES = {"empty_text": "Проекты еще не добавлены."}

VIEWS = {
    "created": f"{MODELS.get('contest').get('singular')} создан.",
    "updated": f"{MODELS.get('contest').get('singular')} обновлен.",
    "deleted": f"{MODELS.get('contest').get('singular')} удален.",
}

TEMPLATES = {
    "table": MODELS.get("contest").get("plural"),
    "create": "Создание конкурсного проекта",
    "read": "Просмотр конкурсного проекта",
    "update": "Обновление конкурсного проекта",
    "delete": "Удаление конкурсного проекта",
}

ERROR_MESSAGES = {
    "project": {
        "unique": f"""
        {MODELS.get('contest').get('singular')} с таким названием уже существует.
        """
    },
}

HELP_TEXTS = {
    "manager": "ФИО полностью, должность, степень, звание.",
}

FORMS = {"error_messages": ERROR_MESSAGES, "help_texts": HELP_TEXTS}
