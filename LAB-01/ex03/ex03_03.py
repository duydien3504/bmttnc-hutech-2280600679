def taotupletulist(lst):
    return tuple(lst)
input_list = input("Nhap day so cach nhau boi dau phay: ")
numbers = list(map(int, input_list.split(',')))
tupledayso = taotupletulist(numbers)
numbers = list(map(int, input_list.split(',')))
my_tuple = taotupletulist(numbers)
print("Day so duoc chuyen thanh tuple la: ", my_tuple)
print("List ", numbers)