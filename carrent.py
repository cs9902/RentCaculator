total = 327800
rate = 0.50757/100
count = 36

print('total:', total)
print('rate:', rate)
print('count:', count)

money = total * rate * (1 + rate)**count / ((1 + rate)**count - 1)

print money
print money * count - total



