import requests
from bs4 import BeautifulSoup
import re
import sys

urls = sys.argv[1:]

if len(urls) != 2:
    print("need 2 urls")
    sys.exit()

mydata = {}

for i, site in enumerate(urls):
    try:
        response = requests.get(site)
        soup = BeautifulSoup(response.content, "html.parser")
        
        for tag in soup(["script", "style"]):
            tag.decompose()
        
        content = soup.get_text().lower()
        content = re.sub(r'[^a-z0-9 ]', '', content)
        words = content.split()
        
        wordcounts = {}
        for word in words:
            wordcounts[word] = wordcounts.get(word, 0) + 1
        
        arr = [0] * 64
        
        for word, freq in wordcounts.items():
            val = 0
            power = 1
            for alphabet in word:
                val = (val + ord(alphabet) * power) % (2**64)
                power = (power * 53) % (2**64)
            
            for j in range(64):
                if (val >> j) & 1:
                    arr[j] += freq
                else:
                    arr[j] -= freq
        
        answer = 0
        for j in range(64):
            if arr[j] > 0:
                answer = answer | (1 << j)
        
        mydata[i] = {"h": answer, "w": len(wordcounts)}
    
    except Exception as err:
        print(f"error: {err}")
        sys.exit()

a = mydata[0]["h"]
b = mydata[1]["h"]

different = bin(a ^ b).count('1')
same = 64 - different

print("Same bits:", same)