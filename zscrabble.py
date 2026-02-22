import random

words= ["animal", "bottle", "pillow", "ladder", "hammer", "pencil", "eraser", "marker", "poster", "folder",
"ruler", "locker", "engine", "button", "camera", "school", "friend", "parent", "sister", "brother",
"cousin", "uncle", "auntie", "grandma", "grandpa", "window", "mirror", "carpet", "closet", "bucket",
"blanket", "planet", "rocket", "sunset", "forest", "canyon", "island", "castle", "garden", "border",
"circle", "square", "letter", "doctor", "farmer", "painter", "driver", "player", "singer", "dancer",
"artist", "pilot", "baker", "hunter", "reader", "writer", "police", "sailor", "actor", "person",
"kitchen", "bedroom", "garage", "office", "market", "cinema", "museum", "hallway", "station", "prison",
"street", "alley", "desert", "jungle", "valley", "river", "ocean", "bridge", "tunnel", "candle",
"ticket", "wallet", "tablet", "laptop", "screen", "corner", "jacket", "sweater", "slipper", "planet",
"rocket", "forest", "canyon", "castle", "garden", "rabbit", "monkey", "tiger", "zebra", "parrot",
"donkey", "flower", "orange", "banana", "butter", "cheese", "tomato", "potato", "pepper", "onion",
"lettuce", "carrot", "muffin", "cookie", "pizza", "burger", "salad", "noodle", "cereal", "ketchup",
"honey", "donut", "basket", "tissue", "helmet", "gloves", "charger", "magnet", "pirate", "dragon",
"ninja", "monster", "puppet", "rocket", "animal", "window", "poster", "sticker", "ticket", "napkin",
"breeze", "desert", "castle", "market", "camera", "tunnel", "valley", "planet", "castle", "rabbit",
"wallet", "planet", "magnet", "dragon", "jungle", "castle", "closet", "tablet", "market", "rocket",
"museum", "pirate", "button", "hunter", "forest", "person", "cookie", "donkey", "bridge", "school",
"castle", "rocket", "camera", "mirror", "castle", "planet", "jungle", "banana", "rocket", "bridge",
"planet", "pillow", "valley", "border", "closet", "bucket", "school", "castle", "dragon", "rocket",
"animal", "basket", "bottle", "camera", "circle", "dinner", "doctor", "driver", "family", "finger",
"friend", "guitar", "hammer", "handle", "jacket", "jungle", "ladder", "letter", "market", "mirror",
"mother", "napkin", "notebook", "office", "orange", "packet", "pillow", "planet", "pocket", "rabbit",
"remote", "rocket", "school", "season", "shadow", "shovel", "silver", "sister", "soccer", "speech",
"spider", "spouse", "street", "sugar", "summer", "ticket", "tissue", "tomato", "tooth", "trophy",
"trucks", "tunnel", "vacuum", "valley", "wallet", "window", "winner", "winter", "writer", "zebra",
"artist", "breeze", "bridge", "bubble", "button", "carrot", "castle", "cattle", "cheese", "circle",
"closet", "coffee", "column", "cookie", "crayon", "danger", "dealer", "drawer", "driver", "editor",
"energy", "engine", "escape", "farmer", "father", "fever", "flower", "forest", "garage", "garlic",
"gloves", "grapes", "guitar", "hockey", "honest", "hunter", "icebox", "injury", "island", "jungle",
"kettle", "kitten", "ladder", "lawyer", "leader", "lesson", "liquid", "magnet", "marble", "marker",
"market", "minute", "mirror", "monkey", "mother", "museum", "napkin", "nation", "needle", "object",
"office", "orange", "oxygen", "pencil", "people", "pepper", "planet", "player", "pocket", "police",
"potato", "prince", "prison", "rabbit", "ranger", "record", "remote", "repair", "rescue", "ribbon",
"rocket", "safety", "salmon", "school", "screen", "season", "shower", "silver", "singer", "sister",
"socket", "speech", "sphere", "spider", "spouse", "square", "stitch", "stomach", "stool", "street",
"summer", "tablet", "target", "temple", "ticket", "tomato", "tongue", "tooth", "trophy", "tunnel",
"turtle", "vacuum", "valley", "vessel", "viking", "violin", "walnut", "wallet", "window", "winter",
"wizard", "writer", "yellow", "zebra", "airbag", "anchor", "answer", "backup", "badge", "ballot",
"banana", "barber", "beacon", "beetle", "belief", "bishop", "bottle", "border", "branch", "bucket",
"button", "cactus", "camera", "candle", "carpet", "cattle", "charge", "circle", "clergy", "closet",
"cobweb", "coffin", "comedy", "cookie", "cotton", "couple", "crater", "credit", "curtain", "dagger",
"dealer", "dental", "desert", "doctor", "donkey", "drawer", "editor", "effort", "engine", "eyelid",
"fabric", "famine", "finger", "finish", "flavor", "flower", "folder", "forest", "fortune", "funnel",
"garage", "garlic", "goblet", "gossip", "guitar", "hammer", "hazard", "helmet", "hockey", "honest",
"honor", "impact", "income", "injury", "insect", "island", "jacket", "jungle", "kettle", "ladder",
"lawyer", "leader", "lemon", "lesson", "liquid", "magnet", "marble", "marker", "method", "minute",
"mirror", "monkey", "mother", "napkin", "nation", "needle", "notion", "object", "orange", "outfit",
"oxygen", "packet", "palace", "parrot", "pastor", "pepper", "pickle", "planet", "player", "plenty",
"pocket", "police", "potato", "prince", "prison", "puzzle", "rabbit", "ranger", "remote", "repair",
"rescue", "reward", "ribbon", "rocket", "saddle", "safety", "salmon", "school", "screen", "season",
"shadow", "shovel", "silver", "singer", "socket", "speech", "sphere", "spider", "spouse", "spring",
"square", "stomach", "stool", "street", "studio", "summer", "tablet", "target", "temple", "ticket",
"tomato", "tongue", "tooth", "trains", "trophy", "tunnel", "turtle", "vacuum", "valley", "vessel",
"violin", "wallet", "window", "winter", "wizard", "writer", "yellow", "zebra"]
#print(len(words))

def scramble():
    d = []
    letters=[]
    new_word=""

    i = random.randint(0,537)
    word = words[i].upper()
    #print(word)
    for letter in word:
        letters.append(letter)
    random.shuffle(letters)
    for new_letters in letters:
        new_word = new_word + new_letters
    d = [word,new_word]
    return d

#word= scramble()
#print("Word:",word[0])
#print("Scrambelled word:",word[1])
