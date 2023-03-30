from typing import Generator, TextIO

import pytest

from . import main


@pytest.fixture
def data() -> list[str]:
    return ['111111dj1111\n', 'sdflsBohdan554k dj']


@pytest.fixture
def input_file(tmp_path: str, data: list[str]) -> Generator[TextIO, None, None]:
    with open(f'{tmp_path}/tmp_file.txt', 'w') as file:
        file.writelines(data)
    file = open(f'{tmp_path}/tmp_file.txt', 'r')
    yield file
    file.close()


def test_get_keyword(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: x)
    assert main.get_keyword() == 'Keyword: '


def test_get_data_from_file(monkeypatch, input_file, data):
    monkeypatch.setattr('builtins.open', lambda x: input_file)
    assert main.get_data_from_file('') == data


@pytest.mark.parametrize('keyword,expected', (
        ('Bohdan554', ['sdflsBohdan554k dj']),
        ('dj', ['111111dj1111\n', 'sdflsBohdan554k dj']),
))
def test_filter_data(keyword, expected, data):
    assert main.filter_data(data, keyword) == expected
