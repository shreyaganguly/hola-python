import secret_messages
import pytest
import mock

def test_get_type():
    assert secret_messages.get_type("e") == "en"
    assert secret_messages.get_type("d") == "de"

def test_encode():
    assert secret_messages.encode("ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz0123456789","hello","1245") == "63AAD"

def test_decode():
    assert secret_messages.decode("ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz0123456789", "63AAD", "1245") == "hello"

def test_code():
    assert secret_messages.code("e","hello","1245") == "63AAD"
    assert secret_messages.code("d","63AAD","1245") == "hello"

# @pytest.mark.parametrize('valid_codes, valid_key', [('hello', "1245")])
# def test_start_messaging(valid_codes, valid_key):
#     print("*******************")
#     # secret_messages.input
#     print(valid_codes, valid_key)
#     # with mock.patch.object(builtins, 'input', lambda _: 'hello'):
#     with mock.patch('builtins.input', return_values=[valid_codes,valid_key]):
#         secret_messages.start_messaging("e")
#         # captured = capsys.readouterr()
#         # assert "63AAD" in captured.out

def test_start_messaging_success(capsys):
    input_values = ['hello', "1245"]

    def mock_input(s):
        return input_values.pop(0)
    secret_messages.input = mock_input

    secret_messages.start_messaging("e")

    captured = capsys.readouterr()
    assert "63AAD" in captured.out

def test_start_messaging_error(capsys):
    input_values = ['hello()', "1245"]

    def mock_input(s):
        return input_values.pop(0)
    secret_messages.input = mock_input

    secret_messages.start_messaging("e")

    captured = capsys.readouterr()
    assert "Wrong input! Please correct and try again" in captured.out

def test_start_messaging_error_key(capsys):
    input_values = ['hello', "abc"]

    def mock_input(s):
        return input_values.pop(0)
    secret_messages.input = mock_input

    secret_messages.start_messaging("e")

    captured = capsys.readouterr()
    assert "Wrong input! Please correct and try again" in captured.out


def test_init_secret_messages_game_success(capsys):
    input_values = ['e','hello', "1245"]
    def mock_input(s):
        return input_values.pop(0)
    secret_messages.input = mock_input

    secret_messages.init_secret_messages_game()

    captured = capsys.readouterr()
    assert "Start encrypting you message" in captured.out


def test_init_secret_messages_game_error(capsys):
    input_values = ['f']

    def mock_input(s):
        return input_values.pop(0)
    secret_messages.input = mock_input

    secret_messages.init_secret_messages_game()

    captured = capsys.readouterr()
    assert "Wrong input! Please correct and try again" in captured.out
