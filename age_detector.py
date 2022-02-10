
def ageandyearfinder(x,a):
  return a-x

b = 2022
while(True):
    try:
      y = int(input("enter your age or birth year : "))
    except ValueError:
        print("plz enter a valid number")
        continue
    break

s = ageandyearfinder(y,b)
u = []
u.extend(str(s))  # alg alg print hoga str ho ya int
i = list(u)

if len(i) == 4 :
    print(f"your birth year is {s}")
else:
    print(f"your age is {s}")