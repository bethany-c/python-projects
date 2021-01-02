

import tkinter as tk
from tkinter import *
from tkinter import ttk
#import requests

# base is EUR
url = 'https://api.exchangeratesapi.io/latest'

class convertCurrency():
    # constructor
    def __init__(self, url):
        self.data = GET.get(url).json()
        
        # extract rates from json
        self.rates = self.data['rates']

    # function to convert an amount given currencies
    def convert(self, convertFrom, convertTo, amount):
        givenAmount = amount
        # convert to base 
        if convertFrom != 'EUR':
            amount = amount / self.rates[convertFrom]
        amount = round(amount * self.rates[convertTo], 5)
        return amount


