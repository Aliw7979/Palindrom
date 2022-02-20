def palindrome_checker(input_string):
    len_of_str=len(input_string)/2
    for i in range(0,int(len_of_str)):
        if input_string[-i-1] != input_string[i]:
            return False
    return True


def get_letters_without_duplication(input_string):
    list_of_letters = []
    for i in input_string:
        if not i in list_of_letters:
            list_of_letters.append(i)
    return list_of_letters

def palindrome_generator(user_input):
    letters = get_letters_without_duplication(input_string)
    for i in letters:
        for j in range(0,len(user_input)+1):
            temp = user_input[:j] + i + user_input[j:]
            if palindrome_checker(temp):
                return True


n = input()
for i in range(0, int(n)):
    input_string = input()
    if palindrome_checker(input_string):
        print("YES")
    else:
        if palindrome_generator(input_string):
            print("YES")
        else:
            print("NO")



