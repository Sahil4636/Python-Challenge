import sys

def function1():
    print("First function")

def function2():
    print("Second function")

arguments = sys.argv[1:]

if len(arguments) != 1:
    print(f'ERROR: 1 argument expected, {len(arguments)} provided')
    sys.exit(1)

argument = arguments[0]
if argument == 'f' or argument == 'first':
    function1()
elif argument == 's' or argument == 'second':
    function2()
else:
    print(f'ERROR: Invalid argument {argument}')
    sys.exit(1)



