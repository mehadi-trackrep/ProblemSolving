# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

regex_obj = re.compile(r'https?://(?:www.|ww2.)?([\w|\.]+)/')

text = 'http://www.xyz.com/news, https://abc.xyz.com/jobs, http://abcd.xyz.com/jobs2 http://ww2.mmh49.com/news'
all_domains = re.findall(regex_obj, text)
print(all_domains)
# print(';'.join(all_unique_domains))

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