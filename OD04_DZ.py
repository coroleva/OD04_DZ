# Алгоритм с линейной временной сложностью

def sum_of_list_elements(arr):
    total_sum = 0
    for element in arr:
        total_sum += element
    return total_sum

# Пример использования функции
my_list = [1, 2, 3, 4, 5]
result = sum_of_list_elements(my_list)
print("Сумма элементов списка:", result)

# алгоритм  с константной сложностью
def get_first_element(arr):
    if len(arr) == 0:
        return None
    return arr[0]

# Пример использования функции
my_list = [1, 2, 3, 4, 5]
first_element = get_first_element(my_list)
print("Первый элемент списка:", first_element)


# логарифмическая сложность алгоритма
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Пример использования функции
num1 = 48
num2 = 18
greatest_common_divisor = gcd(num1, num2)
print(f"Наибольший общий делитель чисел {num1} и {num2}: {greatest_common_divisor}")
