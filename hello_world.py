print("hello world")

print("Fibonacci sequence")

a, b = 0, 1
c, d = 0, 1

print("method 1")
while a < 10:
    print(a)

    a, b = b, a+b

print("method 2")

while c < 10:
    print(c)
    temp = d
    
    d = c+d
    c = temp


print("method 3")
sequence = [0, 1]

while len(sequence) < 10:
    sequence = sequence + [sequence[-1] + sequence[-2]]

print(sequence)


print("fizz buzz bust")
for trigger in range(25):
    if trigger % 5 ==0  and trigger % 3 == 0:
        print("fizzbuzz ... ", "trigger: ", trigger)
    elif trigger % 3 == 0:
        print("fizz ... ", "trigger: ", trigger)
    elif trigger % 5 == 0:
        print("buzz ... ", "trigger: ", trigger)
    else:
        # print("bust ... ", "trigger: ", trigger)
        pass


print("fizz buzz")
def fizzBuzz(n: int): #-> List[str]:
    output = []
    if n % 5 == 0 and n % 3 == 0:
        output = output + ["FizzBuzz"]
    elif n % 3 == 0 :
        output = output + ["Fizz"]
    elif n % 5 == 0:
        output = output + ["Buzz"]
    else:
        output.append(n)
    
    return output

out = []
for r in range(1,26):
    out = out + fizzBuzz( r)

print(out)


