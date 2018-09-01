def function1(x):
    if len(x) != 0:
        x_max = max(x)
        x_min = min(x)
        x_len = len(x)
        x_mean = sum(x) / x_len
        return (x_max, x_min, x_len, x_mean)
    else:
        print('Ups! Lista vacía.')
        return None

    
def function2(x, y):
    if len(x) == len(y):
        n = len(x)
        aux_list = []
        for i in range(n):
            aux_list.append(abs(x[i] - y[-i]))
        return aux_list
    else:
        print('Las listas no son del mismo largo!')
        return None


def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)