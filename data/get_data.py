"""Download data from our server
"""
import urllib.request
import zipfile
import os
import sys
SERVER_URL = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/'
SAVING_DIRECTORY = "./data/Downloads"


def download_file(url: str, file_name: str):
    # TODO: Download to pwd
    if not os.path.exists(SAVING_DIRECTORY):
        os.makedirs(SAVING_DIRECTORY)
    file_path = os.path.join(SAVING_DIRECTORY, file_name)
    print("Downloading file: ", file_name )
    urllib.request.urlretrieve(url + file_name, file_path)

    if file_name.endswith(".zip"):
        unzip_file(file_path)

# TODO: Create a function to download the files from Kaggle directly by passing the dataset name

def unzip_file(file_path):
    # TODO: Unzip file
    if not os.path.exists(SAVING_DIRECTORY):
        os.makedirs(SAVING_DIRECTORY)
    with zipfile.ZipFile(file_path, 'r') as zip_file:
        zip_file.extractall(SAVING_DIRECTORY)
        print("Extracted files: ", zip_file.namelist())


def main():
    """Driven Function
    """
    # -i for icarus
    # -k for kaggle
    # -s for other servers <SERVER> <FILE>
    # If no arguments are provided, print a usage message
    data = 'seaborData.zip'
    if len(sys.argv) == 2:
        download_file(SERVER_URL, sys.argv[1])
        return
    
    
    download_file(SERVER_URL, data)



if __name__ == '__main__':
    main()