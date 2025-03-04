so_gio_lam = float(input("Nhập số giờ làm moi tuan: "))
luong_gio = float(input("Nhập thu lao tren moi gio lam tieu chuan: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = so_gio_lam * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print("Lương thực lĩnh là:", thuc_linh)