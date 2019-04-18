from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import UploadForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # form = LoginForm()
    form = UploadForm()
    if form.validate_on_submit():
        flash('YONIGO')
        return redirect('/index')
    return render_template('index.html', title='Sign In', form=form)

