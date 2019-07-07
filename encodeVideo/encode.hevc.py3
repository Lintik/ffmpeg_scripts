import os

for filename in os.listdir(os.getcwd()):
    if (filename.endswith(".mp4") and "hevc" not in filename): 
        os.system("ffmpeg -i {0} -preset slow -c:v hevc -crf 23 -c:a copy hevc.{0}".format(filename))
    else:
        continue