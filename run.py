from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

import os
import time

firstName = 'FIRSTNAME'
lastName = 'SURNAME'
firstName2 = 'FIRSTNAME2'
lastName2 = 'SURNAME2'
myAddress = 'ADDRESSLINE'
myPostcode = 'POSTCODE'
dayPhone = 'PHONENUM'
eveningPhone = 'PHONENUM'
myEmail = 'EMAIL'
myAge = 'AGE'
profession = 'PROFESSION'
comedian = 'COMEDIANNAME'
faveShow = 'TVSHOW'

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='PATH HERE')
browser.get('https://www.sroaudiences.com/shows.asp')
time.sleep(2)
showButtons = browser.find_elements_by_css_selector('.WhiteText a')
showList = browser.find_elements_by_css_selector('.WhiteText strong')

print("Ok, here's what shows are available at the moment:")

x=0;
tvShows = []
for tvShow in showList:
	showName = tvShow.text.encode("utf-8")
	if showName != 'JOIN OUR MAILING LIST':
		if len(showName) > 4:
			print str(x)+" "+str(showName)
			tvShows.append(showName)
			x+=1

showLinks = []
for tvBtn in showButtons:
	btnLink = tvBtn.get_attribute("href")
	showLinks.append(btnLink)

tvLinks = filter(lambda x: 'show_id' in x, showLinks)

print('---------------------------------')
print('Which show would you like to see?')
showtoGet = input()
print("Attempting to get tickets for "+str(tvShows[showtoGet]))
browser.get(showLinks[showtoGet])
time.sleep(3)


nameTitle = browser.find_element_by_xpath("//select[@name='Title']/option[text()=' Mr. ']")
firstnameField = browser.find_element_by_name('First_name')
lastnameField = browser.find_element_by_name('Last_name')
addressField = browser.find_element_by_name('Full_postal_address')
postcodeField = browser.find_element_by_name('Postcode')
dayPhoneField = browser.find_element_by_name('Daytime_phone_number')
eveningPhoneField = browser.find_element_by_name('Evening_phone_number')
emailField = browser.find_element_by_name('Email_address')
ageField = browser.find_element_by_name('Age')
termsBox = browser.find_element_by_id('TermsBox')
submitBtn = browser.find_element_by_name('submit')

nameTitle.click()
firstnameField.send_keys(firstName)
lastnameField.send_keys(lastName)

try:
    ticketNum = browser.find_element_by_xpath("//select[@id='numtickets']/option[text()='2']")
    ticketNum.click()
except NoSuchElementException:
    pass

time.sleep(2)

try:
    person2First = browser.find_element_by_id('second_person_first_name')
    person2First.send_keys(firstName2)
except NoSuchElementException:
    pass

try:
    person2Last = browser.find_element_by_id('second_person_last_name')
    person2Last.send_keys(lastName2)
except NoSuchElementException:
    pass

try:
    firstchoice = Select(browser.find_element_by_name("1st_choice"))
    firstchoice.select_by_index(3)
except NoSuchElementException:
    pass

try:
    secondchoice = Select(browser.find_element_by_name("2nd_choice"))
    secondchoice.select_by_index(4)
except NoSuchElementException:
    pass

try:
    thirdchoice = Select(browser.find_element_by_name("3rd_choice"))
    thirdchoice.select_by_index(5)
except NoSuchElementException:
    pass


addressField.send_keys(myAddress)
postcodeField.send_keys(myPostcode)
dayPhoneField.send_keys(dayPhone)
eveningPhoneField.send_keys(eveningPhone)
emailField.send_keys(myEmail)
ageField.send_keys(myAge)

try:
    professionSelect = browser.find_element_by_name("Profession")
    professionSelect.send_keys(profession)
except NoSuchElementException:
    pass

try:
    comedianSelect = browser.find_element_by_name("Favourite_comedian")
    comedianSelect.send_keys(comedian)
except NoSuchElementException:
    pass

try:
    showSelect = browser.find_element_by_name("Favourite_comedy_show")
    showSelect.send_keys(faveShow)
except NoSuchElementException:
    pass

try:
    termsBox2 = browser.find_element_by_id("TermsBox2")
    termsBox2.click()
except NoSuchElementException:
    pass

termsBox.click()

#submit form
submitBtn.click()
print("Applied for tickets!");
