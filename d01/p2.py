def read_input():
    with open("input.txt", "r") as f:
        return f.read()


def parse_input(input):
    rows = input.split("\n")
    return rows

def get_loads(rows):
    loads = []
    temp = []
    for r in rows:
        if r == "":
            loads.append(temp)
            temp = []
        else:
            temp.append(int(r))
    return loads
        
input = parse_input(read_input())
loads = get_loads(input)

total = [ sum(i) for i in loads ]
total.sort()
top3 = total[-3:]
print(top3)
print(sum(top3))
