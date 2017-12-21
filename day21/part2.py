import sys

def rotations(image):
    size = len(image)
    r = []

    r.append(image)

    t = []
    for i in range(size):
        s = ""
        for j in range(size):
            s += image[j][i]
        t.append(s)

    r.append(t)

    t = []
    t2 = []
    for i in range(size):
        s = ""
        s2 = ""
        for j in range(size-1, -1, -1):
            s += image[i][j]
            s2 += image[j][i]
        t.append(s)
        t2.append(s2)

    r.append(t)
    r.append(t2)

    t = []
    t2 = []
    for i in range(size-1, -1, -1):
        s = ""
        s2 = ""
        for j in range(size-1, -1, -1):
            s += image[i][j]
            s2 += image[j][i]
        t.append(s)
        t2.append(s2)

    r.append(t)
    r.append(t2)

    t = []
    t2 = []
    for i in range(size-1, -1, -1):
        s = ""
        s2 = ""
        for j in range(size):
            s += image[i][j]
            s2 += image[j][i]
        t.append(s)
        t2.append(s2)

    r.append(t)
    r.append(t2)

    return r

def apply_rules(s, image):
    img_list = []
    for j in range(int(len(image)/s)):
        for k in range(int(len(image)/s)):
            sub_image = []
            for i in range(s):
                sub_image.append(image[j*s+i][k*s:k*s+s])
            rots = rotations(sub_image)

            for rot in rots:
                match = False
                for rule, res in rules:
                    if rule == rot:
                        img_list.append(res)
                        match = True
                        break
                if match == True:
                    break
    return img_list

def build_image(img_list):
    size = int(len(img_list)**0.5)

    new_img = []

    for i in range(len(img_list)):
        if i % size == 0:
            new_img.extend(img_list[i])
        else:
            for j in range(len(img_list[i])):
                new_img[j - len(img_list[i])] += img_list[i][j]

    return new_img

with open('input', 'r') as f:
    lines = f.read().strip().split("\n")

    rules = []

    for line in lines:
        l = line.split(" => ")
        rules.append((l[0].split("/"), l[1].split("/")))

    image = [".#.", "..#", "###"]

    for i in range(18):
        if len(image) % 2 == 0:
            img_list = apply_rules(2, image)
        else:
            img_list = apply_rules(3, image)
        image = build_image(img_list)

    print(''.join(image).count("#"))