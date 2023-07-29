import time

from moviepy.editor import VideoFileClip


class GetAudio:
    @staticmethod
    def get_audio(filename: str):
        """Extract audio from a given videofile and save it as an MP3."""
        video = VideoFileClip(filename)
        audio = video.audio
        audio.write_audiofile(f"{filename.split('.')[0]}_audio_{time.time()}.mp3")


if __name__ == "__main__":
    GetAudio.get_audio("sasuke.mp4")
