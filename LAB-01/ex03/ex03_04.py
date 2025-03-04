def truycapphantu(tupledata):
    firstelement = tupledata[0]
    lastelement = tupledata[-1]
    return firstelement, lastelement

inputtuple = eval(input("Nhap tuple : "))
first, last = truycapphantu(inputtuple)
print("Phan tu dau tien cua tuple la: ", first)
print("Phan tu cuoi cung cua tuple la: ", last)
