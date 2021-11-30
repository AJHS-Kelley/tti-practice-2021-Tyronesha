# Try / Except, 11/30/21

y = 25
my_name = "Tyronesha Alexander"

try:
    print(x)
except:
    print("Oh no, something is burning!\n")

try:
    print(z)
except NameError:
    print("That variable is not defined, let's define it.\n")
    z=25
except:
    print("Oh no, something is burning!\n")
finally:
    print("The try/catch is finished.")
print(z)
