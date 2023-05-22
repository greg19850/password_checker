import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error: {res.status_code}! Please try again later.")
    return res

def get_password_leaks_count(hash_start, hash_end):
    hashes = (line.split(':')
              for line in hash_start.text.splitlines())
    for h, count in hashes:
        if h == hash_end:
            return count
        return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('UTF-8')).hexdigest().upper()
    first_5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first_5_char)
    return get_password_leaks_count(response, tail)


pwned_api_check('password123')
