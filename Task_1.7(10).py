# В этой задаче мы сами будем решать, какое значение использовать в качестве разделителя в параметре sep
#
# Программа принимает на вход строку - разделитель, вам необходимо распечатать числа от 1 до 5, выводя между ними введенный разделитель
#
# Sample Input 1:
#
# !
# Sample Output 1:
#
# 1!2!3!4!5

separator = input()
result = ''
for i in range(1, 6):
    if i == 5:
        result = result + str(i)
    else:
        result = result + str(i) + str(separator)
print(result)

# a, b, c, d, e = 1, 2, 3, 4, 5
# print(a, b, c, d, e, sep=separator)