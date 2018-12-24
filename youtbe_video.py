class YoutubeVideo:
    def __init__(self, title, duration, url):
        self.title = title
        self.duration = duration
        self.url = url
        self.minutes = duration.replace("PT", "").split("M")[0]
        if len(duration.replace("PT", "").split("M")) > 1:
            self.seconds = duration.replace("PT", "").split("M")[1].replace("S", "")
        else:
            self.seconds = 0

        #print(self.minutes, ":", self.seconds)
