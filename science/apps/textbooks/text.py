__all__ = ["MODELS", "FIELDS", "TABLES", "VIEWS", "TEMPLATES", "FORMS", "ERRORS"]

from apps.common.text import FIELDS as COMMON_FIELDS

MODELS = {
    "field_of_study": {
        "singular": "Область исследования",
        "plural": "Области исследования",
    },
    "textbook": {"singular": "Учебник", "plural": "Учебники"},
    "textbook_category": {
        "singular": "Категория учебника",
        "plural": "Категории учебников",
    },
    "manual": {"singular": "Учебное пособие", "plural": "Учебные пособия"},
    "manual_category": {
        "singular": "Категория учебного пособия",
        "plural": "Категории учебных пособий",
    },
    "guide": {
        "singular": "Учебно-методическое пособие",
        "plural": "Учебно-методические пособия",
    },
    "guide_category": {
        "singular": "Категория учебно-методического пособия",
        "plural": "Категории учебно-методических пособий",
    },
}

FIELDS = {
    "name": "Название",
    "description": "Библиографическое описание",
    "publisher": "Издатель",
    "circulation": "Тираж",
    "isbn": "ISBN",
    "field_of_study": MODELS.get("field_of_study").get("singular"),
    "volume": "Объем",
    "volume_employees": "Объем, выполненный штантыми преподавателями",
    "employee_authors": "Авторы (сотрудники)",
    "foreign_authors": "Авторы (иностранцы)",
    "postgraduate_authors": "Авторы (аспиранты, докторанты)",
    "student_authors": "Авторы (студенты)",
    "category": "Категория",
    "date_added": COMMON_FIELDS.get("date_added"),
}

TABLES = {
    "empty_text": {
        "textbook": "Учебники еще не добавлены.",
        "manual": "Учебные пособия еще не добавлены.",
        "guide": "Учебно-методические пособия еще не добавлены.",
    }
}

VIEWS = {
    "created": {
        "textbook": f'{MODELS.get("textbook").get("singular")} создан.',
        "manual": f'{MODELS.get("manual").get("singular")} создано.',
        "guide": f'{MODELS.get("guide").get("singular")} создано',
    },
    "updated": {
        "textbook": f'{MODELS.get("textbook").get("singular")} обновлен.',
        "manual": f'{MODELS.get("manual").get("singular")} обновлено.',
        "guide": f'{MODELS.get("guide").get("singular")} обновлено.',
    },
    "deleted": {
        "textbook": f'{MODELS.get("textbook").get("singular")} удален.',
        "manual": f'{MODELS.get("manual").get("singular")} удалено.',
        "guide": f'{MODELS.get("guide").get("singular")} удалено.',
    },
}

TEMPLATES = {
    "table": {
        "textbook": MODELS.get("textbook").get("plural"),
        "manual": MODELS.get("manual").get("plural"),
        "guide": MODELS.get("guide").get("plural"),
    },
    "create": {
        "textbook": "Создание учебника.",
        "manual": "Создание учебного пособия.",
        "guide": "Создание учебно-методического пособия.",
    },
    "read": {
        "textbook": "Просмотр учебника.",
        "manual": "Просмотр учебного пособия.",
        "guide": "Просмотр учебно-методического пособия.",
    },
    "update": {
        "textbook": "Обновление учебника.",
        "manual": "Обновление учебного пособия.",
        "guide": "Обновление учебно-методического пособия.",
    },
    "delete": {
        "textbook": "Удаление учебника.",
        "manual": "Удаление учебного пособия.",
        "guide": "Удаление учебно-методического пособия.",
    },
}


ERRORS = {
    "invalid_author_format": "Автор %(nth)s не соответсвует формату.",
}

AUTHOR_FORMAT_MESSAGE = (
    'Перечислите авторов в соответствии с форматом "Фамилия И.[О.]" через запятую.'
)

ERROR_MESSAGES = {
    "description": {"unique": "Описание должно быть уникальным."},
    "participants": {"item_invalid": ERRORS.get("invalid_author_format")},
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
    "isbn": 'Введите ISBN-10 или ISBN-13. Например: "ISBN 0-0000-0000-0"',
    "circulation": "Оставьте поле пустым, если издание электронное.",
}

FORMS = {"error_messages": ERROR_MESSAGES, "help_texts": HELP_TEXTS}
