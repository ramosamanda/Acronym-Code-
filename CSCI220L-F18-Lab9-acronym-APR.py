# CSCI220L-F18-Lab9-acronym-APR.py
# Amanda Ramos
# A program that allows the user to type in a phrase that outputs an acronym.

def acronym(phrase):
    acronym =""
    for words in phrase.split():
        acronym = acronym + words[0]
    return acronym
# end acronym

def main(): 
    sentence =input("Enter a phrase: ")
    sentenceupper = sentence.upper()
    answer = acronym(sentence)
    print(str(answer))
# end main
main()
    

