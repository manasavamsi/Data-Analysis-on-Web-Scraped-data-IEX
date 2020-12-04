from   selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
browser = webdriver.Chrome(r"C:\Users\raghu\Desktop\chromedriver.exe")

#https://www.geeksforgeeks.org/selenium-python-tutorial/
def Wait_Till_Page_Loads( ID_Xpath, Xpath_ID_Details, temp):
    print(temp)
    print(ID_Xpath)
    print(Xpath_ID_Details)
    if (temp == 2):
        print("Hi Stop here")
    try:
        try:
            if ID_Xpath == 'Xpath':
                Boolean_Value = str(bool((browser.find_element_by_xpath(Xpath_ID_Details))))
            elif ID_Xpath == 'ID':
                Boolean_Value = str(bool((browser.find_element_by_id(Xpath_ID_Details))))
            elif ID_Xpath == 'CSS_Selector':
                Boolean_Value = str(bool((browser.find_element_by_css_selector(Xpath_ID_Details))))
            elif ID_Xpath == 'Class_name':
                Boolean_Value = str(bool((browser.find_element_by_class_name(Xpath_ID_Details))))
        except:
            Boolean_Value = "False"
            print("First phase exception to find the element")

        print(Boolean_Value)
        print("Entered Function tab " + Boolean_Value)
        print(temp)
        try:
            if Boolean_Value == 'False':
                while (Boolean_Value == 'False'):
                    print(temp)
                    time.sleep(temp)
                    if temp == 10:
                        print("Closing the webpage as we can't find the file")
                        # browser.quit()
                        break
                    elif temp < 10:
                        print(ID_Xpath + " " + Xpath_ID_Details)
                        temp = temp + 1
                        print(temp)
                        print('Code is executing till here')
                        return Wait_Till_Page_Loads(ID_Xpath, Xpath_ID_Details, temp)
                    else:
                        print("We got the value1")
                        break
            else:
                print("We got the value")

        except Exception as e:
            Boolean_Value = "False"
            print("Second Phase EException near while loop"+str(e))
            return None

    except:
        Boolean_Value = "False"
        print("Third phase Exception near total wait function ")
        return None
# logging.basicConfig(filename='test.log', level=logging.DEBUG)

Main_URL = "https://www.iexindia.com/marketdata/areaprice.aspx"
browser.get(Main_URL)
step1 = browser.find_element_by_xpath('//*[@id="ctl00_InnerContent_ddlPeriod"]/option[4]')
#time.sleep(0.2)
Wait_Till_Page_Loads('Xpath', step1, 1)
browser.find_element_by_xpath('//*[@id="ctl00_InnerContent_ddlPeriod"]/option[4]').click()
step2 = browser.find_element_by_xpath('//*[@id="ctl00_InnerContent_btnUpdateReport"]')
Wait_Till_Page_Loads('Xpath', step2, 1)
browser.implicitly_wait(15)
browser.find_element_by_xpath('//*[@id="ctl00_InnerContent_btnUpdateReport"]').click()
browser.find_element_by_xpath('//*[@id="ctl00_InnerContent_reportViewer_ctl05_ctl04_ctl00_ButtonImgDown"]').click()
button = browser.find_element_by_xpath('//*[@id="ctl00_InnerContent_reportViewer_ctl05_ctl04_ctl00_Menu"]/div[1]/a')
# browser.implicitly_wait(10)
Wait_Till_Page_Loads('Xpath', button, 1)
# browser.find_element(By.Title)
button.click()
browser.close()
# ActionChains(browser).move_to_element(button).click(button).perform()
