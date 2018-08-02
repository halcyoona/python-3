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
