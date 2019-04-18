from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import UploadForm
from fastai.vision import load_learner, open_image, BytesIO
import os


model_path = os.getcwd() + '/ai/model'
model_name = 'model.pkl'
model = load_learner(model_path, model_name)


def predict(image_bytes):
    image = open_image(BytesIO(image_bytes))
    x, class_, losses = model.predict(image)
    return x


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        image_bytes = form.image.data.read()
        prediction = predict(image_bytes)
        flash(str(prediction))
        return redirect('/index')
    return render_template('index.html', title='upload', form=form)
