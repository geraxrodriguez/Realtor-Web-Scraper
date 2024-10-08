from project import check_zip, get_addresses, get_prices, get_links, email
from bs4 import BeautifulSoup
import requests
import pytest
import sys
import re

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Referer': 'https://google.com',
        'DNT': '1',
        }
# Use whatever zipcode
url = f"https://www.realtor.com/realestateandhomes-search/46312/type-multi-family-home/radius-1/sby-1"
page = requests.get(url, headers=headers).text
soup = BeautifulSoup(page, "html.parser")
zipcode = '46312'
addresses = get_addresses(soup)
prices = get_prices(soup)
links = get_links(soup)

def test_check_zip_invalid(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['project.py'])
    with pytest.raises(SystemExit):
        check_zip()
    monkeypatch.setattr(sys, 'argv', ['project.py', '1', '2', '3'])
    with pytest.raises(SystemExit):
        check_zip()
    monkeypatch.setattr(sys, 'argv', ['project.py', '543210'])
    with pytest.raises(SystemExit):
        check_zip()

def test_check_zip_valid(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['project.py', '60639'])
    assert check_zip() == '60639'

def test_get_addresses():
    assert get_addresses(soup) == ['4131 Grace St, East Chicago, IN 46312', '1215 E Columbus Dr, East Chicago, IN 46312', '530 Narva Pl, East Chicago, IN 46312', '2834 Schrage Ave, Whiting, IN 46394', '3836 Parrish Ave, East Chicago, IN 46312']

def test_get_prices():
    assert get_prices(soup) == ['$99,000', '$115,000', '$129,900', '$139,900', '$150,000']

def test_get_links():
    assert get_links(soup) == ['https://www.realtor.com/realestateandhomes-detail/4131-Grace-St_East-Chicago_IN_46312_M43304-05801', 'https://www.realtor.com/realestateandhomes-detail/1215-E-Columbus-Dr_East-Chicago_IN_46312_M33450-94281', 'https://www.realtor.com/realestateandhomes-detail/530-Narva-Pl_East-Chicago_IN_46312_M36673-73301', 'https://www.realtor.com/realestateandhomes-detail/2834-Schrage-Ave_Whiting_IN_46394_M38549-37864', 'https://www.realtor.com/realestateandhomes-detail/3836-Parrish-Ave_East-Chicago_IN_46312_M39214-72093']

def test_email():
    assert email(addresses, prices, links, zipcode) == 'Email Sent :)'