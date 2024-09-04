"""Read file from web and do analysis of data
"""
#import requests 
from urllib.request import urlopen


def count_words_from_web_file(file_address):
    """Reads a file from the web and returns the file content as a string

    Args:
        file_address (str): web address to the file

    Returns:
        str: the content of the file
    """
    #response = requests.get(file_address)
    #return response.text
    words = 0
    with urlopen(file_address) as data:
        for line in data:
            line = line.decode('utf-8') # convert bytes to string
            line = line.split()
            words += len(line)
    return words


def main():
    """Driven Function
    """
    file_address = 'http://icarus.cs.weber.edu/~hvalle/sample_data/poem.txt'
    word_count = count_words_from_web_file(file_address)
    print("File contains ", word_count, " words.")

if __name__ == '__main__':
    main()