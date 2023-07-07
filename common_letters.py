# problem 2:
# input: ["flower", "flour", "float"]
# output: "flo"

# input: ["flower", "flat", "flour"]
# output: "fl"

# input: ["flower", "mark"]
# output: ""
               
def find_common_letters(words):
    if not words:
        return None

    common_letters = set(words[0])

    for word in words[1:]:
        common_letters.intersection_update(word)

    if common_letters:
        return ''.join(sorted(common_letters))
    else:
        return None


# Example usage
words_list = ["flat", "flow"]
common = find_common_letters(words_list)
print(common)  # Output: fl

words_list = ["float", "floated"]
common = find_common_letters(words_list)
print(common)  # Output: float

words_list = ["cat", "dog"]
common = find_common_letters(words_list)
print(common)  # Output: None
               
