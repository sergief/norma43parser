from datetime import datetime
from decimal import Decimal


class Header:
    def __init__(
        self,
        bank_identifier: str,
        branch_key: str,
        account_number: str,
        start_date: datetime,
        initial_balance: Decimal,
        currency: str,
        type_of_information_service: int,
        account_name: str,
    ) -> None:
        self.bank_identifier = bank_identifier
        self.branch_key = branch_key
        self.account_number = account_number
        self.start_date = start_date
        self.initial_balance = initial_balance
        self.currency = currency
        self.type_of_information_service = type_of_information_service
        self.account_name = account_name
