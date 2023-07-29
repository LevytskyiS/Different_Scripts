import os

from pytube import YouTube
from pytube.exceptions import RegexMatchError


class DownloadYoutuveVideo:
    @staticmethod
    def download_video():
        """Download a video from a Youtube link"""
        while True:
            DOWNLOAD_FOLDER = os.getcwd()
            video_url = input("Put youtube's url: ")

            if video_url == "q":
                exit("Bye")

            try:
                video_obj = YouTube(video_url)
            except RegexMatchError as e:
                print("That's not a Youtube link. Check it and try again.")
                continue

            stream = video_obj.streams.get_highest_resolution()
            stream.download(DOWNLOAD_FOLDER)

            print("Done\n")


if __name__ == "__main__":
    DownloadYoutuveVideo.download_video()
