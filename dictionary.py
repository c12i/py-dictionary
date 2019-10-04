import json
from difflib import get_close_matches
# import sys

# getting the data from the json file
handle = open("data.json")
data = json.load(handle)

print(
'''
Term-Dict (>__<)

'''
    )

print(
'''
A handy dictinary tool accessed through the terminal:

=====================
|                   |
|                   |
|    DICTIONARY     |
|                   |
|                   |
=====================
'''
    )

def search(word=input("Enter a word to search: ").lower()):
    # an array of close matches, with a cutoff of 0.6
    close = get_close_matches(word, data.keys(), cutoff=0.7)

    if word in data:
        print(data[word])
        print("-----------------------------------------")
    elif len(close) > 0:
        # returns the value at index 0, the closest match
        print("------------------")
        response = input("Oops, did you mean {} instead? Enter 'Y' if yes and 'N' if no: ".format(close[0])).lower()
        if response.startswith("y"):
            word = close[0]
            print(data[word])
            print("-----------------------------------------")
        else:
            pass       
    else:
        print("The word does not exist, please check again.")

search()