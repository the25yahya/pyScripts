"""Login to the Website:

Use the requests library to handle the login process. Some websites may require session handling or token management.
Navigate Through Pagination:

Scrape multiple pages of articles. Ensure that your script can handle and navigate through pagination.
Handle Dynamic Content:

Use Selenium to handle pages that load content dynamically via JavaScript.
Extract Specific Data:

For each article, extract the title, publication date, author, and the main text content.
Store Data in a CSV File:

Save the extracted data in a structured format, such as a CSV file.
Error Handling and Logging:

Implement error handling for network issues, login failures, or unexpected HTML structures. Log errors to a file for later inspection."""


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
    div_links = [] #links from main divs
    category_links = [] #nav links
    pages_data = []  #content from each nav link    
    pages_data_links = []
    ##############################################
    
    #################################
    #get the links in the main divs of the main page 
    for item in div_items:
        links = item.find_all("a")
        for link in links : 
            href = link.get("href")
            div_links.append(href)
    #################################
    
    
    #################################
    #get the links in the items in the nav bar 
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
    #print(f"\033[91m\033[1m category links are : \033[0m {category_links}")
    
    
    #for item in main_section:
     #   print("MAIN SECTIONS ============================== ", item.prettify())
    #for item in div_items:
        #print("Div Class : ", item.get('class'))      
    
    for item in category_links:
        r = requests.get(item) #send request to each element in the categorie links
        soup = BeautifulSoup(r.content, "html.parser") #parse the content of each response
        title = soup.title.text if soup.title else "no title"
        pages_data.append((title,soup)) 
        link = soup.find_all("a")
        link.append(pages_data_links)
else:
    print(f"Failed to retrieve content: {r.status_code}")
    
    
#for item in pages_data[1]:
 #   headers = item.find_all("a")
  #  for header in headers:
   #     href = header.get("href")
    #    pages_data_links.append(href)

print(f"PAGES DATA LINKS : {pages_data_links}")        

