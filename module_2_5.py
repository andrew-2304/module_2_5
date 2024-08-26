
# def say_hello(name):  # Принимающая ф-я
#     print('Hello', name)
#
#
# say_hello('Andrey')
# say_hello('Sergey')


# import random  #Возвращающая ф-я
# def lottery():
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win = random.choice(tickets)
#     return win
# win = lottery()
# print(win)




# def lottery(*args, **kwargs): #Принимающая (не работает)
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     tickets.remove(win1)
#     win2 = random.choice(tickets)
#     print(*args)
#     return win1, win2
#
#
# win1, win2 = lottery(*args:1,2,3)
# print(win1, win2)


# def test(a=2, b=True):
#     print(a,b)
# test()

# def test(a=2, b=True):
#     print(a,b)
# test(False, 'ok')

# def test(a=2, b=True):
#     print(a,b)
# test(*[1,3])


def get_matrix(n,m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
result1 = get_matrix(2,2,10)
result2 = get_matrix(3,5,42)
result3 = get_matrix(4,2,13)