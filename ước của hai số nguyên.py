def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# sử dụng hàm để tính GCD của hai số
a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
gcd = gcd(a, b)
print("GCD của", a, "và", b, "là:", gcd)
