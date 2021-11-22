color_list_1 = list(input("Write first group of colors using only comma: ").split(","))
color_list_2 = list(input("Write second group of colors using only comma: ").split(","))

#color_list_1 = set(["White", "Black", "Red"])
#color_list_2 = set(["Red", "Green"])
#for i in list(color_list_2):
#    color_list_1.discard(i)
result_list= []

for i in color_list_1:
    if i not in color_list_2:
        result_list.append(i)
print(result_list)
