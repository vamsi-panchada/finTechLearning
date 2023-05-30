# import requests

# url = "https://currency-exchange.p.rapidapi.com/listquotes"

# headers = {
# 	"X-RapidAPI-Key": "bef9258816msh7db4395f2f0033fp17eccejsnb6b7e23354d0",
# 	"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# print(response.json())

# import requests

# url = "https://currency-exchange.p.rapidapi.com/exchange"

# querystring = {"from":"SGD","to":"MYR","q":"1.0"}

# headers = {
# 	"X-RapidAPI-Key": "bef9258816msh7db4395f2f0033fp17eccejsnb6b7e23354d0",
# 	"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())

# from urllib import response
# import requests

# response = requests.get('https://v6.exchangerate-api.com/v6/f999688a223170137c71e110/latest/USD')
# print(response.json())


# import requests 

# response = requests.get('https://v6.exchangerate-api.com/v6/f999688a223170137c71e110/codes')

# print(response.json())


import streamlit as st
