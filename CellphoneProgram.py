import CellphoneClass as cp

def main():
    m = input("Enter the manufacturer of the phone: ")
    n = input("Enter the model of the phone: ")
    p = float(input("Enter the price of the phone: "))

    phone = cp.Phone(m,n,p)

    print(phone)

main()