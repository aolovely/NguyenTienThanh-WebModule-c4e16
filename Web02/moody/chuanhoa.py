def ChuanHoa(n):
    n =n.lower()
    n = n.title()
    n = n.strip()
    for i in range(len(n)):
        n = n.replace('  ', ' ',)
    return n
