num_users = int(input("Nhập vào số lượng người chia thưởng: "))
bonus_amount = int(input("Nhập vào số tiền muốn chia: "))

if num_users > 0:
    bonus_per_user = bonus_amount / num_users
    print(f"Each user will receive {bonus_per_user} bonus")
else:
    print("Invalid number of users")
