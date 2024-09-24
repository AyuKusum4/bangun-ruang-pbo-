# Pemrograman Berorientasai Objek

# 3D Tabung
phi = 3.14
r = int(input("Masukkan jari-jari : "))
t = 20
volume_tabung = phi * (r**2) * t
luas_permukaan = 2 * phi * r * (r + t)
print(f"Volume tabung: {volume_tabung} ")
print(f"Luas permukaan tabung: {luas_permukaan} ")

# 3D Kerucut
phi = 3.14
r = int(input("Masukkan jari-jari : "))
t = 36
s = 12
volume_kerucut = 1 / 3 * phi * (r**2) * t
luas_permukaan = phi * r * (r + s)
print(f"Volume kerucut: {volume_kerucut} ")
print(f"Luas permukaan kerucut: {luas_permukaan} ")