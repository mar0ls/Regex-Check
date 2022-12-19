import re

print('''|  _ \ ___  __ _  _____  __     / ___| |__   ___  ___| | __
| |_) / _ \/ _` |/ _ \ \/ /____| |   | '_ \ / _ \/ __| |/ /
|  _ <  __/ (_| |  __/>  <_____| |___| | | |  __/ (__|   < 
|_| \_\___|\__, |\___/_/\_\     \____|_| |_|\___|\___|_|\_\
            
----m4r0ls------------------     
Input:
- quit to exit ;
- help to display help;
- your regex .                                  
           ''')
txt = open('strings.txt', "r")

run = True

while run:
    regex = str(input("Your choice:  "))
    if regex == 'quit':
        print("Goodbye bro")
        txt.close()
        run = False
    elif regex == 'help':
        print('''Input your regax with using:
[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
\A	Returns a match if the specified characters are at the beginning of the string		
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")		
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")		
\d	Returns a match where the string contains digits (numbers from 0-9)	
\D	Returns a match where the string DOES NOT contain digits		
\s	Returns a match where the string contains a white space character		
\S	Returns a match where the string DOES NOT contain a white space character	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	
\W	Returns a match where the string DOES NOT contain any word characters	
\Z	Returns a match if the specified characters are at the end of the string
[]	A set of characters	
\	Signals a special sequence (can also be used to escape special characters)	
.	Any character (except newline character)		
^	Starts with		
$	Ends with		
*	Zero or more occurrences		
+	One or more occurrences		
?	Zero or one occurrences		
{}	Exactly the specified number of occurrences	
|	Either or	"falls|stays"	
()	Capture and group	''')
    else:
        for word in txt:
            if re.search(regex, word):
                print(word)
                continue

