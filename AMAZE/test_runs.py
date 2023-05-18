import os

folder_path = "/home/mitul/_03_ Dev&git/AMAZE-CART/AMAZE/amezon_seller_data"  # replace with the path to your folder

# iterate over all files in the folder
for file_name in os.listdir(folder_path):
    # create new file name with spaces and dashes replaced by underscores
    new_file_name = file_name.replace(" ", "_").replace("-", "_")

    # check if the new file name is different from the old one
    if new_file_name != file_name:
        # rename the file
        os.rename(
            os.path.join(folder_path, file_name),
            os.path.join(folder_path, new_file_name),
        )
