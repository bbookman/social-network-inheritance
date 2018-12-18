from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp = None, user = None):
        self.text = text
        self.timestamp = timestamp or datetime.utcnow()
        self.user = user

    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)


    def __str__(self):
        return '@{name}: "{text}\n\t{date}"'.format(name = self.user.name, text = self.text, date = self.timestamp) 


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp) 
        self.image_url = image_url
        
    def __str__(self):
        return '@{name}: "{text}\n\t{image_url}\n\t{date}"'.format(name = self.user.name, text = self.text, image_url = self.image_url, date = self.timestamp) 

class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None): #'@Kevin Checked In: "Sample post text"\n\t-34.603722, -58.381592\n\tTuesday, Jan 10, 2017'
        super(CheckInPost, self).__init__(text)
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return '@{name} Checked In: "{text}\n\t{latitude}, {longitude}\n\t{date}"'.format(name = self.user.name, text = self.text, latitude = self.latitude, longitude = self.longitude )
