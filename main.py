import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))


def translate(find_word):
    find_word = find_word.lower()
    if find_word in data:
        return data[find_word]
    elif len(get_close_matches(find_word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if Yes or N if NO:" % get_close_matches(find_word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(find_word, data.keys())[0]]
        elif yn == "N":
            return "The Word doesn't exist.Please double check it."
        else:
            return "we didn't understand your entry."
    else:
        return "The word doesn't exist.Please double check it"


input_word = input("Enter word: ")
output = translate(input_word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)