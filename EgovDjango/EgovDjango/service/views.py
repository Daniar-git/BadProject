import time
import requests

from rest_framework import views, status
from selenium import webdriver
from rest_framework.response import Response

class FormaView(views.APIView):
    def post(self, request):
        s = requests.Session()
        cookies = request.data.get('cookies')
        for cookie_name, cookie_value in cookies.items():
            s.cookies.set(cookie_name, cookie_value)
        time.sleep(3)
        print(s.cookies)
        s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        s.headers['Host'] = 'egov.kz'
        s.headers['Origin'] = None
        s.headers['Referer'] = None
        s.get('https://egov.kz/cms/ru/services/buy_sale/pass076_mu')
        s.get('https://egov.kz/services/P3.05/#/declaration/0//')
        s.get('https://egov.kz/services/P80.01/rest/current-user')
        return Response({"succes": "True"} ,status=200)