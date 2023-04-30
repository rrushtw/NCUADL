from selenium import webdriver
from selenium.webdriver.common.by import By

class Portal:
    def __init__(self, driver: webdriver):
        self.__Web: webdriver.Chrome = driver

        # url
        self.__Login: str = 'https://portal.ncu.edu.tw/login'
    # end def

    def Login(self, id, pwd):
        '''go to login page'''
        self.__Web.get(self.__Login)
        self.__Web.execute_script("$('#inputAccount').val('"+id+"');")
        self.__Web.execute_script("$('#inputPassword').val('"+pwd+"');")
        self.__Web.execute_script("$('button[type=\"submit\"]').click();")
    # end def
# end class
