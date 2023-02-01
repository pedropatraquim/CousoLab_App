# attributes.py

# Define global variables for attributes
Attributes = {
    "Strength": 0,
    "Intelligence": 0,
    "Charisma": 5,
    "Followers": 0,
    "Disciples": 0
}

def update_attributes(str, intel, cha):
    global strength, intelligence, charisma
    strength += str
    intelligence += intel
    charisma += cha

def update_followers(num):
    global followers
    followers += num

#Faith = 10
#Wisdom = 10
#Charisma= 10
#Wealth= 10
#Health= 10
#Power= 10
#Influence= 10
#Reputation= 10
#Knowledge= 10
#Devotion= 10
