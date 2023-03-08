#Source: Cột đặt
#Destination: Cột mục tiêu
#auxiliary: Cột trung gian
def TowerofHanoi(n, source, destination, auxiliary):
    if n==1:
        print("Chuyển đĩa 1 từ cọc",source,"sang cọc",destination)
        return
    TowerofHanoi(n-1,source,auxiliary,destination)
    print("Chuyển đĩa",n,"từ cọc",source,"sang cọc",destination)
    TowerofHanoi(n-1,auxiliary,destination,source)

n =int(input("Nhập vào: "))
A= input("Nhập vào cột đặt: ")
B= input("Nhập vào cột mục tiêu: ")
C= input("Nhập vào cột trung gian: ")
TowerofHanoi(n,A,B,C)