total = 920221.02
rate = 4.655/100/12
count = 240 - 45

print('total:', total)
print('rate:', rate)
print('count:', count)

money = total * rate * (1 + rate)**count / ((1 + rate)**count - 1)

print (money - 1900)


def returnrent(amount):
    newTotal = total - amount
    print('new total: ', newTotal)
    newmoney = newTotal * rate * (1 + rate)**count / ((1 + rate)**count - 1)
    print('new money: ', newmoney)
    print('new money monthly: ', newmoney - 1900)

returnrent(250000)

