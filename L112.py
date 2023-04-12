#Krista and Sarah
name_dict = {
    "Hoffman": "Rosemary",
    "Anspach": "Grace",
    "O'roark": "Katherine",
    "Gallaway": "Gabrielle",
    "Berlag": "Bethany",
    "Bong": "Saerin",
    "Busk": "Olivia",
    "Eafon": "Breanna",
    "Nixon": "Emily",
    "Paradiso": "Vincenza",
    "Stephenson": "Sarah",
    " Dockery": "Krista"
}

freq_dict = {}

for first_name in name_dict.values():
    if first_name in freq_dict:
        freq_dict[first_name] += 1
    else:
        freq_dict[first_name] = 1

print(freq_dict)
