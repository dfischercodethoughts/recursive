## definition of recursive: uses itself in its definition
## eg, fibonacci: fib(a) = fib(a-1) + fib(a-2)
## fibonacci(0) = 0
## 0, 1, 1, 2

def fun_function(a, b):
    return a + b

state = {}

def fibonacci(a):
    # base case: fib(0) = 0
    # blocking pattern
    if a == 0:
        return 0
    if a == 1:
        return 1
    # these are "recursive calls"

    if a in state:
        return state[a]

    res = fibonacci(a-1) + fibonacci(a-2)
    state[a] = res
    print(res)
    return res

def main():
    print(fun_function(1, 2))
    ## what happens??
    ## THIS WILL CRASH YOUR PROCESS unless we add a base case to fibonacci
    ## very slow still
    print(fibonacci(7, {}))
    ## how do we improve?
    # option1 : memoization

## execution magic -> python has a magic constant called __name__, where __name__ is a string containing "__main__" if I call the file directly
## as opposed to creating new libraries, where you can 'import' a python file, which executes everything inside that file. 
if __name__ == "__main__":
    main()
