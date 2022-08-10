import re
mystr = '''Tata
Hello bro  
my self debashish sahu
i am come from india and i am a multi programmer.
phn no-8260770087
i know many types of programming language like python,
the fass  is what i dont know.
aiii  ai
23564-1243
c,c++ etc... which are most useful for working in computer system'''

#findall,search,split,sub,finditer
# print(r'\n')   #raw string
# patt = re.compile(r'fass')
# patt = re.compile(r'.')  #any character
# patt = re.compile(r'.sh') 
# patt = re.compile(r'^Tata')  #start with
# patt = re.compile(r'tem$')   #end with
# patt = re.compile(r'ai*')
# patt = re.compile(r'a*i*')
# patt = re.compile(r'ai+')
# patt = re.compile(r'ai{2}')
# patt = re.compile(r'(ai){1}')
# patt = re.compile(r'(ai){1}|fax')

#special sequences
# patt = re.compile(r'\ATata')
# patt = re.compile(r'age\b')
# patt = re.compile(r'\d{5}-\d{4}')
patt = re.compile(r'\d{10}')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
    # print(mystr[145:149])

'''meta character
[]=A set of character
\ signals a special sequence(can also be used to escape special characters)
. any character(except new line character)
^ start with
$ end with
* zero or more occurance
+ one or more occurance
{} exactly the specified number of occurance
| either or
() capture and group 

special sequence:
\A Return a match if the specified character are at the beggining of the string
\b return a match where the specified characeters at the biginning or at the end of a word r"ain\b"
\B Return a match where the specified character are present,but not at the beginning not at the end of the word
\d Returns a match where the string contains digits(0-9)
\D Returns a match where the string DOES NOT contain a white space character
\s Returns a match where the string contains a white space character
\S returns a match where the string DOES NOT contain a whitespace character
\w Returns a match where the string contains any word characters (character from a to z,digits from 0-9,and the underscore character_)
\W Returns a match where the string DOES NOT contain any word characters 
\Z Return a match where if the specified character are at the end of the string 
'''