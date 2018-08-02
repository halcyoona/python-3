#This function takes one string argument.Returns a dictionary in which number of words and their repetetion is counted

def word_count(string):
    k = 0
    string = string.lower()
    my_dict = {}
    for k in range(len(string)):
        if string[k] == ' ':
            continue
        else:
            new_string = string[k:] + ' '
            break
    specail = "'"
    c = 0
    for p in new_string:
        if specail == p:
            c += 1
        else:
            continue
    if c==3:
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz'0123456789"
    word = ''
    total_word_list = []
    final_word_list = []
    count = 0
    for i in new_string:
        if i in alphabet:
            word += i
        else:
            if word == '':
                continue
            else:
                total_word_list.append(word)
                word = ''
    for j in total_word_list:
        if j in final_word_list:
            continue
        else:
            final_word_list.append(j)
            for k in range(len(total_word_list)):
                if j == total_word_list[k]:
                    count += 1
            my_dict[j] = count
            count = 0
    return my_dict















def word_count(string):
    k = 0
    string = string.lower()
    my_dict = {}
    for k in range(len(string)):
        if string[k] == ' ':
            continue
        else:
            new_string = string[k:] + ' '
            break
    alphabet = "abcdefghijklmnopqrstuvwxyz'0123456789"
    word = ''
    total_word_list = []
    final_word_list = []
    count = 0
    for i in new_string:
        if i in alphabet:
            word += i
        else:
            if word == '':
                continue
            else:
                total_word_list.append(word)
                word = ''
    for j in total_word_list:
        if j in final_word_list:
            continue
        else:
            final_word_list.append(j)
            for k in range(len(total_word_list)):
                if j == total_word_list[k]:
                    count += 1
            my_dict[j] = count
            count = 0
    return(my_dict)







