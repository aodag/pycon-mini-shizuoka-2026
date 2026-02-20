import sys

def listed():
    return (line.strip() + " processed" for line in sys.stdin)

for l in listed():
    print(l)

    
