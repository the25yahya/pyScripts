import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

r = requests.get("https://www.wired.com/")

if r.status_code == 200:
    
    soup = BeautifulSoup(r.content, "html.parser")
    ##############################################
    nav_items = soup.find_all("nav")  # Finding all 'nav' elements
    div_items = soup.find_all("div")
    main_section = soup.find_all("main")
    ##############################################
    
    
    category_links = []
    
    for item in nav_items:
        links = item.find_all("a")
        for link in links:
             href = link.get("href")
             if href and "category" in href :
                 #print(f"item is a category {link}")
                 #print("Link Text:", link.get_text(strip=True))
                 #print("Link URL:", link.get('href'))
                 #print("="*80)  # Separator for readability
                 if not href.startswith(('http://', 'https://')):
                    # If not, join it with the root domain
                    href = urljoin("https://www.wired.com/", href)
                 category_links.append(href)
    print(f"\033[91m\033[1m category links are : \033[0m {category_links}")
    
    
    #for item in main_section:
     #   print("MAIN SECTIONS ============================== ", item.prettify())
    #for item in div_items:
        #print("Div Class : ", item.get('class'))      
    pages_data = []     
    
    for item in category_links:
        r = requests.get(item) #send request to each element in the categorie links
        soup = BeautifulSoup(r.content, "html.parser") #parse the content of each response
        title = soup.title.text if soup.title else "no title"
        pages_data.append((title,r.content)) 
    
    for content,title in pages_data:
        print(f"\033[91m\033[1m TITLE \033[0m : {title}")   
        print(f"\033[91m\033[1mCONTENT \033[0m: {content}")
        print("="*50)   
else:
    print(f"Failed to retrieve content: {r.status_code}")

