from main import get_keyword


def test_get_keyword(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: x)
    assert get_keyword() == 'Keyword: '
