import requests 
from bs4 import BeautifulSoup
import sys
def main():

    if len(sys.argv) != 2:
        sys.exit(1)

    url= sys.argv[1]
    if not url.startswith("http"):
        url="https://"+url
    webpage=requests.get(url)
    if webpage.status_code ==200:
        soup=BeautifulSoup(webpage.content,"html.parser")
        title=soup.title
        body=soup.body
        links=soup.find_all("a")
        if (title):
            print(title.string+"\n")
        
        if (body):
            print(body.get_text(separator="\n",strip=True))
            print("\n")
        if(links):
            for link in links:
                link=link.get("href")
                print(link)
                print("\n")

    else:
        print("cant scrape the link")
if __name__=="__main__":
    main()
        



