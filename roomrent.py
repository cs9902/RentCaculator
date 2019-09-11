total = 878093.18
rate = 4.655/100/12
count = 240 - 58

print('total:', total)
print('rate:', rate)
print('count:', count)

money = total * rate * (1 + rate)**count / ((1 + rate)**count - 1)

print (money)


def returnrent(amount):
    newTotal = total - amount
    print('new total: ', newTotal)
    newmoney = newTotal * rate * (1 + rate)**count / ((1 + rate)**count - 1)
    print('new money: ', newmoney)
    print('new money monthly: ', newmoney - 2250)
    print('new money yearly: ', (newmoney - 2250) * 12)
    

returnrent(450000)

