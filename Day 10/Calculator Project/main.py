import art
def add(n1, n2):
    return n1 + n2
def sub(n1 , n2):
    return n1 - n2
def multiply(n1 , n2):
    return n1 * n2
def division(n1 , n2):
    return n1 / n2
operations = {
    "+": add,
    "-" : sub,
    "*" : multiply,
    "/" : division,
}
def calculator():
    print(art.logo)
    game_play = True
    n1 = int(input("Enter first number: "))
    while game_play:
        for symbol in operations:
            print(symbol)
        op = input("Pick an operation: ")
        n2 = int(input("Enter the second number: "))
        answer = operations[op](n1, n2)
        print(f"{n1} {op} {n2} : {answer}")
        choice = input("Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation : ")
        if choice == "y":
            n1= answer
        else:
            game_play = False
            print("\n" * 20)
            calculator()

calculator()



