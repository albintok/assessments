# def group_by_owners(files):
#     return

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

d = {}
for i in files.keys():
    if files[i] in d:
        d[files[i]] = d[files[i]] + [i]
    else:
        d[files[i]] = [i]
print(d)








# print(group_by_owners(files))

