def get_last_name(full_name:str):
    if full_name != None and full_name != "":
        splited_name = full_name.split(" ")
        return splited_name[len(splited_name) - 1]


print(get_last_name("Elvis Presley"))