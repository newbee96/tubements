from flask import Flask, render_template, request, redirect
import downloader
import httplib
import requests

app = Flask(__name__)

@app.route('/')
def index(name=None):
        return render_template('index.html', name=name)


@app.route('/signup', methods = ['POST'])


def signup():
    postdata = request.form.get('ytlink')
    #if requests.head("http://"+postdata) == 200:
    downloader.main(["-y"+postdata, "-o"+postdata])
    return render_template('loading.html')





if __name__ == "__main__":
    app.run(debug=True)
