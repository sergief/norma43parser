from norma43parser import Norma43Document, MovementLine, DateFormat

from norma43parser.parsers.movement_line_extra_information_parser import MovementLineExtraInformationParser


class TestMovementLineParser:
    @classmethod
    def setup_class(cls):
        cls.CONTENT = ["2301LIQ. OP. N 000000000000069", "2302AUTOMOCION LAGUNA SL 41001 SEVILLA ES"]

    def test_parse_extra_information(self):
        norma_43_document = Norma43Document()
        norma_43_document.movement_lines = [MovementLine()]
        for line in self.CONTENT:
            norma_43_document = MovementLineExtraInformationParser.parse(line, norma_43_document, DateFormat.SPANISH)

        extra_information = norma_43_document.movement_lines[0].extra_information

        assert len(extra_information) == 2
        assert extra_information[0] == "LIQ. OP. N 000000000000069"
        assert extra_information[1] == "AUTOMOCION LAGUNA SL 41001 SEVILLA ES"
