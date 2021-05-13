from apps.common.text import FIELDS

MODELS = {
    "grant": {
        "singular": "Грант зарубежного фонда",
        "plural": "Гранты зарубежных фондов",
    }
}

POSTGRADUATES = "Количество аспирантов и докторантов в научной коллективе"
STUDENTS = "Количество студентов в научном коллективе"

FIELDS = {
    "fond": "Название фонда/организации",
    "contest": "Название конкурса",
    "project": "Название проекта",
    "time_period": "Сроки выполнения",
    "financing": "Объем финансирования",
    "manager": "Руководитель гранта",
    "participants": "Участники гранта",
    "postgraduates_number_payed": f"{POSTGRADUATES} на возмездной основе",
    "postgraduates_number": f"{POSTGRADUATES} на безвозмездной основе",
    "students_number_payed": f"{STUDENTS} на безвозмездной основе",
    "students_number": f"{STUDENTS} на безвозмездной основе",
    "date_added": FIELDS.get("date_added"),
}

TABLES = {"empty_text": "Гранты еще не добавлены."}

VIEWS = {
    "created": f"{MODELS.get('grant').get('singular')} создан.",
    "updated": f"{MODELS.get('grant').get('singular')} обновлен.",
    "deleted": f"{MODELS.get('grant').get('singular')} удален.",
}

TEMPLATES = {
    "table": MODELS.get("grant").get("plural"),
    "create": "Создание гранта",
    "read": "Просмотр гранта",
    "update": "Обновление гранта",
    "delete": "Удаление гранта",
}

HELP_TEXTS = {
    "manager": "ФИО полностью, должность, степень, звание.",
}

ERRORS = {
    "invalid_author_format": "Автор %(nth)s не соответсвует формату.",
    "incompatible_participants_values": """
        Количество участников не согласуется со списком участников.
        """,
}

AUTHOR_FORMAT_MESSAGE = (
    'Перечислите авторов в соответствии с форматом "Фамилия И.[О.]" через запятую.'
)

ERROR_MESSAGES = {
    "participants": {"item_invalid": ERRORS.get("invalid_author_format")},
    "project": {
        "unique": f"""
        {MODELS.get('grant').get('singular')} с таким названием уже существует.
        """
    },
}

HELP_TEXTS = {
    "manager": "ФИО полностью, должность, степень, звание.",
}

FORMS = {"error_messages": ERROR_MESSAGES, "help_texts": HELP_TEXTS}
