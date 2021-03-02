class Programme:
    def __init__(self, title, category, channel, start, end):
        self.title = title
        self.category = category
        self.channel = channel
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.title} | {self.category} | {self.channel} | {self.start} | {self.end}"

    def __repr__(self):
        return self.__str__()
