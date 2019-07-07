import os

for filename in os.listdir(os.getcwd()):
    if (filename.endswith(".mp4") and "hevc" not in filename): 
        os.system("ffmpeg -i {0} -c:v hevc_nvenc -rc vbr_hq -c:a copy hevc_nvenc.{0}".format(filename))
    else:
        continue