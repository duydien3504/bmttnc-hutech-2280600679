print("Nhap cac dong van ban(Nhap 'done' de ket thuc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\nIn hoa cac dong van ban:")
for line in lines:
    print(line.upper())