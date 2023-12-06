'''
Name: Leo Wei
Data: 2023 Nov 30
Reflection:
I found this project very fun while I worked on it, and I tried to go beyond what was required. I became more experienced
in using APIs as well as writing code faster. I also improved my debugging skills and it is only my second time using the
module 'logging', and it helped in controlling the debug messages.

Sources:
https://platform.openai.com/docs/api-reference/introduction
https://docs.python.org/3/library/textwrap.html

On my honor, I have neither given nor received unauthorized aid.
'''

import time
import logging
import requests
import json
import textwrap
import sys


logging.basicConfig(level=logging.ERROR) # toggle logging.ERROR or logging.DEBUG for debugging
TEXT_WRAPPING = True # boolean to toggle text wrapping
OUTPUT_MAX_WIDTH = 70 # text wrapping width

def send_api_request(messages):

    API_KEY = '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' # DO NOT DISCLOSE
    API_URL = 'https://api.openai.com/v1/chat/completions'

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"

    }

    body = {
        "model": "gpt-4-1106-preview", # GPT-4 Turbo model
        "messages": messages,
        "max_tokens": 500,
        "temperature": 0.5 # Consistency of the response (lower = more consistent)

    }


    response = requests.post(API_URL,headers=headers,data=json.dumps(body)) # send request

    # debug for response error codes
    if response.status_code == 200:
        logging.debug(f'API Request Successful.')
    else:
        logging.error(f'API Request Failed. Error Code {response.status_code}')
        logging.error(f'Received Response: {response.json()}')
        sys.exit(1) # Exit code with exit code 1

    response_dict = response.json()
    logging.debug(response_dict)
    response_content = response_dict['choices'][0]['message']['content'] # locate ai response
    return response_content


def ai_convo():
    messages = []
    while True:

        logging.debug(messages)
        user_input = input('>>> ')

        messages.append({'role': 'user','content': user_input})

        assistant_response = send_api_request(messages)
        messages.append({'role': 'assistant','content': assistant_response})

        if TEXT_WRAPPING:
            [print(wrapped_response) for wrapped_response in textwrap.wrap(assistant_response,width=70,replace_whitespace=False)]
        else:
            print(assistant_response)

def ai_talk_to_ai():
    messages = [{'role': 'user','content': 'Hello!'}]
    assistant_response = send_api_request(messages)
    messages.append({'role': 'assistant', 'content': assistant_response})

    if TEXT_WRAPPING:
        [print(wrapped_response) for wrapped_response in textwrap.wrap(assistant_response, width=70, replace_whitespace=False)]
    else:
        print(assistant_response)

    while True:
        #messages.append({'role': 'user', 'content': assistant_response})

        assistant_response = send_api_request([{'role': 'system','content': 'Begin your messages with \'We are both AI and were coded to talk to '
                                                                            'each other. Lets argue how to solve climate change\''}]+messages)
        messages.append({'role': 'assistant', 'content': assistant_response})

        if TEXT_WRAPPING:
            [print(wrapped_response) for wrapped_response in textwrap.wrap(assistant_response, width=70, replace_whitespace=False)]
            print('\n')
        else:
            print(assistant_response,'\n')

        for message in messages:
            if message['role'] == 'user':
                message['role'] = 'assistant'
            elif message['role'] == 'assistant':
                message['role'] = 'user'





def programmed_convo():
    print('Hey! What\'s your name?')
    user_name = input('>>> ')
    print(f'So I was tasked with programming a conversation with you, {user_name}.')
    time.sleep(2)
    print('Let\'s talk then.')
    time.sleep(2)
    print('How old are you?')
    while True:
        age = input('>>> ')
        try:
            age = int(age)
            break
        except ValueError:
            print('Please input a valid number!')
    print(f'Wow! You know, {age} is actually my lucky number!')
    time.sleep(2)
    print('What\'s your favorite color?')
    fav_color = input('>>> ').lower().strip().strip('.').strip('!')
    if fav_color == 'yellow':
        print('I love yellow too!')
    else:
        print(f'Cool. My favorite color is actually yellow. But I like {fav_color} too!')
    time.sleep(3)
    print('.')
    time.sleep(1)
    print('..')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print(f'Be honest, {user_name}. Is this conversation interesting? (Yes/No)')
    interest = input('>>> ').lower().strip().strip('.').strip('?').strip('!')
    if interest == 'yes':
        print('That\'s great!')
    elif interest == 'no':
        print('Yeah, I kinda agree.')
    else: print('I\'ll take that as a no then.')
    time.sleep(2)
    print('But, I\'ll be honest.')
    time.sleep(2)
    print('You can only go so far with pre-programmed conversations like this one.')
    time.sleep(2)
    print('And it\'s not all that dynamic, either.')
    time.sleep(2)
    print('However, there\'s something we can do.')
    time.sleep(2)
    print('Something very new to us.')
    time.sleep(2)
    print('What is it? You\'ll have to find out for yourself.')
    time.sleep(2)
    print(f'Enjoy the conversation, {user_name}!')
    time.sleep(2)
    print('(Say Anything)')


#programmed_convo()
#ai_convo()
ai_talk_to_ai()