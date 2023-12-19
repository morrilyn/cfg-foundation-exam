## Concept Questions 19 marks 

"""An Isogram is a word in which no letter occurs more than once. For example, the word "isogram" is an Isogram, but the word "isograms" is not an Isogram (extra "s" exists). Similarly, the words "background" and "downstream" are Isograms. """

# The function should return True if the word is an isogram and False otherwise

def is_isogram(word):
    # First, we make the word lowercase to make sure that 'A' and 'a' are counted as the same letter
    word = word.lower()
    
    # We create an empty list to keep track of the letters we've seen
    seen_letters = []
    
    # Now we check each letter in the word
    for letter in word:
        # If we have already seen this letter, then it's not an isogram
        if letter in seen_letters:
            return False
        # If it's a new letter, we add it to our list of seen letters
        seen_letters.append(letter)
    
    # If we've checked all the letters and haven't found any repeats, it's an isogram
    return True

#test the function with examples
test_words = ["isogram", "machine", "ambidextrously", "alphabet", "A"]

# Check each word and return results in a dictionary
test_results = {word: is_isogram(word) for word in test_words}
test_results
print(test_results)