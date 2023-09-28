def count_reap_char(input_string):
    char_count={}
    for char in input_string:
        if char.isalpha():
            if char.lower() in char_count:
                char_count[char.lower()]+=1
            else:
                char_count[char.lower()]=1
    return char_count

input_string=input("enter a string : ")
result=count_reap_char(input_string)
print(result)
