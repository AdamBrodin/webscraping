from selenium import webdriver

# the website to open
googleSearch = "https://www.google.com/search?q="

# prompts the user what to search for
searchTerm = input("What would you like to search for?: ")

# the url to scrape
url = googleSearch + searchTerm

# sets up the driver to chrome
driverPath = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(driverPath)
driver.fullscreen_window()

# opens the selected url in a browser
driver.get(url)

# fetches the first class object (first result)
firstResultLink = driver.find_element_by_class_name("yuRUbf")

# gets the <a href = "link"> from that object
firstResultLink = firstResultLink.find_element_by_css_selector('a').get_attribute('href')

# opens link
driver.get(firstResultLink)




