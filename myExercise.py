import sys
with open(sys.argv[1]) as f:
    dict = {name:dep for (name,dep) in [x.strip().split(":") for x in f.readlines()]}
for name in sys.argv[2].split(","):
    try:
        print(f"Name: {name}, University: {dict[name]}")
    except KeyError:
        print(f"No record of '{name}' was found!")
