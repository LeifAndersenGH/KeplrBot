from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def LoadChromeBrowser(username='YOUR WINDOWS USERNAME'):
    """ Load the Chrome browser with the extension data it needs to access a keplr wallet. """
    
    username = username # Get this windows users login username from the system.

    # Create an abs path with a place holder to allow for username
    user_data_dir = 'C:\\Users\\%(username)s\\AppData\Local\\Google\\Chrome\\User Data\\'
    
    # Place the value of username in the string at point %(username)s
    user_data_dir = user_data_dir % {"username": username}
    
    # A dictionary of chrome options arguments. Keys are option names, values are option values 
    params = {
        "--user-data-dir" : user_data_dir,
        "--profile-directory": "Default"
    }
    
    # Create the chrome options instance
    options = ChromeOptions()
    # Add the keplr extension
    options.add_extension('keplr.crx')
    
    # Dynamically add chrome options.
    for key, value in params.items():
        print('%s=%s' % (key, value))
        options.add_argument('%s=%s' % (key, value))
    
    # Instantiate chrome browser instance with options loaded
    driver = webdriver.Chrome('./chromedriver', chrome_options=options)
    return driver

def Login(driver, wait, password = "YOUR PASSWORD HERE"): 
    
    password_element = wait.until(presence_of_element_located((By.NAME, "password")))
    
    password_element.send_keys(password + Keys.RETURN)    

def SelectAkash(driver, wait):
    select_portfolio = wait.until(presence_of_element_located((By.CLASS_NAME, "popper")))
    
    # Click the container that enables visibility of dropdown menu (for visual effect)
    parent = select_portfolio.find_element(By.XPATH, "./..")
    print(parent)
    parent.click()
    
    akash_xpath = "//*[text() = '%s']" % ("Akash")
    
    wait.until(presence_of_element_located( (By.XPATH, akash_xpath) )).click()
   
def ClaimRewards(driver, wait):
    
    pending_reward = wait.until(presence_of_element_located((By.CLASS_NAME, "container-inner-1k4PbBScgIT9M_LAlCnAr")))
    
    claim_xpath = "//button[text() = '%s']" % ("Claim")
    wait.until(presence_of_element_located( (By.XPATH, claim_xpath) )).click()
                                                          
    low_gas_xpath = "//div[text()='%s']" % ("Low")
    low_gas_button = wait.until(presence_of_element_located( (By.XPATH, low_gas_xpath) ))
    low_gas_button.find_element(By.XPATH, "./..").click()
    
    approve_button_xpath = "//button[text() = '%s']" % ("Approve")
    approve_button = wait.until(presence_of_element_located( (By.XPATH, approve_button_xpath) )).click()

def Staking(driver, wait):
    
    # set window before to current screen before clicking staking?
    window_before = driver.window_handles[0]
    
    # click stake button, opens the new window with validators
    stake_xpath = "//button[text() = '%s']" % ("Stake")
    wait.until(presence_of_element_located( (By.XPATH, stake_xpath) )).click()
    
    # when validator selection screen pops up set window after to this?
    window_after = driver.window_handles[1]
    
    # switch driver to the validator seclection window?
    driver.switch_to_window(window_after)
    time.sleep(5)    
    
    # attempt to click the manage button on the validator 
    validator_manage_xpath = "//*[text() = '%s']" % ("Manage")
    wait.until(presence_of_element_located( (By.XPATH, validator_manage_xpath) )).click() 
    
    #driver.window handle
    #wait.until EC.windows =2
    #//divv@class[container div]
    #manage with space at the end
    
driver = LoadChromeBrowser()
driver.get('chrome-extension://dmkamcknogkgcdfhhbddcghachkejeap/popup.html');
wait = WebDriverWait(driver, 10)

Login(driver, wait)
SelectAkash(driver, wait)
#ClaimRewards(driver, wait)
Staking(driver, wait)
