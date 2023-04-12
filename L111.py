#Krista and Sarah
dict_1 ={"Smith":"John","Johnson":"Sarah"}

def my_get_method(dict, key, default):
    if key in dict_1 :
        return dict_1[key]
    else:
        return default

print(my_get_method(dict_1,"smith",0))
