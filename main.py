from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Properly configure the ChromeDriver service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://www.python.org")
assert "Python" in driver.title

elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

input("Press Enter to close the browser...")  # Keeps the browser open until user input
driver.close()
