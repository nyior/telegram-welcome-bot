import pytest
from telegrambot.bot import get_user_first_name


@pytest.fixture
def update_with_expectedkey():
    """
    function to return an object that simulates json update
    posted to the bot's fall back webhook url

    """
    update = {
                'update_id': 418763186,
                'message': {
                            'message_id': 59,  
                            'date': 1611506709, 
                            'new_chat_member': {
                                                'id': 1344418577, 
                                                'is_bot': False, 
                                                'first_name': 'Nyior', 
                                                'last_name': 'Clement'
                            }
                }
            }

    return update


@pytest.fixture
def update_without_expectedkey():
    """
    function to return an object that simulates json update
    posted to the bot's fall back webhook url
    but without the expected 'message' key
    """
    update = {
                'update_id': 418763186,
            }

    return update


def test_get_user_first_name(update_with_expectedkey):  
    """
    Method to extract a newly added user's first name.
    """
    first_name = get_user_first_name(update_with_expectedkey)

    assert first_name.lower() == "nyior"


def test_raises_exception_on_key_not_found(update_without_expectedkey):
    with pytest.raises(KeyError):
        get_user_first_name(update_without_expectedkey)