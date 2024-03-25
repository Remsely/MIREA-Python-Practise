import timeit

import matplotlib.pyplot as plt
from Levenshtein import distance


def ex1(n, m, a):
    result = 1
    for c in range(1, a + 1):
        for j in range(1, m + 1):
            summ = 0
            for i in range(1, n + 1):
                summ += (28 * c ** 2) ** 6 / 5 + 16 * (
                        j ** 3 / 44 + i ** 2) ** 5
            result *= summ
    return result


def ex2(y, z):
    summ = 0
    for i in range(len(y)):
        summ += (y[i] - z[i]) ** 2
    return summ ** 0.5


def ex3(y, z):
    summ = 0
    for i in range(len(y)):
        summ += abs(y[i] - z[i])
    return summ


def ex4(y, z):
    _max = 0
    for i in range(len(y)):
        cur = abs(y[i] - z[i])
        if cur > _max:
            _max = cur
    return _max


def ex5(y, z):
    summ = 0
    for i in range(len(y)):
        summ += (y[i] - z[i]) ** 2
    return summ


def ex6(y, z, h=5):
    summ = 0
    for i in range(len(y)):
        summ += abs(y[i] - z[i]) ** h
    return summ ** (1 / h)


def visualize(distance_metrics, y, z, move=1):
    moved_z = [i + move for i in z]
    distance_differences = []
    for distance in distance_metrics:
        distance_before_move = distance(y, z)
        distance_after_move = distance(y, moved_z)
        distance_difference = distance_after_move - distance_before_move
        distance_differences.append(distance_difference)
    x = range(0, len(distance_differences))
    figure, axis = plt.subplots()

    axis.bar(x, distance_differences)
    axis.set_xticks(x, labels=[f'd_{i + 1}' for i in x])
    plt.show()


def ex8(words):
    if not words:
        return ''
    result = ''
    for i in range(len(words) - 1, -1, -1):
        result += words[i] + ' '
    return result.rstrip()


def ex9(string):
    string = string.lower()
    char_count = {}
    for char in string:
        if char == ' ':
            continue
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


def ex10(a, b, i, j):
    if i == 0 or j == 0:
        return max(i, j)
    if a[i - 1] == b[j - 1]:
        return ex10(a, b, i - 1, j - 1)
    return 1 + min(ex10(a, b, i, j - 1), ex10(a, b, i - 1, j),
                   ex10(a, b, i - 1, j - 1))


metrics = [ex2, ex3, ex4, ex5, ex6]

print(f'1) {ex1(4, 2, 8)}')
print(f'2) {ex2([1, 0.5, 1], [0.5, 2, 1])}')
print(f'3) {ex3([1, 0.5, 1], [0.5, 2, 1])}')
print(f'4) {ex4([1, 0.5, 1], [0.5, 2, 1])}')
print(f'5) {ex5([1, 0.5, 1], [0.5, 2, 1])}')
print(f'6) {ex6([1, 0.5, 1], [0.5, 2, 1])}')
print(f'8) {ex8(["language!", "programming", "Python", "the", "love", "I"])}')
print(f'9) {ex9("I love the Python programming language!")}')
print(f'10) {ex10("Hello, world!", "Goodbye, world!", 12, 14)}')
print(f'10) {ex10("Hello, world!", "Bye, world!", 12, 10)}')
print(f'10) {ex10("I love Python!", "I like Python!", 13, 13)}')
print(f'10) {ex10("100101", "100011", 6, 6)}')
visualize(metrics, [1, 0.5, 1], [0.5, 2, 1])
print(
    f'11) {timeit.timeit(lambda: ex10(
        "Hello, world!",
        "Goodbye, world!",
        12,
        14)
        , number=10000)} - {timeit.timeit(lambda: distance(
        "Hello, world!",
        "Goodbye, world!"), number=10000)}')
