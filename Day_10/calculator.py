from traceback import print_tb


def add(first_num,second_num):
    return first_num + second_num

def minus(first_num,second_num):
    return first_num - second_num

def multiple(first_num,second_num):
    return first_num * second_num

def divide(first_num,second_num):
    return first_num / second_num

operations = {
    "+" : add,
    "-" : minus,
    "*" : multiple,
    "/" : divide
}
def calculator():
    first_num = float(input("What is the firs number"))
    while True:
        print("+\n-\n*\n/")
        op = input("What is the operator")
        second_num = float(input("What is the second number"))
        result = operations[op](first_num,second_num)
        print(f" {first_num} {op} {second_num} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result},or type 'n' to start new calculation,or type 'o' to out")

        if choice == "y":
            first_num = result
        elif choice == "n":
            print("\n"*20)
            calculator()
        else:
            break

calculator()




