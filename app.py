""" x = 3
y = float(3)
print(x, y) """

""" values = [1, 2, 5, 7, 8, 24]
print(values)
for i in values:
    print(i) """

""" x = "mark f"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" right_number = input("what number is it ")
if right_number == "19":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """

""" number = int(input("even or odd "))
if (number % 2) == (0):
    print("even")
if (number % 2) == (1):
    print("odd")
 """

tip = input("how was your excperience? ")
bill = float(input("what is your total?"))
if tip == "bad":
    print("your total is", bill)
elif tip == "ok":
    print("your total is", round(bill * 1.15, 2))
elif tip == "good":
    print("your total is", round(bill * 1.20, 2))
elif tip == "great":
    print("your total is", round(bill * 1.25, 2))