# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #keep open the browser 
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach' , True)
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://en.wikipedia.org/wiki/Main_Page')

# view_count = driver.find_element(By.XPATH , value='/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]')
# print(f'The totaL number of articles on the wikipedia is {view_count.text}')
# #interact with the webpage using the .click method 
# # view_count.click()

# # all_portals = driver.find_element(By.LINK_TEXT , value= 'Content portals')
# # all_portals.click()

# searchbar = driver.find_element(By.XPATH , value = '//*[@id="p-search"]/a/span[1]')
# # searchbar = driver.find_element(By.NAME , value='search')
# searchbar.click()
# searchbar.send_keys('Python')
# # driver.quit()  


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
# Navigate to Wikipedia
driver.get('https://www.wikipedia.org/')
    
def wikipedia_search(query):
    # Wait for the search input field to be clickable
    search_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'search'))
    )
    
    # Enter the search query and press Enter
    search_input.clear()  # Clear the input field if necessary
    search_input.send_keys(query)
    search_input.send_keys(Keys.RETURN)  # Press Enter to search
    
    # Optionally, wait for a while to view the results
    WebDriverWait(driver, 10).until(
        EC.title_contains(query)  # Wait until the title contains the search term
    )
    
    # You can further process the search results here if needed
    print(f"Searching for: {query}")
    print(f"Current page title: {driver.title}")
    
    # Optional: close the browser after a delay or keep it open
    time.sleep(10)
    driver.quit()

# Example usage
if __name__ == "__main__":
    term_to_search = str(input("Enter the search term: "))  # Change this to whatever you want to search for
    wikipedia_search(term_to_search)
