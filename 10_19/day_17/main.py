class User:
    
    username: str
    id: str
    followers: int
    following: int
    
    def __init__(
                    self,
                    id : str,
                    username: str
                ):
                    print('new user being created')
                    self.username = username
                    self.id = id
                    # Attribute with default value
                    self.followers = 0
                    self.following = 0
    
    # Method                    
    def follow(self, user):
        user.followers += 1
        self.following += 1
    

"""
    This form don't need the equals parametes,
    we need to define a contract in class
    Use init to define initialize values
"""
# user_1 = User()

# user_1.id = '001'
# user_1.username = 'angela'


# user_2 = User()

# user_2.id = '001'
# user_2.name = 'angela'

"""
    Better:
"""

user_3: User = User('001', 'Rafael')

print(user_3.username)


user_4: User = User('002', 'Luis')
user_4.follow(user_3)
print(user_4.username)

print('User 4 followers: ' + str(user_4.followers))
print('User 4 following: ' + str(user_4.following))

print('User 3 followers: ' + str(user_3.followers))
print('User 3 following: ' + str(user_3.following))