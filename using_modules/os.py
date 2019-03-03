#!/usr/bin/python3

# import os
# home=os.getcwd()
# print(home)

# # browser=os.system("/usr/bin/google-chrome")

# a=os.system('google-chrome "https://www.hattrick.org/"')
# b=os.system('google-chrome "https://www.google.com/"')
# os.system(a + b)

import os, shutil, time

root_src_dir = r'/home/mrgrumpy/Documents'
root_dst_dir = '/home/mrgrumpy/Backup/' + time.asctime()

for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        shutil.copy(src_file, dst_dir)

print(">>> BACKUP COMPLETE <<<")