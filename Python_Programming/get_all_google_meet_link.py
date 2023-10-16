import webbrowser

# BASE_LINK = "https://meet.google.com/xob-{0}w{1}e-gr{2}"
BASE_LINK = "https://meet.google.com/xob-xw{0}e-gr{1}"
# BASE_LINK = "https://meet.google.com/xob-xw{0}e-gr{1}?authuser=0"

POSSIBLE_CHAR_LIST = ['o', 'e', 'c']
SZ = 2

"""
    {0} -> x,y,v
"""

def get_all_links():
    for i in range(3):
        for j in range(3):
            a_possible_link = BASE_LINK.format(POSSIBLE_CHAR_LIST[i], POSSIBLE_CHAR_LIST[j])
            print(a_possible_link)
            webbrowser.open(a_possible_link)
        
get_all_links()