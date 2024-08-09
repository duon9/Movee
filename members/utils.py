
from .models import Member

def complex_hash(key, table_size = 20):
  hash_value = 0
  prime = 31
  for i, char in enumerate(key):
    hash_value += ord(char) * (prime ** i)
  return hash_value % table_size

def isAuthenticated(request):
    member_id = request.session.get('member_id')
    if member_id:
        try:
            member = Member.objects.get(id=member_id)
            return {'is_authenticated': True}
        except Member.DoesNotExist:
            return {'is_authenticated': False}
    return {'is_authenticated': False}

def is_password_strong(password, min_length=8):
    contains_special_character = False
    contains_uppercase_character = False
    contains_number = False
    contains_lowercase_character = False

    # Check if the password meets the minimum length requirement
    if len(password) < min_length:
        return False

    for ch in password:
        if ch.islower():
            contains_lowercase_character = True
        elif ch.isupper():
            contains_uppercase_character = True
        elif ch.isdigit():
            contains_number = True
        elif not ch.isalnum():
            contains_special_character = True

    # Assess the password by checking all conditions
    return all([
        contains_special_character,
        contains_uppercase_character,
        contains_number,
        contains_lowercase_character
    ])
      
