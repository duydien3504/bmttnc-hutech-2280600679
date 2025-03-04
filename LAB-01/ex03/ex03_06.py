def xoaphantu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = 'b'
result = xoaphantu(mydict, key_to_delete)
if result:
    print("Phan tu dax xoa: ", mydict)
else:
    print("Khong tim thay phan tu can xoa")