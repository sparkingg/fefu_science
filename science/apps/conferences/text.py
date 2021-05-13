__all__ = ["MODELS", "FIELDS", "TABLES", "VIEWS", "TEMPLATES", "FORMS", "ERRORS"]


MODELS = {
    "conference_type": "Тип конференции",
    "conference_type_plural": "Типы конференций",
    "conference": "Конференция",
    "conference_plural": "Конференции",
}

FIELDS = {
    "description": "Описание",
    "employee_authors": "Авторы (сотрудники)",
    "foreign_authors": "Авторы (иностранцы)",
    "postgraduate_authors": "Авторы (аспиранты, докторанты)",
    "student_authors": "Авторы (студенты)",
    "conference_type": MODELS.get("conference_type"),
    "date_added": "Дата добавления",
}

TABLES = {
    "number_of_employee_authors": "Количество авторов (сотрудники)",
    "number_of_foreign_authors": "Количество авторов (иностранцы)",
    "number_of_postgraduate_authors": "Количество авторов (аспиранты, докторанты)",
    "number_of_student_authors": "Количество авторов (студенты)",
    "empty_text": "Конференции еще не добавлены.",
}

VIEWS = {
    "created": f"{MODELS.get('conference')} создана.",
    "updated": f"{MODELS.get('conference')} обновлена.",
    "deleted": f"{MODELS.get('conference')} удалена.",
}

TEMPLATES = {
    "table": MODELS.get("conference"),
    "create": "Создание конференции",
    "read": "Просмотр конференции",
    "update": "Обновление конференции",
    "delete": "Удаление конференции",
}


ERRORS = {
    "no_authors": "Авторы должны быть указаны.",
    "invalid_author_format": "Автор %(nth)s не соответсвует формату.",
}

AUTHOR_FORMAT_MESSAGE = (
    'Перечислите авторов в соответствии с форматом "Фамилия И.[О.]" через запятую.'
)

ERROR_MESSAGES = {
    "description": {
        "unique": f"{MODELS.get('conference')} с таким описанием уже существует."
    },
    "employee_authors": {"item_invalid": ERRORS.get("invalid_author_format")},
    "foreign_authors": {"item_invalid": ERRORS.get("invalid_author_format")},
    "postgraduate_authors": {"item_invalid": ERRORS.get("invalid_author_format")},
    "student_authors": {"item_invalid": ERRORS.get("invalid_author_format")},
}

HELP_TEXTS = {
    "description": """
        Введите описание без указанием авторов.
        При экспорте они будут добавлены автоматически.
        """,
    "employee_authors": AUTHOR_FORMAT_MESSAGE,
    "foreign_authors": AUTHOR_FORMAT_MESSAGE,
    "postgraduate_authors": AUTHOR_FORMAT_MESSAGE,
    "student_authors": AUTHOR_FORMAT_MESSAGE,
    "bibliographic_databases": """
        Выберите библиографическую базу данных, которая содержит ссылку на публикацию.
        Удерживайте CTRL (Windows) или CMD (Mac), чтобы выбрать несколько.
        """,
}

FORMS = {"error_messages": ERROR_MESSAGES, "help_texts": HELP_TEXTS}
