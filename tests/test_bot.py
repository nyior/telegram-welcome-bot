import pytest
from telegrambot.bot import (
                                get_user_first_name, 
                                get_chat_id)


@pytest.fixture
def update_with_expectedkey():
    """
    function to return an object that simulates json update
    posted to the bot's fall back webhook url
    this data has the expected key and chat_id of typ int
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
                            },
                            'chat': {
                                        'id':1
                                    }
                }
            }

    return update


@pytest.fixture
def update_without_expectedkey():
    """
    function to return an object that simulates json 
    update posted to the bot's fall back webhook url
    but without the expected 'new_chat_member' key 
    and chat id not int
    """
    update = {
                'update_id': 418763186,
                'message': {
                            'message_id': 59,  
                            'date': 1611506709, 
                            'chat': {
                                        'id':"nyior"
                                    }
                }
            }

    return update


def test_get_user_first_name(update_with_expectedkey):  
    """
    Method to test the get_user_first_name function
    """
    first_name = get_user_first_name(update_with_expectedkey)

    assert first_name.lower() == "nyior"


def test_get_chat_id(update_with_expectedkey):  
    """
    Method to test the get_chat_id function
    """
    assert get_chat_id(update_with_expectedkey) == 1


def test_raises_exception_on_key_not_found(update_without_expectedkey):
    with pytest.raises(KeyError):
        get_user_first_name(update_without_expectedkey)


def test_raises_exception_on_not_int(update_without_expectedkey):
    with pytest.raises(TypeError):
        get_chat_id(update_without_expectedkey)