# parser_with_authorization.py
import requests
import bs4

LOGIN_URL = 'http://158.160.172.156/login/'


session = requests.session()
take_token = session.get(LOGIN_URL)
take_token_split = take_token.text.split()
for i in take_token_split:
    if 'value=' in i and len(i) > 10:
        a = i
token = a.split('"')


data = {
        'csrfmiddlewaretoken': token[1],
        'username': 'test_parser_user',
        'password': 'testpassword',  
}


response = session.get(LOGIN_URL, data=data)
enter = session.post(LOGIN_URL, data=data)
print(enter.status_code)
