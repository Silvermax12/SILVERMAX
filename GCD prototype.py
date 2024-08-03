print("Silvermax Welcomes You")
#Program to find the GCD using Euclid's algorithm
def GCD(a, b):
    while b != 0:
        print(f"{a} = {a//b}*{b} + {a%b}")
        a, b = b, a % b
    return a
#so this part of the program is to get the user input and find the GCD
def max():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    # so this is the start of the GCD finding process
    print(f"\nSteps to find the GCD of {a} and {b} using Euclid's algorithm:")
    gcd = GCD(a, b)
    print(f"The GCD of {a} and {b} is {gcd}.")
    print("This simple thing u can't do")
    print("Hope u learnt something")

max()
print("All Hail Silvermax")