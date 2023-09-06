# Enter your code here. Read input from STDIN. Print output to STDOUT
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())
regex_obj = re.compile(r'[http|https]://[www\.|ww2\.]*?(\w|\.)+/')
all_unique_domains = set()

for _ in range(N):
    text = input()
    all_domains = re.findall(regex_obj, text)
    print(all_domains)
    all_unique_domains.update(all_domains)

all_unique_domains = sorted(all_unique_domains)
# print(';'.join(all_unique_domains))

"""
import re

def one():
    regex_obj = re.compile(r'https?://(?:www.|ww2.)?([\w|\.]+)/')

    text = 'http://www.xyz.com/news, https://abc.xyz.com/jobs, http://abcd.xyz.com/jobs2 http://ww2.mmh49.com/news'
    all_domains = re.findall(regex_obj, text)
    print(all_domains)

def test1(l):
    # l = ['hasan']
    l = []
    l.append('mmh49')

def two():
    # a_list = ['mehadi']
    a_list = list()
    a_list.append('mehadi')
    test1(l=a_list)
    print(a_list)
    def test2(ll):
        # ll.append('hasan')
        ll = ['hasan']
    test2(ll=a_list)
    print(a_list)

if __name__=='__main__':
    # one()
    two()