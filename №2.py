print('w x y z')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if ((not x) and y and z and (not w)) or ((not x) and y and (not z) and (not w)) or (
                        x and y and z and (not w)) == 1:
                    print(w, x, y, z)
