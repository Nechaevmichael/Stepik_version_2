# Программа, считывает натуральное число n, после чего выводит двойное неравенство этого числа с его соседними числами.
#
# Смотрите примеры ниже
#
# Sample Input 1:
#
# 15
# Sample Output 1:
#
# 14<15<16

n = int(input())
print(n - 1, n, n + 1, sep='<')