name = "Ann"
age = 15
pi =322222.14
print(f"Hello {name:15}")
print(f"Your age is {age:15}")
print(f"Your age is {age:15d}")
print(f"Hello {name:15s}")
print(f"pi: {pi:10.4f}")

print("Today is friday, {day:10d}.".format(day=13))

day = 0.11
print("Today is friday, {:10.2f}.".format(day))

print("Hello \nWorld")

print("Hello Wor\bld")

print("Hello Wor\rld")

print("Hello Wo\trld")

details_damage_price = {"energy gun": 100, 
                        "minigun": 70, 
                        "Thor hammer": 50, 
                        "laser gun": 80,
                        "rail gun": 90, 
                        "sniper rifle": 150}

details_survive_price = {"shield": 50, 
                         "energyshield": 80, 
                         "resist": 30, 
                         "evasion": 100,
                         "armor": 140}

users_bot = {}
users_list = ["Krim","Revi"]

def create_users(users):
   check = False
   while not check:
    name = input("Please input name users")
    if len(name)>3:
      users.append(name)
      print("Success")
      check = True
    else:
      print(f"Error. Please input name again")
    
create_users(users_list)

