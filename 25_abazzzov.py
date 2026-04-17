from fnmatch import fnmatch

for i in range(0,10**10, 7244):
    if fnmatch(str(i), '12*937?4'):
        print(i, i//7244)