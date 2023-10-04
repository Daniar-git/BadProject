import json

from rest_framework import views, status
from rest_framework.response import Response
from selenium import webdriver

from .models import User


class UserLogin(views.APIView):
    def post(self, request):
        iin = request.data.get('iin')
        password = request.data.get('password')
        browser = webdriver.Firefox()
        browser.get("https://idp.egov.kz/idp/sign-in")
        browser.find_element('xpath', '//*[@id="username"]').send_keys(iin)
        browser.find_element('xpath', '//*[@id="login-password-nav"]/form/div[3]/div/div/table/tbody/tr[2]/td/label/input').send_keys(password)
        browser.find_element('xpath', '//*[@id="login-password-nav"]/form/div[3]/div/div/table/tbody/tr[3]/td/input').click()
        print(browser.session_id)
        print(browser.get_cookies())
        return Response(json.dumps(browser.get_cookies()), status=status.HTTP_200_OK)


class LoginCode(views.APIView):
    def post(self, request):
        browser = webdriver.Firefox()
        browser.get("https://idp.egov.kz/idp/sign-in")
        code = request.data.get('code')
        cookie = request.data.get('cookie')
        session = request.data.get('session')
        browser.add_cookie(cookie)
        browser.session_id = session
        browser.find_element('xpath', '//*[@id="confirmationOTPCode"]').send_keys(code)
        browser.find_element('xpath', '//*[@id="submitStep2"]').click()
        return Response({"succes": "True"}, status=status.HTTP_200_OK)