import hashlib
import hmac
import random
import string

SECRET_KEY = "DebugTalk"

def gen_random_string(str_len):
    random_char_list = []
    for _ in range(str_len):
        random_char = random.choice(string.ascii_letters + string.digits)
        random_char_list.append(random_char)

    random_string = ''.join(random_char_list)
    return random_string

def get_sign(*args):
    content = ''.join(args).encode('ascii')
    sign_key = SECRET_KEY.encode('ascii')
    sign = hmac.new(sign_key, content, hashlib.sha1).hexdigest()
    return sign

def get_content_type():
    content_type = "application/x-www-form-urlencoded; charset=UTF-8"
    return content_type

def get_password():
    content_type = "nideyangzi1"
    return content_type

def hook_print(*args):
    if args == "setup":
        pass
    elif args =="teardown":
        pass
    return

