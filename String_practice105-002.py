

school = "McHenry County College"

letter = school[0]
print letter


length = len(school)
last = school[length-1]
print length


index = 0
while index < len(school):
    letter = school[index]
    print letter
    index = index + 1


school = 'Mchenry County College'
print school[0:7]
print school[8:14]
print school[15:22]



def find(school, e):
    index = 0
    while index < len(school):
        if school[index] == e:
            return index
        index = index + 1
    return -1

word = "Mchenry County College"
count = 0
for letter in word:
    if letter == 'e':
        count = count + 1
print count

word = "Mchenry County College"
count = 0
for letter in word:
    if letter == 'y':
        count = count + 1
print count


college = word.upper()
word = 'school'
new_word = word.upper()
print new_word





