def fizzBuzz(i):
    i = int(i)
    if i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz'
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'


if __name__ == "__main__":
    for i in range(1, 101):
        s = fizzBuzz(i)
        print(s)
