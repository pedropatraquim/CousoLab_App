# attributes.py

# Define global variables for attributes
#attributes = {
#    "Strength": 5,
#    "Intelligence": 5,
#    "Charisma": 5,
#    "Followers": 10,
#    "Disciples": 0
#}

## Define global variable for followers
#followers = 100

def update_attributes(str, intel, cha):
    global strength, intelligence, charisma
    strength += str
    intelligence += intel
    charisma += cha

def update_followers(num):
    global followers
    followers += num
