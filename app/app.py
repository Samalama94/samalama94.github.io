from flask import Flask, render_template 
from flask import request
from flask import send_from_directory
import os
import sys
import glob
import binascii
import argparse


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/cdn/<path:filepath>')
def download_file(filepath):
    dir,filename = os.path.split((filepath))
    return send_from_directory(dir, filename, as_attachment=False)


if __name__ == '__main__':
    app.run(debug=True)
