class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return "Test by Test Author (0 posts)"

    def create_post(self, title, content):
        pass

    def json(self):
        pass