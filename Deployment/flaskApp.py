from flask import Flask, render_template, send_file, request, redirect, url_for
from markupsafe import escape
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import io
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ej.html', url="", data = None)

@app.route('/', methods=['POST', 'GET'])
def index_img():
    if request.method == 'POST':
        return render_template('ej.html', url=url_for('fig', data= request.form), data=request.form)
    else:
        return render_template('ej.html', url="")


@app.route('/fig/<data>')
def fig(data):
    return send_file(create_image(data), mimetype='image/png')


def create_image(data):
    fig = plt.figure(figsize=(10,5))
    fig.patch.set_facecolor('gray')
    np.random.seed = 12
    carreras = ['ingeniería', 'política', 'veterinaria', 'ulinaria', 'teología', 'jueguitos']
    y_pos = np.random.randint(10, size=len(carreras))
    plt.barh(carreras,y_pos, height=1, color='#5c03f5')
    ax = plt.gca()
    ax.tick_params(axis=u'both', which=u'both',length=0)
    ax.set_facecolor((0, 0, 0))
    ax.grid(axis="x")
    [i.set_color("white") for i in plt.gca().get_xticklabels()]
    [i.set_color("white") for i in plt.gca().get_yticklabels()]
    for spine in ax.spines:
        ax.spines[spine].set_visible(False)
    img = io.BytesIO()
    fig.savefig(img, transparent=True)
    img.seek(0)
    return img