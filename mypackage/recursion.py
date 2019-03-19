 def sum_array(array):
    array_sum = 0
    for i in array:
        array_sum +=i
    return array_sum


def fibonacci(number):
    if number <= 1:
        return 1
    return fibonacci(number - 2) + fibonacci(number - 1)


def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

def reverse(word):
    words = word.split(" ")
    new_words = [word[::-1] for word in words]
    new_sentence = " ".join(new_words)

    return new_sentence
