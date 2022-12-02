import yfinance as yf
import requests
import pandas as pd
import matplotlib.pyplot as plt
import io


# https://towardsdatascience.com/python-plotting-api-expose-your-scientific-python-plots-through-a-flask-api-31ec7555c4a8

goog_stock_data = yf.download('GOOG','2004-08-19')

plt.figure(figsize=(15, 15))

plt.ylabel('GOOG Closing Price')

goog_stock_data.Close.plot()

# here is the trick save your figure into a bytes object and you can afterwards expose it via flask
bytes_image = io.BytesIO()
plt.savefig(bytes_image, format='png')
bytes_image.seek(0)
bytes_image