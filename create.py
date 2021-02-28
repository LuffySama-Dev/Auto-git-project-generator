import sys
import os
from selenium import webdriver



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome("Add Path of your chrome web driver",chrome_options=chrome_options)

browser.get('https://github.com/login')


def create(directory):
    
    # Create a folder if the os path exists
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
    
    # Add username 
    python_button = browser.find_element_by_xpath("//*[@id='login_field']")
    python_button.click()
    python_button.send_keys('Github-Username')
    
    # Add password
    python_button = browser.find_element_by_xpath("//*[@id='password']")
    python_button.click()
    python_button.send_keys('Password')

    # Submit your details (Login)
    python_button = browser.find_element_by_xpath("//*[@id='login']/div[4]/form/input[14]")
    python_button.click()
    
    # Open Create Repository Page
    browser.get('https://github.com/new')
    
    # Add repo name (Name of the folder which was given earlier while running script
    python_button = browser.find_element_by_xpath("//*[@id='repository_name']")
    python_button.click()
    python_button.send_keys(str(sys.argv[2]))
    
    # Uncomment below line's to add readme file while creating the repository itself
#    python_button = browser.find_element_by_xpath("//*[@id='repository_auto_init']")
#    python_button.click()
    
    # Submit's information
    python_button = browser.find_element_by_xpath("//*[@id='new_repository']/div[4]/button")
    python_button.submit()

    # Close the browser once process completed
    browser.quit()
    


if __name__ == "__main__":
    create(sys.argv[1])
