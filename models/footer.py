from decimal import Decimal


class Footer:
    def __init__(
        self,
        bank_identifier: str = None,
        branch_key: str = None,
        account_number: str = None,
        debit_entries: int = None,
        debit_amount: Decimal = None,
        credit_entries: int = None,
        credit_amount: Decimal = None,
        final_balance: Decimal = None,
        currency: str = None,
    ) -> None:
        self.bank_identifier = bank_identifier
        self.branch_key = branch_key
        self.account_number = account_number
        self.debit_entries = debit_entries
        self.debit_amount = debit_amount
        self.credit_entries = credit_entries
        self.credit_amount = credit_amount
        self.final_balance = final_balance
        self.currency = currency
