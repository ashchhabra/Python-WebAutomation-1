from selenium import webdriver
import yaml

logindetails =open('credentials.yml')
parseFile=yaml.load(logindetails,Loader=yaml.FullLoader)

myName =parseFile['user']['username']
myPwd =parseFile['user']['password']
print("parsing complete")


chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver=webdriver.Chrome(chrome_options=chrome_options)
def login(url,uid,uname,pid,pname,submitid):
  driver.get(url)
  driver.find_element_by_id(uid).send_keys(uname)
  driver.find_element_by_id(pid).send_keys(pname)
  driver.find_element_by_name(submitid).click()
  driver.maximize_window()
login("https://sso.teachable.com/secure/212820/users/sign_in?clean_login=true&reset_purchase_session=1","user_email",myName,"user_password",myPwd,"commit")
