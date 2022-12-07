import pytest

from time import perf_counter

LIMIT = 100000
FILE_SYSTEM_MEMORY = 70_000_000

def format_time(func):
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        func(*args, **kwargs)
        t2 = perf_counter()
        time_delta = t2 - t1
        if time_delta * 1000 < 1:
            print(f"{time_delta * 1000000:.3f} μs")
        elif time_delta < 1:
            print(f"{time_delta * 1000:.3f} ms")
        else:
            print(f"{time_delta:.3f} s")

    return wrapper()

class Directory:
    def __init__(self, name, parent_directory=None):
        self.name = name
        self.size = None
        self.files = []
        self.dirs = []
        self.parent_directory = parent_directory

    def add_file(self, file_):
        self.files.append(file_)
    
    def add_dir(self, dir_):
        self.dirs.append(dir_)
    
    def path(self):
        if self.parent_directory:
            if self.parent_directory.name == "/":
                return "/" + self.name
        elif self.name == "/":
            return "/"
        return self.parent_directory.path() + "/" + self.name
    
    def get_size(self, limit=LIMIT):
        if self.size is not None:
            return self.size
        # if self.size is not None:
        #     if self.size <= limit:
        #         print(f"returning size {self.size} for {self.path()}")
        #         print()
        #         return self.size
        #     return 0
        size = 0
        for file_ in self.files:
            size += file_.size
        for dir_ in self.dirs:
            size += dir_.get_size()
        # if limit is not None:
        #     if size > limit:
        #         return 0
        # print(f"returning size {size} for {self.path()}")
        # print()
        self.size = size
        return size
    
    def list_contents(self):
        print(self.path())
        for file_ in self.files:
            print(file_.path())
        for dir_ in self.dirs:
            dir_.list_contents()

    def __repr__(self):
        return self.path()

class File:
    def __init__(self, name, size, directory=None):
        self.name = name
        self.size = int(size)
        self.directory = directory

    def path(self):
        if self.directory:
            if self.directory.name == "/":
                return "/" + self.name + " " + str(self.size)
        return self.directory.path() + "/" + self.name + " " + str(self.size)

    def __repr__(self):
        return self.name

class AllDirectories:
    def __init__(self):
        self.directories = {}

    def add_directory(self, directory):
        self.directories[directory.path()] = directory

    def get_directory(self, path):
        return self.directories[path]

root_directory = Directory(name="/")
ad = AllDirectories()

def compute1(data):
    current_directory = root_directory
    commands = data.split("$ ")
    for command in commands:
        if command.startswith("cd"):
            cd, dir_name = command.strip().split(" ")
            # If the destination is the root directory, change the current directory to the root directory.
            if dir_name == "/":
                # If the current directory is the root directory, do nothing.
                if current_directory.name == "/":
                    continue
                # Otherwise, change the current directory to the root directory.
                current_directory = root_directory
                continue
            # If the destination is '..', go up one directory.
            elif dir_name == "..":
                if current_directory.name == "/":
                    raise FileNotFoundError("Cannot go up from root directory.")
                current_directory = current_directory.parent_directory
                continue
            # If the destination is a regular name, search for the directory with that name.
            for dir_ in current_directory.dirs:
                if dir_.name == dir_name:
                    current_directory = dir_
                    break
            else:
                # If the subdirectory is not found, raise a FileNotFoundError.
                raise FileNotFoundError(f"Directory '{dir_name}' not found in '{current_directory.path()}'")
            
        # If the command is 'ls', list the contents of the current directory.
        elif command.startswith("ls"):
            lines = command.strip().split("\n")
            # Iterate through the directory contents.
            for line in lines[1:]:
                # If the line is a directory
                if line.startswith("dir"):
                    dir_name = line.split(" ")[1]
                    current_directory.add_dir(Directory(dir_name, current_directory))
                # If the line is a file
                else:
                    file_size, file_name = line.split(" ")
                    file_ = File(file_name, file_size, current_directory)
                    file_.directory.add_file(file_)


    total_size = 0
    root_directory.get_size()

    tracked_directories = [root_directory]
    td = 0
    while td < len(tracked_directories):
        current_directory = tracked_directories[td]
        # total_size += current_directory.get_size(limit=LIMIT)
        tracked_directories.extend(current_directory.dirs)
        td += 1
        
    for dir_ in tracked_directories:
        ad.add_directory(dir_)
        if dir_.size is not None:
            if dir_.size <= LIMIT:
                total_size += dir_.size
        else:
            print(dir_.path())
    return total_size



def compute2(data):
    UNUSED_MEMORY = FILE_SYSTEM_MEMORY - root_directory.size
    NEEDED_MEMORY = abs(UNUSED_MEMORY - 30_000_000)
    print(f"UNUSED_MEMORY: {UNUSED_MEMORY}")
    print(f"NEEDED_MEMORY: {NEEDED_MEMORY}")
    del_dir = None
    for dir_path, dir_ in ad.directories.items():
        if dir_.size >= NEEDED_MEMORY:
            if del_dir is None:
                del_dir = dir_
            elif dir_.size < del_dir.size:
                del_dir = dir_
    print(f"Deleting {del_dir.path()} with size {del_dir.size}")
    return del_dir.size

def main():
    with open("2022/Day_07/input.txt") as f:
        data = f.read()
    answer = compute1(data)
    print(answer)
    answer = compute2(data)
    print(answer)


@pytest.mark.parametrize("input_, expected", [
    ("""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""", 95437),
    ])
def test1(input_, expected):
    assert compute1(input_) == expected


@pytest.mark.parametrize("input_, expected", [
    ("""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""", 24933642),
    ])
def test2(input_, expected):
    assert compute2(input_) == expected


if __name__ == "__main__":
    format_time(main)
