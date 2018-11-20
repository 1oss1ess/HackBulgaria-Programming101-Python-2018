from cashdesk import Bill, BillBatch, CashDesk

a = Bill(10)
b = Bill(5)
c = Bill(10)

int(a)  # 10
str(a)  # "A 10$ bill"
print(a)  # A 10$ bill

a == b  # False
a == c  # True

money_holder = {}

money_holder[a] = 1  # We have one 10% bill

if c in money_holder:
    money_holder[c] += 1

print(money_holder)  # { "A 10$ bill": 2 }

print("===")

values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

for bill in batch:
    print(bill)

print("===")

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total())  # 390
desk.inspect()
