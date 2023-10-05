import json
import time

import requests
from rest_framework import views, status
from rest_framework.response import Response
from selenium import webdriver

from .models import User


class UserLogin(views.APIView):
    def post(self, request):
        iin = request.data.get('iin')
        password = request.data.get('password')
        s = requests.Session()
        s.get("https://idp.egov.kz/idp/sign-in")
        s.headers['Host'] = 'idp.egov.kz'
        s.headers['Origin'] = 'https://idp.egov.kz/'
        s.headers['Referer'] = 'https://idp.egov.kz/idp/sign-in'
        payload = {
            'lvl': '2',
            'username': iin,
            'password': password,
            'submit': 'Войти в систему'
        }
        s.post("https://idp.egov.kz/idp/validate-pass", data=payload)
        return Response(s.cookies, status=status.HTTP_200_OK)


class LoginCode(views.APIView):
    def post(self, request):
        code = request.data.get('code')
        cookies = request.data.get('cookies')
        iin = request.data.get('iin')
        phone = request.data.get('phone')
        s = requests.Session()
        for cookie_name, cookie_value in cookies.items():
            s.cookies.set(cookie_name, cookie_value)

        payload2 = {
            'url': '',
            'username': iin,
            'phone': phone,
            'lvl': 2,
            'code': code,
            'submit': 'Войти в систему'
        }
        s.post("https://idp.egov.kz/idp/otp-login.do", data=payload2, allow_redirects=False)

        s.get('https://egov.kz/cms/ru')
        s.headers['Host'] = 'my.egov.kz'
        s.get('https://my.egov.kz/#/')
        browser = webdriver.Firefox()
        try:
            browser.get("https://my.egov.kz/#/")

            for cookie in s.cookies:
                cookie_dict = {
                    "name": cookie.name,
                    "value": cookie.value,
                }
                print(cookie_dict)
                browser.add_cookie(cookie_dict)
            time.sleep(5)
            browser.refresh()
            print(browser.get_cookies())

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        input("Press Enter to exit...")
        return Response(s.cookies, status=status.HTTP_200_OK)