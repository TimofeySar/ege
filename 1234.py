a = sorted(['б','у','р','а','т','и','н','о'])
sh = 1
c = 0
for q in a:
    for w in a:
        for e in a:
            for r in a:
                for t in a:
                    s = q + w + e + r + t
                    if sh % 2 != 0 and q not in ["а", "у", "и", "о"]:
                        c = sh
                    sh += 1
print(sh)

