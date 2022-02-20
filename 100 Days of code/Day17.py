class User:

    def __init__(self, user_id, username):
        # Initialize the attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, other_user):
        self.following += 1
        other_user.followers += 1


user1 = User("1", "johndoe")
user2 = User("2", "selena")

user1.follow(user2)
print(f"user1.following: {user1.following}")
print(f"user1.followers: {user1.followers}")
print(f"user2.following: {user2.following}")
print(f"user2.followers: {user2.followers}")
