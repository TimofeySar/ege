a = "КОСУФ"
sh = 0
ssh = 1
for q in a:
    for w in a:
        for e in a:
            for r in a:
                for t in a:
                    sh += 1
                    s = q+w+e+r+t
                    if s.count('Ф') == 0 and s.count('У') == 2:
                        ssh = sh
print(ssh)