def convert_to_binary(array):
    binary_array = []
    for elem in array:
        if elem < 0:
            binary_array.append(bin(elem)[0] + bin(elem)[3:])
        else:
            binary_array.append(bin(elem)[2:])
    return binary_array

try:
    print("Введите массив десятичных чисел")
    decimal_array = list(map(int, input().split()))
    print("Массив двоичных чисел:")
    print(*convert_to_binary(decimal_array))
except:
    print("Вводите только числа!!!!")
