from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import requests
import smtplib
import sys
import re

def main():
    # Check zipcode
    zipcode = check_zip()
    # Create our own headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Referer': 'https://google.com',
        'DNT': '1',
        }
    url = f"https://www.realtor.com/realestateandhomes-search/{zipcode}/type-multi-family-home/radius-1/sby-1"
    # Get URL and make some soup
    try:
        page = requests.get(url, headers=headers).text
        soup = BeautifulSoup(page, "html.parser")
        # Call scraping functions
        addresses = get_addresses(soup)
        prices = get_prices(soup)
        links = get_links(soup)
    except Exception:
        sys.exit("Oops! Looks like there's an error with the webpage. Please try again later!")
    # Send email
    print(email(addresses, prices, links, zipcode))

def check_zip():
    if len(sys.argv) < 2:
        sys.exit('Oops! Looks like you forgot something!')
    elif len(sys.argv) > 2:
        sys.exit('Oops! Looks like you typed too much!')
    elif not re.match(r"^\d{5}(-\d{4})?$", sys.argv[1]):
        sys.exit('Oops! Please type a valid zipcode!')
    else:
        return sys.argv[1]

# Get addresses
def get_addresses(soup):
    addresses = soup.find_all(class_='jsx-2683691781 address ellipsis srp-page-address srp-address-redesign')
    return [address.text for address in addresses[:5]]

# Get prices
def get_prices(soup):
    prices = soup.find_all('span', class_="Price__Component-rui__x3geed-0 gipzbd")
    return [price.text for price in prices[:5]]

def get_links(soup):
    links = soup(class_="jsx-1534613990 card-anchor")
    return [f"https://www.realtor.com{link['href']}" for link in links[:5]]

def email(addresses, prices, links, zipcode):
    # Create formatted list so that when sending email, the address, price, and link for each prop. are together
    formatted_list = '\n'.join([f'{i}. {price}, {address}, {link}' for i, (address, price, link) in enumerate(zip(addresses, prices, links), 1)])
    # Get pw
    with open("password.txt", "r") as file:
        pw = file.read().strip()
    email_password = pw
    email_sender = 'delajeezy45@gmail.com'
    email_receiver = 'gerarodriguez@proton.me'
    message = MIMEText(formatted_list)
    message['Subject'] = f'5 Cheapest Multi-Family Properties Near {zipcode}'
    message['From'] = email_sender
    message['To'] = email_receiver

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, message.as_string())
        return 'Email Sent :)'

if __name__ == '__main__':
        main()