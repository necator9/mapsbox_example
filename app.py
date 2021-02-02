from flask import Flask
from flask import request, url_for, render_template, redirect
import os
import dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
dotenv.load_dotenv(os.path.join(basedir, '.env'))


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def my_maps():
    token = os.getenv('MAPS_TOKEN')
    coordinates = {'lat': 51.756845, 'long': 11.956438}

    return render_template('index.html', mapbox_access_token=token, coordinates=coordinates)


if __name__ == '__main__':
    app.run(debug=True)
