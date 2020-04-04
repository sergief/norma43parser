from norma43parser import Norma43Document, MovementLine, DateFormat, Account

from norma43parser.parsers.movement_line_extra_information_parser import MovementLineExtraInformationParser


class TestMovementLineParser:
    @classmethod
    def setup_class(cls):
        cls.CONTENT = ["2301PAYMENT OPERATION APPROVED", "2302GROCERIES AND OTHER PAYMENTS SSSLLLAB"]

    def test_parse_extra_information(self):
        norma_43_document = Norma43Document(accounts=[Account(movement_lines=[MovementLine()])])
        for line in self.CONTENT:
            norma_43_document = MovementLineExtraInformationParser.parse(line, norma_43_document, DateFormat.SPANISH)

        extra_information = norma_43_document.accounts[0].movement_lines[0].extra_information

        assert len(extra_information) == 2
        assert extra_information[0] == "PAYMENT OPERATION APPROVED"
        assert extra_information[1] == "GROCERIES AND OTHER PAYMENTS SSSLLLAB"
