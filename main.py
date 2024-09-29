import requests
from bs4 import BeautifulSoup
import re
import time

url = 'website.org'  

headers = {
    'User-Agent': ''
}



def get_artical(url,terms):
    r = requests.get(url, headers=headers)

    # 200 is code for connected
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        articals = soup.find_all("span")
        # print(articals)
        for artical in articals:
            content = artical.select_one("a")       
            if not content == None:
                if any(re.search(term, content.text, re.IGNORECASE) for term in terms):
                    headline = content.text
                    print(headline)
    else:
        print(f"Error: {r.status_code}")
def get_next_site(url,next_site):
    req = requests.get(url,headers=headers)
    soup = BeautifulSoup(req.content,'html.parser')
    element = soup.find(attrs={"aria-label":f"Seite {next_site}"})
    return element["href"]

if __name__ == "__main__":
    pages = 28

    # what are the keywords
    terms = ['slide','closure', 'fastener']

    for i in range(1,pages+1):
        time.sleep(2)
        print(f"Seite: {i}")
        get_artical(url,terms)
        if i<pages:
            url = get_next_site(url,i+1)
        
        

