from bs4 import BeautifulSoup
import requests
from pydantic import BaseModel, ValidationError, validator
from typing import Optional

html_doc = requests.get('https://www.bop.gov/locations/institutions/tha/#send_things')
soup = BeautifulSoup(html_doc.content, 'html.parser')

print(soup.title.text)

# for link in soup.find_all("a"):
#     print(f"Inner text: {link.text}")
#     print(f"Title: {link.get('title')}")
#     print(f"href: {link.get('href')}")

element_location = soup.find("span", attrs={"class": "send-address-state"})

print(element_location.text)


class Checker(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    inmate_id: Optional[str]
    inmate_id_second: Optional[str]
    facility_name: Optional[str]
    street_1: Optional[str]
    street_2: Optional[str]

    @validator('first_name')
    def check_first_name(cls, v):
        assert v != '', 'Empty strings are not allowed.'
        if len(v) > 15:
            raise ValueError('First name exceeds length allowed by Channergy.')
        return v

    @validator('last_name', 'inmate_id')
    def check_last_name_and_inmate_id(cls, v):
        max_val = 40
        last_name_id_length = 0
        for ele in v:
            assert v != '', 'Empty strings are not allowed.'
            last_name_id_length += len(ele)
        if last_name_id_length > max_val:
            raise ValueError('Length of last name and inmate ID is too long.')
        return v

    @validator('inmate_id_second')
    def check_inmate_id_second(cls, v):
        if len(v) < 10:
            raise ValueError('This is too short')
        return v

    @validator('facility_name')
    def check_facility_name(cls, v):
        if len(v) < 10:
            raise ValueError('This is too short')
        return v

    @validator('street_1')
    def check_street_1(cls, v):
        if len(v) < 10:
            raise ValueError('This is too short')
        return v



try:
    tester = Checker(first_name='', last_name='way toolong name goes herelong name goes here ')
    print('values are good')
except ValidationError as e:
    print(e)
    print('nope')

# try:
#     tester2 = Checker(last_name='way toolong name goes herelong name goes here ', inmate_id='01029012910291029')
#     print('values are good')
# except ValidationError as e:
#     print(e)
#     print('no00000pe')