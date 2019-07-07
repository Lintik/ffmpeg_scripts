import os

for filename in os.listdir(os.getcwd()):
    if (filename.endswith(".mov")): 
        os.system("ffmpeg -i {0} -c copy {0}.pm4".format(filename))
    else:
        continue