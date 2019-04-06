from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.accept_untrusted_certs = True
chrome_options.assume_untrusted_cert_issuer = True
chrome_options.add_argument('test-type')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('disable-popup-blocking')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-useAutomationExtension')
chrome_options.set_headless(True)
browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
browser.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

#search = browser.find_element_by_name('q')
#search.send_keys('Testing')
#submit = browser.find_element_by_name("btnK")
#search.submit()
allelem = browser.find_elements_by_xpath('//input')
for e in allelem:
    print(e.get_attribute('name'))
# submit.click()


browser.quit()
