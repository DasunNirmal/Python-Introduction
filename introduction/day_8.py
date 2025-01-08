# Web Scraping

# web scraping is the process of extracting data from websites.

# Requst Libary
# this is a used for making HTTP requests to web servers.

import requests

# GET

# response = requests.get('https://api.github.com/events')
# print(response,"\n") # <Response [200]>

# if response.status_code == 200:
#     print("Request was successful!","\n")
    
#     print(response.headers,"\n")
    
#     content_type = response.headers['Content-Type']
#     print("Content Type:", content_type,"\n")

#     # print(response.text)

#     if 'application/json' in response.headers['Content-Type']:
#         data = response.json()
#         print(data,"\n",type(data),"\n")
# else:
#     print("Request failed with status code:", response.status_code)


# POST

# data = {'username':'Dasun', 'password': '1254'}
# post = requests.post('https://httpbin.org/post',data)

# if post.status_code == 200:
#     print("Login Successful")
#     print(post.text,"\n")
# else:
#     print("Request failed with status code:", post.status_code)

# url = 'https://google.com/search'
# params = {'p': 'python', 'category':'books'}

# response = requests.get(url,params=params)
# print(response.url,'\n')
# print(response.text)


# Basic Authentication

# url = 'https://httpbin.org/get'
# usename = 'Dasun'
# password = '1254'

# responce = requests.get(url,auth=(usename,password))

# if responce.status_code == 200:
#     print("Request was successful!","\n")
#     print(responce.text)
# else:
#     print("Request failed with status code:", responce.status_code)


# BeautifulSoup

from bs4 import BeautifulSoup


html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie&quot; class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie&quot; class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie&quot; class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.title,'\n')
# print(soup.title.name,'\n')
# print(soup.p,'\n')
# print(soup.a,'\n')
# p_tag = soup.find('p')
# print(p_tag,'\n')
# p_tags = soup.find_all('p')
# print(p_tags,'\n')

# Fetch a webpage, check if the request was successful, and extract the main heading text form the page's
# content. base url is https://example.com

# resposnce = requests.get('https://example.com')

# if resposnce.status_code == 200:
#     print("Request was successful!","\n")
#     soup = BeautifulSoup(resposnce.text, 'html.parser')
#     if soup.h1.text:
#         print(soup.h1.text,"\n")
#     else:
#         print("No main heading found.")
# else:
#     print("Request failed with status code:", resposnce.status_code)


# API Integration


base_url = "https://api.open-meteo.com/v1/forecast"

params = {
    'latitude': 6.711140477751053,
    'longitude': 79.90983285116995,
    'current': 'temperature_2m,windspeed_10m'
}

# response = requests.get(base_url, params=params)
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("Request failed with status code:", response.status_code)


def fetch_weather_data(latitude, longitude):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current': 'temperature_2m,windspeed_10m'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Request failed with status code:", response.status_code)
        return None
    
# print("Weather Data", fetch_weather_data(6.711140477751053, 79.90983285116995))

# def parse_weather_data(data):

#     print("Current Weather Data",data,"\n")

#     if data:
#         temperature = data['current']['temperature_2m']
#         windspeed = data['current']['windspeed_10m']
#         return  f"temperature {temperature}, windspeed {windspeed}"
#     else:
#         print("No weather data available.")

# print(parse_weather_data(fetch_weather_data(6.711140477751053, 79.90983285116995)))

# SyntaxError
# RuntimeError

print("Hello World")

import pdb

def multiplication(a,b):
    answer = a * b
    return answer

# pdb.set_trace() # when this is here the code will not run after this this line
breakpoint() 
x = input("Enter a number: ")
y = input("Enter a number: ")
mul = multiplication(x,y)
print(mul)