# Preschooler number recognition game. 
# Mommy or Daddy reads the number, preschooler types it out with digits.
# Reward is a page of cat gifs!!!
# github/foralma

import random, webbrowser

number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

number_words_tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

number_words_ones = ["", "-one", "-two", "-three", "-four", "-five", "-six", "-seven", "-eight", "-nine"]

for i in range(len(number_words_tens)):
    for j in range(len(number_words_ones)):
        number_words.append(number_words_tens[i]+number_words_ones[j])

number_words.append("one hundred")

number_strings = []
for i in range(101):
    number_strings.append(str(i))

print("")

child_name = input("What is your name? ")
cn = child_name[0].upper()+child_name[1:].lower()
print("")

limit = input("What is the highest number you can count to, " + cn + "? ")
if limit not in number_strings:
    limit = "20" # change default depending on your preschooler's abilities
print("OK, %s, we will work up to %s." % (cn, limit))
print("")

get_right = input("How many questions does " + cn + " need to get right? ")
if get_right not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
    get_right = "7" # change default depending on your preschooler's abilities
print("%s must answer %s questions correctly. Let\'s get started!" % (cn, get_right))
print("")
print("*  *  *  *  *  *  *  *  *  *  *")

def number_typing():
    correct_so_far = 0
    while correct_so_far < int(get_right):
        print("")
        random_number = int(random.random()*(int(limit)+1))
        print("Mommy or Daddy read this number: %s." % number_words[random_number])
        guess1 = input("Now " + cn + ", type the number Mommy or Daddy said : ")
        if guess1 == str(random_number):
            correct_so_far += 1
            if correct_so_far < int(get_right):
                print("Good job, %s! %d more to go!" % (cn, int(get_right)-correct_so_far))
            else:
                print("Good job, %s! You answered %s questions correctly. Now we can look at cats." % (cn, get_right))  
        else:
            guess2 = input("That wasn\'t right. Try again: ")
            if guess2 == str(random_number):
                correct_so_far += 1
                if correct_so_far < int(get_right):
                    print("Good job, %s! %d more to go!" % (cn, int(get_right)-correct_so_far))
                else:
                    print("Good job, %s! You answered %s questions correctly. Now we can look at cats." % (cn, get_right))
            else:
                print("Sorry, %s. The correct answer is %s." % (cn, str(random_number)))
    
    
number_typing()
print("")

cat_gifs = input("Type the word \"cat\": ").upper()
if cat_gifs=="CAT":
    webbrowser.open("https://giphy.com/explore/cat", new=0, autoraise=True) # replace with other url if this site no longer works
else:
    webbrowser.open("https://giphy.com/explore/puppy", new=0, autoraise=True) # replace with other url if this site no longer works
print("")



