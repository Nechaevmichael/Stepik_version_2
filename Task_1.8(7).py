# Дано целое положительное трехзначное число, ваша задача найти сумму разрядов этого числа
#
# Sample Input 1:
#
# 123
# Sample Output 1:
#
# 6

number = int(input())
result = 0
for i in range(3):
    temp = number % 10
    result += temp
    number //= 10
print(result)