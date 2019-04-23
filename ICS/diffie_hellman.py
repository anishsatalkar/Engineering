p = 17
q = 7


class User:

    def __init__(self, secret_int=None, secret_key=None, public_key=None, other_users_key=None):
        self.secret_int = secret_int
        self.secret_key = secret_key
        self.public_key = public_key
        self.other_users_public_key = other_users_key

    def calculate_public_key(self):
        self.public_key = (q ** self.secret_int) % p

    def calculate_secret_key(self):
        self.secret_key = (self.other_users_public_key ** self.secret_int) % p


Michael = User()
Dwight = User()

Michael.secret_int = 5
Dwight.secret_int = 3

Michael.calculate_public_key()
Dwight.other_users_public_key = Michael.public_key

Dwight.calculate_public_key()
Michael.other_users_public_key = Dwight.public_key

Michael.calculate_secret_key()

Dwight.calculate_secret_key()

print(Michael.secret_key)
print(Dwight.secret_key)
