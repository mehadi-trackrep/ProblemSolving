
def map_argument_func(a: str, b: int):
    return a + str(b)

def ck_map_func():
    ss = ["s", "s", "s"]
    ans = list(
        map(
            map_argument_func,
            ss,
            list(range(1, 4))
        )
    )
    print(ans)

if __name__=='__main__':
    ck_map_func()

    dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk", 'artra')

    palindromes = list(
        filter(
            lambda word: word == word[::-1],
            list(dromes)
        )
    )

    print(palindromes)
    print(type(dromes))
