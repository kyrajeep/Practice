while True:
    try:
       x = int(input("Please enter a number: "))
       break
    except ValueError:
       print("Oops!  That was no valid number.  Try again...")


t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
print(list(set(t)))

text = 'geeks for geeks' 
# Splits at space
print(text.split())
 
word = 'geeks, for, geeks'
 
# Splits at ','
print(word.split(', '))
 
word = 'geeks:for:geeks'
 
# Splitting at ':'
print(word.split(':'))
 
word = 'CatBatSatFatOr'
 
# Splitting at 3
print([word[i:i+3] for i in range(0, len(word), 3)])


