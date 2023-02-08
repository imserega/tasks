#File Iterator API
# Using os, walk

import os

class FileIterator:
    def __init__(self, root, only_files, only_dirs, pattern) -> None:
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern

    def __iter__(self):
        pass

    def __next__(self):
        pass
            
    def next(self):
        pass
        # raise StopIteration()

print(os.path.abspath(__file__))




fileIterator = FileIterator(".", False, False, None)




