#Krista and Sarah
red_velvet={
    "oil":2,
    "flour":"2.5",
    "sugar":"1.5",
    "baking_soda":"1",
    "eggs":"2",
    "red_color":"2"
}

lemon_cake={
    "flour":"2.5",
    "sugar":"1",
    "baking_soda":"1.5",
    "eggs":"2",
    "lemon_zest":"1",
    "oil":2
}

def cake_recipes(cake_1, cake_2):
    matches = []
    for x in cake_1:
        for y in cake_2:
            if cake_1[x] == cake_2[y]:
                matches.append(x)
            else:
                return None
    return matches
a = cake_recipes(red_velvet, lemon_cake)
print(a)
