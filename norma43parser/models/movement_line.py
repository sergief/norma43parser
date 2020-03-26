from datetime import date
from decimal import Decimal
from typing import List


class MovementLine:
    def __init__(
        self,
        branch_key: str = None,
        operation_date: date = None,
        value_date: date = None,
        initial_balance: Decimal = None,
        description: str = None,
        extra_information: List[str] = None,
    ) -> None:
        self.branch_key = branch_key
        self.operation_date = operation_date
        self.value_date = value_date
        self.initial_balance = initial_balance
        self.description = description
        self.extra_information = extra_information if extra_information is not None else []
