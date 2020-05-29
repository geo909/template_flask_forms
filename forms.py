from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Regexp, Length, Email
import email_validator

class MyForm(FlaskForm):
    fhcode = StringField('FH code', validators=[InputRequired(), 
                                    Regexp(regex=r'^(fh|FH)',
                                    message='FH code needs to start with "FH"') 
                                    ]
                        )
    name = StringField('Name', validators=[Length(min=2)])
    email = StringField('Email', validators = [Email()])
    comments = StringField('Comments')
    discount = BooleanField('Has discount?')
