from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get('localhost:8000/home');

elem = driver.find_element_by_name('searchquery')
elem.send_keys('Goats' + Keys.RETURN)

driver.quit()