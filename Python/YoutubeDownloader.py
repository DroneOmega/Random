import pytube
import os
import ffmpeg

print("Type the URL of the video you want to download: ")
link = input(">>> ")

yt = pytube.YouTube(link)

video = yt.streams.filter(adaptive=True, file_extension='mp4').order_by('resolution').desc().first()
audio = yt.streams.filter(adaptive=True, only_audio=True).order_by('abr').desc().first()

def downloading():
    print("Would you like to download the (audio) or (video) file for this youtube video.")
    q = input(">>> ")
    if q == "audio":
        audio.download()
        print("Your audio has been downloaded")
        print("Would you like to download another audio or video file. Type (yes) or (no).")
        q1 = input(">>> ")
        if q1 == "yes":
            print("========================================================================")
            downloading()
        elif q1 == "no":
            print("Thank you for downloading")
    elif q == "video":
        video.download(filename='video1')
        audio.download(filename='audio1')
        title = yt.title
        cmd = "ffmpeg -i video1.mp4 -i audio1.webm -c:v copy -c:a aac output.mp4"
        os.system(cmd)
        os.system('rm video1.mp4')
        os.system('rm audio1.webm')
        print("Your video has been downloaded.")
        print("Would you like to download another video or audio file. Type (yes) or (no).")
        q2 = input(">>> ")
        if q2 == "yes":
            print("========================================================================")
    else:
        print("This Is Invalid. Please check your spelling.")
        downloading()
downloading()
