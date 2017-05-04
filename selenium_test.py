from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get('localhost:8000/home');
assert "JEA and Books" in driver.title

elem = driver.find_element_by_name('searchquery')
elem.clear()
elem.send_keys('Goats' + Keys.RETURN)
assert "No results found." not in driver.page_source
driver.quit()