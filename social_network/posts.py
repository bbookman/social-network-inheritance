from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        if not timestamp:
            self.timestamp= datetime.today.strftime(%A , %b %d, %Y)
        else:
            self.timestamp = timestamp
        self.user = None
        # Tuesday, Jan 10, 2017'

    def set_user(self, user):
        self.user = user


# class TextPost(...):  # Inherit properly
#     def __init__(self, text, timestamp=None):
#         pass
#
#     def __str__(self):
#         pass


# class PicturePost(...):  # Inherit properly
#     def __init__(self, text, image_url, timestamp=None):
#         pass
#
#     def __str__(self):
#         pass


# class CheckInPost(...):  # Inherit properly
#     def __init__(self, text, latitude, longitude, timestamp=None):
#         pass
#
#     def __str__(self):
#         pass
