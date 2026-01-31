"""
#
# Functions
# 
"""
def myfullname(firstname="Unknown", lastname="forger"):
    return firstname + " " + lastname

print(myfullname("cat", "dog"))
print(myfullname(firstname="lion"))
print(myfullname())
print(myfullname(lastname="wolf"))
print(myfullname("fox","bear"))
print(myfullname("eagle","hawk"))
print(myfullname("shark","whale"))

def redpotion(hp):
    return hp + 50
def bluepotion(mp):
    return mp + 30

current_hp = 70
print("Current HP:", current_hp)
current_hp = redpotion(current_hp)
print("After using Red Potion, HP:", current_hp)