q=True
arr =[]
while q:
    w=input("Enter a Word : ")
    arr.append(w)
    k=input("Another Word : ")
    if k=='n':
        q=False
arr.sort()
str = ""
first_word = arr[0]
last_word = arr[len(arr)-1]
for i in range(len(first_word)):
    if first_word[i] == last_word[i]:
        str = str + first_word[i]
    else:
        break
print(str)