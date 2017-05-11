import pytest
from parser import Parser


@pytest.fixture(scope='session')
def valid_lines():
  return map(
    str.lstrip, '''
    [2017-05-10 07:30:23] [INFO] [parser.Parser] info log
    contined info line #1
    contined info line #2
    [2017-05-10 07:30:23] [ERROR] [parser.Parser] error log
    contined error line #1
    contined error line #2
    [2017-05-10 07:30:23] [ERROR] [parser.Parser] debug log
    '''.split('\n')[1:-1])


@pytest.fixture(scope='session')
def invalid_lines():
  return map(
    str.lstrip, '''
    contined info line #1
    [2017-05-10 07:30:23] [INFO] [parser.Parser] info log
    contined info line #2
    '''.split('\n')[1:-1])


def test_parse_on_valid_lines(valid_lines):
  parser = Parser()
  for line in valid_lines:
    assert parser.parse(line) is not None


def test_parse_on_invalid_lines(invalid_lines):
  parser = Parser()
  with pytest.raises(ValueError):
    for line in invalid_lines:
      parser.parse(line)
