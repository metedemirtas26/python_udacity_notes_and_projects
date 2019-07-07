import os
def rename_files():
    file_list = os.listdir("/home/mt/phyton_udacity_notes_and_projects/prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir("/home/mt/phyton_udacity_notes_and_projects/prank")

    for file_name in file_list:
        os.rename(file_name,file_name.translate(None, "0123456789"))

    os.chdir(saved_path)
    
rename_files()