import time
from pathlib import Path

from moviepy.editor import VideoFileClip


class GetAudio:
    @staticmethod
    def get_audio():
        """Extract audio from a given videofile and save it as an MP3."""
        while True:
            filename = input("Enter a file name including extension: ")

            if filename == "q":
                exit("Good bye!")

            filename = Path(filename)

            try:
                video = VideoFileClip(f"{filename}")
            except AttributeError as e:
                print(
                    f"The video file {filename} could not be found.\nPlease check that you entered the correct path.\n"
                )
                continue
            except OSError as e:
                print(
                    f"The video file {filename} could not be found.\nPlease check that you entered the correct path.\n"
                )
                continue

            audio = video.audio
            audio.write_audiofile(f"{filename.stem}_audio_{time.time()}.mp3")


if __name__ == "__main__":
    GetAudio.get_audio()
