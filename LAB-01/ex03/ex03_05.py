def demsolanxuathien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
input_string = input("Nhap: ")
wordlist = input_string.split()
solansuat = demsolanxuathien(wordlist)
print(solansuat)