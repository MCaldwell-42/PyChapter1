def run_kid(name):
    print(f"{name} ran.")

def swing_kid(name):
    print(f"{name} swung.")

def slide_kid(name):
    print(f"{name} slid.")

def hide_kid(name):
    print(f"{name} hid AND seeked.")

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

# for kids in running_kids:
#     run_kid(kids)
    
# for kids in swinging_kids:
#     swing_kid(kids)

# for kids in sliding_kids:
#     slide_kid(kids)

# for kids in hiding_kids:
#     hide_kid(kids)

for i in range(101):
    if i % 5 == 0 and i % 7 == 0:
        print("ChickenMonkey")
    elif i % 5 == 0: 
        print("Chicken")
    elif i % 7 == 0:
        print("Monkey")
    else:
        print(i)

# for i in range(1,100):
#     output = ""
#     if (i % 5 == 0):
#         output = f'{output}Chicken'
#     if (i % 7 == 0):
#         output = f'{output}Monkey'
    
#     print(output if output != "" else i)