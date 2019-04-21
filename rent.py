total = 95000
rate = 6.75/100/12
count = 60

print('total:', total)
print('rate:', rate)
print('count:', count)

money = total * rate * (1 + rate)**count / ((1 + rate)**count - 1)

print (money)