class Show:

    def __init__(self, name, description, url, img):
        self.name = name
        self.desc = description
        self.url = url
        self.img = img

    def __str__(self) -> str:
        return '[Title: {}, description: {}, url: {}, img: {}]'.format(self.name, self.desc, self.url, self.img)
