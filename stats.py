def text_from_book(text):
    num_words = text.split()
    total = len(num_words)
    print(f"Found {total} total words")

def repitition_in_book(repeated_string):
    dict = {}
    lower_case = repeated_string.lower()
    for char in lower_case:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def sorting(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append(f"char: {char}, count: {count}")

def sorton(char_dict):
    # Create a list to hold our dictionaries
    chars_list = []

    # Convert each character and count to a dictionary and add to the list
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})

    # Define a helper function for sorting
    def sort_by_count(dict_item):
        return dict_item["count"]

    # Sort the list by count (highest to lowest)
    chars_list.sort(reverse=True, key=sort_by_count)

    return chars_list
