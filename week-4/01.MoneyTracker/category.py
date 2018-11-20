class Catergory:
    def __init__(self, money, name):
        self.money = money
        self.name = name

    def get_money(self):
        return self.money

    def get_name(self):
        return self.name


class Income(Catergory):
    def __init__(self, name, money, income):
        super().__init__(name, money)
        self.income = income

    def get_income(self):
        return self.income


class Expense(Catergory):
    def __init__(self, name, money, expense):
        super.__init__(name, money)
        self.expense = expense

    def get_expense(self):
        return self.expense
