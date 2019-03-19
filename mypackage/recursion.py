def sum_array(array):
    array_sum = 0
    for i in array:
        array_sum +=i
    return array_sum


def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 2) + fibonacci(number - 1)


def factorial(n):
    if n == 1 | n ==0:
        return 1
    else:
        return n*factorial(n-1)

def reverse(word):
    new_sentence = word[::-1]
    return new_sentence
print(reverse("reverse this"))