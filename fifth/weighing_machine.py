class Balance:
    def __init__(self):
        self.left_weight = 0
        self.right_weight = 0

    def add_right(self, weight):
        self.right_weight += weight

    def add_left(self, weight):
        self.left_weight += weight

    def result(self):
        if self.right_weight > self.left_weight:
            return "R"
        elif self.left_weight > self.right_weight:
            return "L"
        else:
            return "="


balance = Balance()

while True:
    action = input('[R]ight or [L]eft or [P]rint or [C]lose: ').upper()
    if action not in 'RLPC' or len(action) != 1:
        print("error")
    elif action == "P":
        print(balance.result())
    elif action == "C":
        break
    else:
        weight = int(input('Print weight: '))
        if action == "R":
            balance.add_right(weight)
        else:
            balance.add_left(weight)
