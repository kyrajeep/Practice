def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    sentence = str(sentence)
    list_words = sentence.split(" ")
    # the words are reversed
    list_words = list_words.reverse()
    back_to_string = ' '.join(word for word in list_words)
    back_to_string = back_to_string.swapcase()
    return back_to_string
    
    
if __name__ == '__main__':
   
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
