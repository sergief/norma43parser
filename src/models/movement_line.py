from datetime import datetime
from decimal import Decimal
from typing import List


class MovementLine:
    def __init__(
        self,
        branch_code: str,
        operation_date: datetime,
        value_date: datetime,
        initial_balance: Decimal,
        description: str,
        extra_information: List[str],
    ) -> None:
        self.branch_code = branch_code
        self.operation_date = operation_date
        self.value_date = value_date
        self.inital_balance = initial_balance
        self.description = description
        self.extra_information = extra_information
