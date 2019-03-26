p = 17
q = 7


class User:

    def __init__(self, secret_int, secret_key, public_key, other_users_key):
        self.secret_int = secret_int
        self.secret_key = secret_key
        self.public_key = public_key
        self.other_users_key = other_users_key

    def calculate_public_key(self):
        self.public_key = (q ** self.secret_int) % p

    def calculate_secret_key(self):
        self.secret_key = (self.other_users_key ** self.secret_int) % p


Ramesh = User(0, 0, 0, 0)
Suresh = User(0, 0, 0, 0)

Ramesh.secret_int = 5
Suresh.secret_int = 3

Ramesh.calculate_public_key()
Suresh.other_users_key = Ramesh.public_key

Suresh.calculate_public_key()
Ramesh.other_users_key = Suresh.public_key

Ramesh.calculate_secret_key()

Suresh.calculate_secret_key()

print(Ramesh.secret_key)
print(Suresh.secret_key)
