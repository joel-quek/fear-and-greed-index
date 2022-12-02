from flask import Flask
from flask import send_file
from flask import render_template
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns

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

if __name__=='__main__':
    app.debug = True
    app.run()

    # https://stackoverflow.com/questions/10219486/flask-post-request-is-causing-server-to-crash