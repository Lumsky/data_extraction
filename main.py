# import os #the os module is used for interacting with the operating system

# #This function retrieves information about files in the current directory
# #It returns a list of dictionaries, each containing the file name and its size in bytes 

# def get_file_info_in_directory():
#     file_info_list = []

#     # List all items in the current directory
#     for item in os.listdir():
#         # Check if it's a file (not a folder)
#         if os.path.isfile(item):
#             size = os.path.getsize(item)
#             file_info = {
#                 'name': item,
#                 'size': size  # size in bytes
#             }
#             file_info_list.append(file_info)

#     return file_info_list

# # 🔍 Run the function and print results
# file_data = get_file_info_in_directory()
# for file in file_data:
#     print(file)

import os

def get_file_info(path="."):
    file_info_list = []

    # Walk through all subdirectories and files recursively
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            size = os.path.getsize(full_path)

            file_info = {
                'name': file,
                'path': full_path,
                'size': size
            }

            file_info_list.append(file_info)

    return file_info_list

# Example 1: Use default (current working directory)
# current_files = get_file_info()
# for f in current_files:
#     print(f)

# Example 2: Specify a different directory
other_files = get_file_info("/Users/admin/Desktop/Cloud_vision")
for f in other_files:
    print(f)
