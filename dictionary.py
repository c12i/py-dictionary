import json
from difflib import get_close_matches
# import sys

# getting the data from the json file
handle = open("data.json")
data = json.load(handle)

def search(word=input("Enter a word to search: ").lower()):
    # an array of close matches, with a cutoff of 0.6
    close = get_close_matches(word, data.keys(), cutoff=0.7)

    if word in data:
        print(data[word])
    elif len(close) > 0:
        # returns the value at index 0, the closest match
        print("Oops, did you mean {} instead?".format(close[0]))
    else:
        print("The word does not exist, please check again.")

search()