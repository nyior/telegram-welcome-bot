import requests
from decouple import config
from bottle import (  
    run, post, response, request as bottle_request
)


TOKEN = config('TOKEN') #retrieving the env var TOKEN
BOT_URL = f"https://api.telegram.org/bot{TOKEN}/" 


def get_user_first_name(data):  
    """
    Method to extract a newly added user's first name
    from telegram request
    """
    try:
        first_name = data['message']['new_chat_member']['first_name']
        return first_name
    except KeyError:
        exit


def get_chat_id(data):  
    """
    Method to extract chat id from telegram request.
    """
    chat_id = data['message']['chat']['id']

    if not isinstance(chat_id, int):
        raise TypeError('Please chat_id must be an integer')
    return chat_id


def prepare_welcome_text(data):  
    user = get_user_first_name(data)
    welcome_text = f""" 
                    *Hi {user}, welcome to the Bubbl Family*                                                                                                              we are _very_ glad to have you here :) Not required, but if you can, introduce yourself just so other members of this community get to know you.                                                                          _no fear, e no dey too serious_  :-))                                                                                                               Just tell us who you are, what you do, and your interests in the tech space and beyond if you want.
                   """

    json_data = {
        "chat_id": get_chat_id(data),
        "text": welcome_text,
        "parse_mode": "Markdown"
    }

    return json_data


def send_message(prepared_data):  
    """
    Prepared data should be json which includes at least `chat_id` and `text`
    """ 
    message_url = BOT_URL + 'sendMessage'
    requests.post(
                    message_url, 
                    json=prepared_data,
                    ) #import the requests lib first


@post('/')
def main():  
    data = bottle_request.json
    welcome_text = prepare_welcome_text(data)
    send_message(welcome_text)

    return response  # status 200 OK by default


if __name__ == '__main__':  
    run(host='0.0.0.0', port=8080, debug=True)