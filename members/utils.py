
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
