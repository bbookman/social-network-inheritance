
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.followers = []

    def add_post(self, post):
        self.posts.append(post)

    def get_timeline(self):
        timeline = []
        for follower in self.followers:
            timeline.append(follower.post)
        timeline.sort(key= lambda x: x.timestamp)
        return timeline

    def follow(self, other):
        self.followers.append(other)
