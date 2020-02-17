lisa=[11,22,33,44,55,66]

for i in lisa:
    if i==33:
        lisa.remove(i)
        continue
    print('44index', lisa.index(44))
    print('33index', lisa.index(33))

    print(i)

