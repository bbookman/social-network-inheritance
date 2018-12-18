import pdb
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def add_post(self, post):
        self.posts.append(post)

    def get_timeline(self):
        timeline = []
        #pdb.set_trace()
        for follower in self.following:
            timeline.append(follower.posts)
        timeline.sort(key= lambda follower: follower.post.timestamp)
        return timeline

    def follow(self, other):
        self.following.append(other)
    
    def __str__(self):
        return '{first} {last} - {email}.\n Following: {following}'.format(first = self.first_name, last = self.last_name, email = self.email)
