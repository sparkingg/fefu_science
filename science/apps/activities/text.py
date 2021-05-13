__all__ = ["MODELS", "FIELDS", "TABLES", "VIEWS", "TEMPLATES", "FORMS", "ERRORS"]


MODELS = {
    "activity_type": "Тип научного мероприятия",
    "activity_type_plural": "Типы научных мероприятий",
    "activity": "Научное мероприятие",
    "activity_plural": "Научные меропрития",
}

FIELDS = {
    "activity_type": {
        "name": "Название типа мероприятия",
        "date_added": "Дата добавления",
    },
    "activity": {
        "name": "Название мероприятия, дата проведения",
        "participants": "Число участников (всего)",
        "participants_university": "Число участников (сотрудники, учащиеся ДВФУ)",
        "participants_foreign": "Участие зарубежных специалистов (всего)",
        "participants_country": "Участие зарубежных специалистов (страна)",
        "financing_source": "Финансирование (фонд, организация)",
        "financing_amount": "Финансирование (руб.)",
        "bibliographic_description": "Материалы конференции (полное библиографическое описание)",
        "publications_url": "Ссылки на публикации о мероприятии",
        "journal_name": "Указать название журнала, сборника, если планируется индексация материалов в БД Scopus",
        "activity_type": MODELS.get("activity_type"),
        "date_added": "Дата добавления",
    },
}

TABLES = {
    "empty_text": "Мероприятия еще не добавлены.",
}

VIEWS = {
    "created": f"{MODELS.get('activity')} создано.",
    "updated": f"{MODELS.get('activity')} обновлено.",
    "deleted": f"{MODELS.get('activity')} удалено.",
}

TEMPLATES = {
    "table": MODELS.get("activity"),
    "create": "Создание мероприятия",
    "read": "Просмотр мероприятия",
    "update": "Обновление мероприятия",
    "delete": "Удаление мероприятия",
}
