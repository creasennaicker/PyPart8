import os


path = ''


obj = os.scandir()

print('Files and directories in `% s`' % path)
for entry in obj:
    if entry.is_dir() or entry.is_file():
        print(entry.name)

