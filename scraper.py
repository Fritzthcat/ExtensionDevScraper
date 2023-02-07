import requests
from bs4 import BeautifulSoup

# Set URL of Chrome Web Store
url = 'https://chrome.google.com/webstore/category/extensions?hl=en'
# Get the page content
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Find all extensions
extensions = soup.find('div', class_ = 'e-f-w').find_all('div', class_ = 'h-tb-sc-c')

# Iterate over the list of extensions and find the email
for extension in extensions:
    extension_url = extension.find('a')['href']
    # Get the page content
    extension_page = requests.get(extension_url)
    extension_soup = BeautifulSoup(extension_page.content, 'html.parser')
    email = extension_soup.find('div', class_ = 'e-n').find('a').text
    # Print out the email
    print(email)