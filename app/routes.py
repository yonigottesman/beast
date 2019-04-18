from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import UploadForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        image_bytes = form.image.data.read()
        flash('YONIGO')
        return redirect('/index')
    return render_template('index.html', title='upload', form=form)

