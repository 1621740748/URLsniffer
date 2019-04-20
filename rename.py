import glob
import os
for name in glob.glob(r"bdimg.share.baidu.com/**",recursive=True):
    #print(name)
    if("?" in name):
        os.rename(name,name.split("?")[0])

