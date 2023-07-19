
def map_argument_func(a: str, b: int):
    return a + str(b)

def ck_map_func():
    ss = ["s", "s", "s"]
    ans = list(map(map_argument_func, ss, range(1, 3)))
    print(ans)

if __name__=='__main__':
    ck_map_func()

    dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

    palindromes = list(filter(lambda word: word == word[::-1], dromes))

    print(palindromes)
