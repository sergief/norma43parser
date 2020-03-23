from datetime import date
from decimal import Decimal


class Header:
    def __init__(
        self,
        bank_identifier: str = None,
        branch_key: str = None,
        account_number: str = None,
        start_date: date = None,
        end_date: date = None,
        initial_balance: Decimal = None,
        currency: str = None,
        type_of_information_service: str = None,
        account_name: str = None,
    ) -> None:
        self.bank_identifier = bank_identifier
        self.branch_key = branch_key
        self.account_number = account_number
        self.start_date = start_date
        self.end_date = end_date
        self.initial_balance = initial_balance
        self.currency = currency
        self.type_of_information_service = type_of_information_service
        self.account_name = account_name
