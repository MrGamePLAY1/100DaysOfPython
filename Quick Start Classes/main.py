class User:
    def __init__(self, user_id, user_name, user_age):
        print('New object being created.')
        self.id = user_id
        self.user_name = user_name
        self.user_age = user_age
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "Craig", 25)
user_2 = User('002', 'Steven', 25)

user_2.follow(user_1)
print('User 2 following count: ', user_2.following)
print('User 1 Followers: ', user_1.followers)

