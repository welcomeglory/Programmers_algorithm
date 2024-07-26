def solution(my_string):
    return ''.join([char.lower() if char.isupper() else char.upper() for char in my_string ])