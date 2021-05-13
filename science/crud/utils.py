from collections import namedtuple

Actions = namedtuple("Actions", ["create", "read", "update", "delete"])


class PathBuilder:
    @staticmethod
    def _extract_app_name(model):
        return model._meta.app_label.lower().replace("_", "-")

    @staticmethod
    def _extract_model_name(model):
        return (model.__name__).lower()

    @staticmethod
    def _build_path(model, action):
        app_name = PathBuilder._extract_app_name(model)
        model_name = PathBuilder._extract_model_name(model)

        return f"{app_name}-{model_name}-{action}"

    @staticmethod
    def build_table_path(model):
        return PathBuilder._build_path(model, "table")

    @staticmethod
    def build_create_path(model):
        return PathBuilder._build_path(model, "create")

    @staticmethod
    def build_read_path(model):
        return PathBuilder._build_path(model, "read")

    @staticmethod
    def build_update_path(model):
        return PathBuilder._build_path(model, "update")

    @staticmethod
    def build_delete_path(model):
        return PathBuilder._build_path(model, "delete")
