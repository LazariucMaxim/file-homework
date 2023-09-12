import os


def len_file(file):
    with open(f'files/{file}') as f:
        return len(f.readlines())


files = sorted(os.listdir('files'), key=len_file)
files.remove('final_file.txt')
with open('files/final_file.txt', 'w') as final_file:
    for num, file in enumerate(files):
        final_file.write('\n'*bool(num)+file+'\n')
        final_file.write(str(len_file(file))+'\n')
        with open(f'files/{file}') as current_file:
            final_file.write(current_file.read())
