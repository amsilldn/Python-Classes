#Amanda Sill
#Group 06
#LP1

#define function
def show_list(lst):
    print("The current possible passwords are:\n", "-" * 30)
    #for every 5 passwords print them on one line
    for i in range(len(lst)):
        print(lst[i], end = " ")
        if i % 5 == 4:
            print(lst[i])
    #also print the number of possible passwords in the list
    print("\n(", len(lst), "possible)")


#main
        
#create list and open file using list comprehension
passwords = [line.strip() for line in open("passwords.txt", "r")]
#call function
show_list(passwords)

#clue 1
print("\nClue 1: The password is at least 6 characters long.")
#clue 1 list comprehension
#for password in passwords if the password is >= 6 characters long
#append to list
six_char = [password for password in passwords if len(password) >= 6]
#call function
show_list(six_char)

#clue 2
print("\nClue 2: The password contains at least one letter.")
#clue 2 list comprehension
#for password in six_char
    #if there is a letter in the password
        #append password to the list
one_letter = [passw for passw in six_char
              if passw.isdigit() == False]
#call function
show_list(one_letter)

#clue 3
print("\nClue 3: The password does not start with a vowel, but the second character is a vowel")
#clue 3 list comprehension
#for password in one letter
    #if password[1] is a vowel AND password[0] is not a vowel
        #append password to list
vowel = [passw for passw in one_letter if passw[1] in "aeiou" and passw[0] not in "aieou"]
#call function
show_list(vowel)

#clue 4
print("\nClue 4: The password has at least twice as many consonants as vowels.")
#clue 4 list comprehension
#for password in vowel
    #if password[i] not in "aeiou" == password[i] in "aeiou" ** 2
        #append password to the list
consonants = [passw for passw in vowel if len([let for let in passw if let not in "aeiou"]) >=
                                              (2 * len([let for let in passw if let in "aeiou"]))]
#call function
show_list(consonants)

#BONUS - clue 5 - this one isn't 100%
print("\nClue 5: The password has the same letter twice in a row.")
#clue 5 list comprehension
#for password in consonants
    #if two letter snext to each other are the same
        #append to the list
let_row = [passw for passw in consonants if len([passw[i] for i in range(len(passw))]) == len([passw[j] for j in range(len(passw))])]
#call function
show_list(let_row)

