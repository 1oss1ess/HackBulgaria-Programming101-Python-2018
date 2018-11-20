class Bill:

    def __init__(self, amount):
        self.amount = amount
        self.data = []
        # self.data.append(amount)

    def __int__(self):
        return self.amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return '"A {}$ bill"'.format(self.amount)

    def __eq__(self, other):
        return self.amount == other

    def __hash__(self):
        return hash(self.amount)

    def __getitem__(self, index):
        return self.data[index]


class BillBatch:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def total(self):
        result = 0
        for x in self.data:
            for i in x:
                if type(i) is Bill:
                    result += int(i)
        return result

    def __getitem__(self, index):
        return self.data[index]


class CashDesk(BillBatch, Bill):

    def __init__(self):
        self.money = self
        self.data = []

    def take_money(self, money):
        return self.data.append(money)

    def total(self):
        result = 0
        for x in self.data:
            if type(x) is Bill:
                result += int(x)
            for i in x:
                if type(i) is Bill:
                    result += int(i)
        return result

    def inspect(self):
        arr = []
        for item in self.data:
            if type(item) is Bill:
                arr.append(int(item))
            for index in item:
                if type(index) is Bill:
                    arr.append(int(index))
        arr.sort()
        my_dic = dict((i, arr.count(i)) for i in arr)
        for key, value in my_dic.items():
            print(str(key) + '$ bills -', value)
