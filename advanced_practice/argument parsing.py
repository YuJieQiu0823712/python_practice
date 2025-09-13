def myfunction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])
myfunction('hey', True, 19, 'WOW', KEYONE='TEST', KEYTWO=7)



import sys
# Usage: main.py FILENAME MESSAGE
filename = sys.argv[1]
message = sys.argv[2] 
with open(filename, 'w+') as f:
    f.write(message)
# python "argument parsing.py" test.txt "Hello World"



import getopt
filename = "test.txt" # default values
message = "Hello" # default values
opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])
print(opts)
print(args)
# python "argument parsing.py" test.txt "Hello World" => args
# python "argument parsing.py" -f test.txt -m "Hello World" => opts
#   [('-f', 'test.txt'), ('-m', 'Hello World')]
#   []

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg
with open(filename, "w+") as f:
    f.write(message)
# python "argument parsing.py" -f test.txt -m "Hello World" => Hello World
# python "argument parsing.py" => Hello

