import json
import datetime

# from getpass import getpass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

from NCUPortal import Portal


class WorkingHourComfirmation:
    def __init__(self) -> None:
        with open('Teacher.json', encoding='utf-8') as jsonFile:
            self.__teacher = json.load(jsonFile)

        with open('ProjectMembers.json', encoding='utf-8') as jsonFile:
            self.__members = json.load(jsonFile)

        self.__web: webdriver.Chrome = webdriver.Chrome(
            service=Service('./chromedriver')
        )
        self.__web.maximize_window()
    # end def

    def Login(self) -> None:
        portal: Portal = Portal(self.__web)
        portal.Login(self.__teacher['PortalId'], self.__teacher['PortalPwd'])
    # end def

    def GoToHumanSystem(self) -> None:
        sleep(3)

        subURL = self.__web.execute_script(
            "return $('#portal-home a:contains(\"人事系統\")').attr(\"href\");"
        )

        self.__web.get('https://portal.ncu.edu.tw' + subURL)
    # end def

    def SignUp(self, date: datetime.date) -> None:
        for id in self.__members:
            hourCount: int = 0
            tempDate: datetime.date = date

            while hourCount < 120:
                if tempDate.weekday() >= 5:
                    tempDate += datetime.timedelta(days=1)
                    continue

                self.__web.get(
                    'https://cis.ncu.edu.tw/HumanSys/onboard/parttime/parttimeSignManag/create?parttimeUsually_id=' + str(id)
                )

                # input date
                dateString: str = str(tempDate.year - 1911) + \
                    tempDate.strftime('%m%d')
                self.__web.execute_script(
                    "$('input[name=\"AttendDate\"]').val('" + dateString + "')"
                )

                # input check-in time
                self.__web.execute_script(
                    "$('input[name=\"SigninTime\"]').val('09:00')"
                )
                # input check-out time
                self.__web.execute_script(
                    "$('input[name=\"SignoutTime\"]').val('15:00')"
                )
                # input work hour
                self.__web.execute_script("$('#WorkHours').val('6')")

                # submit
                self.__web.execute_script("$('#submit').click()")

                hourCount += 6
                tempDate += datetime.timedelta(days=1)
            # end loop
        # end loop
    # end def
# end class


yearAndMonth = input('Enter year and month for the accountant:(YYYYMM) ')
targetMonth: datetime.date = datetime.datetime.strptime(
    yearAndMonth + '01', '%Y%m%d').date()
print('The accountant year and month is', targetMonth)

myClass = WorkingHourComfirmation()
myClass.Login()
myClass.GoToHumanSystem()
sleep(3)
myClass.SignUp(targetMonth)
