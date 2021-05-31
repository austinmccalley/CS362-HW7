def fizzBuzz(i):
    i = int(i)
    if i % 3 == 0:
        return ('Fizz')


if __name__ == "__main__":
  for i in range(1, 101):
    s = fizzBuzz(i)
    print(s)