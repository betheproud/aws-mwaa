from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class CustomOperator(BaseOperator):

    @apply_defaults
    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context):
        message = f"Hello {self.name}"
        print(message)
        return message
