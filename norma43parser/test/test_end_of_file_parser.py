from norma43parser import Norma43Document
from norma43parser.parsers.end_of_file_parser import EndOfFileParser


def test_parse_end_of_file():
    line_content = "88999999999999999999123456"
    norma_43_document = EndOfFileParser.parse(line_content, Norma43Document(), "YMD")
    assert norma_43_document.reported_entries == 123456
