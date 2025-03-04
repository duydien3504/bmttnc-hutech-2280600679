def daonguoclist(lst):
    return lst[::-1]
input_list = input("Nhap day so cach nhau boi dau phay: ")
numbers = list(map(int, input_list.split(',')))
listdaonguoc = daonguoclist(numbers)
print("Day so dao nguoc la: ", listdaonguoc)
# So, what is the difference between the two snippets?