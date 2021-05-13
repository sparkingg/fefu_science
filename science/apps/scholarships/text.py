__all__ = ["MODELS", "FIELDS", "TABLES", "VIEWS", "TEMPLATES", "FORMS", "ERRORS"]


MODELS = {
    "scholarship_category": {
        "singular": "Категория поддержки",
        "plural": "Категории поддержки",
    },
    "scholarship": {"singular": "Поддержка", "plural": "Поддержка"},
}

FIELDS = {
    "fond": "Название фонда",
    "activity": "Название программы",
    "project": "Название проекта",
    "time_period": "Сроки выполнения",
    "financing": "Объем финансирования",
    "participants": "Участники",
    "support_type": "Форма поддержки",
    "category": MODELS.get("scholarship_category").get("singular"),
    "date_added": "Дата добавления",
}

TABLES = {
    "empty_text": "Записи о поддержке еще не добавлены.",
}

VIEWS = {
    "created": "Запись о поддержке создана.",
    "updated": "Запись о поддержке обновлена.",
    "deleted": "Запись о поддержке удалена.",
}

TEMPLATES = {
    "table": MODELS.get("scholarship").get("plural"),
    "create": "Создание записи о поддержке",
    "read": "Просмотр записи о поддержке",
    "update": "Обновление записи о поддержке",
    "delete": "Удаление записи о поддержке",
}


ERRORS = {
    "invalid_author_format": "Автор %(nth)s не соответсвует формату.",
}

AUTHOR_FORMAT_MESSAGE = (
    'Перечислите авторов в соответствии с форматом "Фамилия И.[О.]" через запятую.'
)

ERROR_MESSAGES = {
    "participants": {"item_invalid": ERRORS.get("invalid_author_format")},
}

HELP_TEXTS = {
    "name": """
        Название фонда, организации или страна.
        """,
    "activity": "Название программы, конкурса или олимпиады.",
    "financing": "Данные за отчетный год.",
    "participants": AUTHOR_FORMAT_MESSAGE,
    "support_type": """
        Денежные премии, именные стипендии, дипломы различных организаций,
        участие в конференциях, предоставление стажировки,
        предоставление гранта, другое.
        """,
}

FORMS = {"error_messages": ERROR_MESSAGES, "help_texts": HELP_TEXTS}
