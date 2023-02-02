_list = ["revolver", "sports car", "gold fish", "celular telephone", "laptop"]

filename="raw.txt"

with open(filename) as f:
    classes = f.readlines()

classes = [i[:-1] for i in classes] 

print(classes)

with open("imagenet_classes.txt", "w") as f:
    for i in classes:
        if i in _list:
            f.write(i + "\n")
        else:
            f.write("N/A\n")