import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f"Error: {res.status_code}! Please try again later.")
    return res


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('UTF-8')).hexdigest().upper()
    first_5_char, tail = sha1password[:5], sha1password[5:]
    request_api_data(first_5_char)


pwned_api_check('password123')
