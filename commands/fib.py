from functools import cache, lru_cache

fabnumber = input("Enter the number of Fibonacci numbers you want: ")

color = {
    "purple" : '\033[95m',
    "cyan" : '\033[96m',
    "darkcyan" : '\033[36m',
    "blue" : '\033[94m',
    "green" : '\033[92m',
    "yellow" : '\033[93m',
    "red" : '\033[91m',
    "end" : '\033[0m',
}

style = {
    "bold" : '\033[1m',
    "underline" : '\033[4m' ,
    "end" : '\033[0m'
} 

@lru_cache(maxsize = 5)
def fib(n):
   if n <= 1:
       return (n)
   else:
       return (fib(n-1) + fib(n-2))

for i in range(int(fabnumber) + 1):
    print(color["green"] + f'{i} ' + color["end"] + '- ' + style["bold"] + f'{fib(i)}' + style["end"])

# def fibSeq(n):
#     x, y = 0, 1
#     z = 0

#     if n <= 0:
#         print("You have no brain, do you?")

#     else:
#         for i in range(n):
#             z = y
#             y = x
#             x = z + y
#             print(x)


# if __name__ == "__main__":
#     n = int(input("Input 'n': "))
#     fibSeq(n)


# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# def main():
#     for i in range(400):
#         print(i , fib(i))
#     print("Done")

# if __name__ == "__main__":
#     main()

