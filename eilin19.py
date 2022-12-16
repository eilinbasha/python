def new_string(str):
    if len(str)>2 and str[:2] == "is":
       return str
    return "is" + str

print(new_string("eilin"))
        