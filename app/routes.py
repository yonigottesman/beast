from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import UploadForm
from fastai.vision import load_learner, open_image, BytesIO
import os
import base64

model_path = os.getcwd() + '/ai/model'
model_name = 'model_with_unicorn.pkl'
model = load_learner(model_path, model_name)


def predict(image_bytes):
    image = open_image(BytesIO(image_bytes))
    x, class_, losses = model.predict(image)
    # print(class_, losses)
    return x


def validate_image_data_url(data_url):
    if len(data_url.split(';')) >= 2 and\
       len(data_url.split(';')[1].split(',')) >= 2:
        return True
    else:
        return False
    

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        data_url = form.image.data
        message = ''
        if validate_image_data_url(data_url):
            content = data_url.split(';')[1]
            image_encoded = content.split(',')[1]
            image_bytes = base64.decodebytes(image_encoded.encode('utf-8'))
            message = str(predict(image_bytes))
        else:
            message = 'Upload valid image'
        flash(message)
        return redirect('/index')
    return render_template('index.html', title='upload', form=form)
