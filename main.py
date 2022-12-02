from flask import Flask
from flask import send_file
from flask import render_template
import io
import base64

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns

import yfinance as yf
import requests
import pandas as pd

# SOURCE OF THIS: Visualize with Seaborn and Matplotlib on Flask https://www.youtube.com/watch?v=shSqnROZ1o8 

# virtualenv FLASK_APP=app.py 
# VIRTUAL ENVIRONMENT https://www.youtube.com/watch?v=QjtW-wnXlUY

fig,ax=plt.subplots(figsize=(6,6))
ax=sns.set_style(style="darkgrid")

x=[i for i in range(100)]
y=[i for i in range(100)]

app=Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('index.html') # THIS line is causing the ERROR
    # SOLVED TEMPLATENOTFOUND ERROR https://www.youtube.com/watch?v=6TPh6jlpGvA

@app.route('/visualise')
def visualise():
    sns.lineplot(x,y)
    canvas=FigureCanvas(fig)
    img=io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img,mimetype='img/png')

# This part is new
@app.route('/technical')
def technical():
    goog_stock_data = yf.download('GOOG','2004-08-19') # dataframe
    sns.lineplot(goog_stock_data.index,goog_stock_data['Close'])
    canvas=FigureCanvas(fig)
    img=io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img,mimetype='img/png')
    '''
    plt.figure(figsize=(15, 15))
    plt.ylabel('GOOG Closing Price')
    goog_stock_data.Close.plot()
    # https://stackoverflow.com/questions/26132693/matplotlib-saving-state-between-different-uses-of-io-bytesio
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    return send_file(buf,mimetype='img/png') # buf.read() 
    '''

if __name__=='__main__':
    app.debug = True
    app.run()

    # https://stackoverflow.com/questions/10219486/flask-post-request-is-causing-server-to-crash