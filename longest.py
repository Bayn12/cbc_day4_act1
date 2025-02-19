def find_longest_word(sentence):
    
    words = sentence.split()
    
    longest_word = ""
    
    for word in words:
        
        if len(word) > len(longest_word):

            longest_word = word 
    
    print(f"The longest word is: '{longest_word}'")
    
    is_longer_than_five = len(longest_word) > 5
 
    print(f"Is the longest word longer than 5 characters? {is_longer_than_five}")

input_sentence = "The quickey brown fox jumps over the lazy dog"
find_longest_word(input_sentence)