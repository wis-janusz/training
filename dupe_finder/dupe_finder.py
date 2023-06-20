import os
import hashlib
from glob import glob

print('Finding files, may take a while.')
path = glob('./**/*.*', recursive=True, )
print(f'Found {len(path)} files.')

print('Getting file sizes, may take a while.')
sizes = {}

for file in path:

    filesize = os.path.getsize(file)
    if filesize not in sizes:
        sizes[filesize] = [file]
    else:
        sizes[filesize].append(file)


sizes = {key:value for (key,value) in sizes.items() if len(value) > 1}
print(f'Found {len(sizes.keys())} sizes with more than one file.')

print('Getting and comparing hashes, may take a while.')
dupes = {}

for size in sizes.keys():
    for file in sizes[size]:
        with open(file,'rb') as in_file:
            file_hash = hashlib.md5(in_file.read()).hexdigest()
            if file_hash not in dupes:
                dupes[file_hash] = [file]
            else:
                dupes[file_hash].append(file)

dupes = {key:value for (key,value) in dupes.items() if len(value) > 1}
print(f'Found {len(dupes.keys())} images with more than one copy.')
print('Writing output to dupes.txt')
with open('dupes.txt', 'w') as out_file:
    lines = [f'\n{key}: {str(value)}' for (key,value) in dupes.items()] 
    out_file.writelines(lines)