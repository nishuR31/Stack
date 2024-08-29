from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

class Stack:
    def __init__(self):
        self.stk = []
        self.top = -1

    def display(self):
        if self.top == -1:
            print(Fore.RED + f"\nStack is empty, no data to show")
        else:
            print()
            for i in range(len(self.stk) - 1, -1, -1):
                print(Fore.CYAN + Back.BLACK + f"{self.stk[i]}")

    def push(self):
        while True:
            try:
                data = int(input(Fore.YELLOW + f"\nEnter or push data=> "))
                self.stk.append(data)
                self.top += 1
                print(Fore.GREEN + f"\nData inserted successfully")
                break
            except ValueError:
                print(Fore.RED + f"\nInvalid input, please enter an integer.")
                retry = input(Fore.MAGENTA + f"\nDo you want to try again? [y]: ").strip().lower()
                if retry != 'y':
                    break

    def pop(self):
        if self.top != -1:
            rem = self.stk.pop()
            print(Fore.GREEN + f"\n{rem} removed successfully")
            self.top -= 1
            return rem
        else:
            print(Fore.RED + f"\nUnderflow: cant\' remove from emptry stack")

    def peek(self):
        if self.top != -1:
            print(Fore.BLUE + f"\nTop most element: {self.stk[-1]}")
            return self.stk[-1]
        else:
            print(Fore.RED + f"\nNo elements in stack")

    def empty(self):
        if self.top == -1:
            print(Fore.RED + f"\nStack is empty")
        else:
            print(Fore.GREEN + f"\nStack is not empty ,top most element is {self.peek()}")

stk = Stack()

while True:
    try:
        ask = int(input(Fore.YELLOW + f"\n1: Push\n2: Pop\n3: Peek\n4: Display\n5: Empty?\n6: Exit\n=> "))
        if ask == 1:
            stk.push()
        elif ask == 2:
            stk.pop()
        elif ask == 3:
            stk.peek()
        elif ask == 4:
            stk.display()
        elif ask == 5:
            stk.empty()
        elif ask == 6:
            break
        else:
            print(Fore.RED + f"\nInvalid choice, please select a valid option.")
    except ValueError:
        print(Fore.RED + f"\nInvalid input, please enter a number.")
