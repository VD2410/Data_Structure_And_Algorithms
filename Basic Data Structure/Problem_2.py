import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    dir_contains = os.listdir(path)

    files = list()

    for element in dir_contains:

    	element_path = os.path.join(path, element)
    	# print(element_path[-2:])

    	if os.path.isdir(element_path):
    		files += (find_files(suffix,element_path))

    	elif element_path[-2:] == suffix:
    		files.append(element_path)

    return files



# Testing with suffix == ".c"

print("-----------------------------Test 1-------------------------------------")

print(find_files(".c", "./testdir"))


print("-----------------------------Test 2-------------------------------------")

print(find_files(".k", "./testdir"))


print("-----------------------------Test 3-------------------------------------")

print(find_files("", "./testdir"))

print("-----------------------------Test 4-------------------------------------")

print(find_files("", ""))