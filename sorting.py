# I am Prerak Patel and I have designed this program by myself and I haven't share
# my program with anyone. My professor's name is Tiffany, Anotopoloski

myList = input("Please enter the list from where you want to seach for : ")
your_search = input("Please enter the word you want to search for : ")

letter_count = 0
comma_count = 0
real_list = []

for letter in myList :
    if letter.isalpha():

        if letter_count == comma_count:
            letter_count += 1

            real_list += [letter]
        
        else:
            
            real_list[letter_count - 1] += letter


    elif letter is ",":
        comma_count += 1


left = 0
right =  letter_count - 1
result = ""
if your_search not in myList :
    result = -1

else:
    while not result.isdecimal() :
    
        middle = int((left + right)/2)
        if real_list[middle] < your_search :
            right = middle - 1
            

        elif real_list[middle] > your_search :
            left = middle + 1
            
            
        elif real_list[middle] == your_search :
            result = str(middle)
print(result)
