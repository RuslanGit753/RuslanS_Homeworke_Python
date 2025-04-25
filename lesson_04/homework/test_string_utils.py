from string_utils import StringUtils
import pytest


@pytest.fixture(scope="session")
def string_utils():
    return StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, result', [
    ('Как дела?', 'Как дела?'),
    ('какой хороший день', 'Какой хороший день'),
])
def test_capitalize(string_utils, input_text, result):
    assert string_utils.capitalize(input_text) == result


@pytest.mark.negative_test
@pytest.mark.parametrize('input_text, result', [
    (' ', ' '),
    (' какой хороший день', ' какой хороший день'),
    ('', ''),
    ('13312', '13312'),
])
def test_capitalize_negative(string_utils, input_text, result):
    assert string_utils.capitalize(input_text) == result


@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, result', [
    (' Как дела?', 'Как дела?')
])
def test_trim(string_utils, input_text, result):
    assert string_utils.trim(input_text) == result


@pytest.mark.negative_test
@pytest.mark.parametrize('input_text, result', [
    ('  Как дела?', 'Как дела?'),
    ('  ', ''),
    ('', '')
])
def test_trim_negative(string_utils, input_text, result):
    assert string_utils.trim(input_text) == result


@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, symbol, result', [
    ('Как дела?', 'К', True),
    ('Как дела?', 'д', True),
    ('Как дела?', '?', True),
    ('Как дела?', ' ', True)
])
def test_contains(string_utils, input_text, symbol, result):
    assert string_utils.contains(input_text, symbol) == result


@pytest.mark.negative_test
@pytest.mark.parametrize('input_text, symbol, result', [
    ('', '', True),
    ('Как дела?', '', True),
    ('Как дела?', 'о', False)
])
def test_contains_negative(string_utils, input_text, symbol, result):
    assert string_utils.contains(input_text, symbol) == result


@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, symbol, result', [
    ('Как дела?', 'К', 'ак дела?'),
    ('Как дела?', ' дела', 'Как?'),
    ('Как дела?', '?', 'Как дела'),
    ('Как дела?', ' ', 'Какдела?')
])
def test_delete_symbol(string_utils, input_text, symbol, result):
    assert string_utils.delete_symbol(input_text, symbol) == result


@pytest.mark.negative_test
@pytest.mark.parametrize('input_text, symbol, result', [
    ('Как дела?', 'O', 'Как дела?'),
    ('Как дела?', 'дд', 'Как дела?'),
    ('', '', '')
])
def test_delete_symbol_negative(string_utils, input_text, symbol, result):
    assert string_utils.delete_symbol(input_text, symbol) == result
