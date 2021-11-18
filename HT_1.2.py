color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
for i in list(color_list_2):
    color_list_1.discard(i)
print(color_list_1)