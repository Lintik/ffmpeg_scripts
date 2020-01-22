#video files must not contain space or other special characters
import os

for filename in os.listdir(os.getcwd()):
    if (filename.endswith(".mov")) or (filename.endswith(".mp4")): 
        os.system("ffmpeg -i {0} -c copy {0}.mkv".format(filename))
    else:
        continue