class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

def get_user_id(self):
    return self._user_id

def get_name(self):
    return self._name

def get_access_level(self):
    return self._access_level

def set_name(self, name):
    self._name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'

def add_user(self, user_list, user):
    user_list.append(user)
    print(user_list)

def remove_user(self, user_list, user):
    user_list.remove(user)
    print(user_list)

users = []
admin1 = Admin("a1", "Steve)")
user1 = User("u1", "Peter")

print(user1, get_user_id(user1), get_name(user1))
