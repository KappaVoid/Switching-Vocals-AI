class YoutubeVideo:

    def __init__(self, title, duration, url):
        self.title = title
        self.duration = duration
        self.original_video_title = ''.join(e for e in self.title.lower().replace("switching vocals","").replace("switching vocal","").replace("nightcore","").replace("lyrics","") if e.isalnum() or e == ' ')
        #print("Swithing Vocals title: " , self.title)
        #print("Original title: " , self.original_video_title)
        self.url = url
        self.minutes = duration.replace("PT", "").split("M")[0]
        if len(duration.replace("PT", "").split("M")) > 1:
            self.seconds = duration.replace("PT", "").split("M")[1].replace("S", "")
        else:
            self.seconds = 0

        # print(self.minutes, ":", self.seconds)

    def add_original_video(self, original_video):
        self.orginal_video = original_video
 