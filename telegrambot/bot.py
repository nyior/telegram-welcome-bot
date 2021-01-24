import requests
from decouple import config
from bottle import (  
    run, post, response, request as bottle_request
)


TOKEN = config('TOKEN')
BOT_URL = f"https://api.telegram.org/bot{TOKEN}/" 


def get_user_first_name(data):  
    """
    Method to extract a newly added user's first name.
    """
    # first_name = data['message']['new_chat_member']['first_name']
    # return first_name
    pass


def send_message(prepared_data):  
    """
    Prepared data should be json which includes at least `chat_id` and `text`
    """ 
    message_url = BOT_URL + 'sendMessage'
    requests.post(message_url, json=prepared_data)  # don't forget to make import requests lib


@post('/')
def main():  
    data = bottle_request.json

    print(data)
    # try:
    #     new_chat_member = data["message"]["new_chat_member"]
    #     username = new_chat_member["username"]
    #     print(f"user added: @{username}")
    # except KeyError as error:
    #     print(error)

    return response  # status 200 OK by default


if __name__ == '__main__':  
    run(host='0.0.0.0', port=8080, debug=True)