from flask import Flask, render_template, redirect, url_for, flash
from forms import MyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

def flash_form(form):
    for field in form:
        if field.name != 'csrf_token':
            flash(f'{field.label.text}:  {field.data}', 'flash-form')

@app.route('/', methods=['GET', 'POST'])
def myform():
    form = MyForm()

    if form.validate_on_submit():
        flash_form(form)
        return redirect(url_for('myform'))

    return render_template('form.html', form=form)

