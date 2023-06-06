# Дано целое положительное число, ваша задача вывести разряд сотен этого числа
#
# Sample Input 1:
#
# 123
# Sample Output 1:
#
# 1

number = int(input())
print(number // 100 % 10)