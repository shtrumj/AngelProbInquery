from flask import Flask, render_template, request, url_for, redirect
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,RadioField,SubmitField)
from wtforms.validators import InputRequired, Length, DataRequired
from flask_wtf import FlaskForm


app = Flask(__name__, instance_relative_config=False)
app.secret_key = 'the random string'


class InqueryForm(FlaskForm):
    FaultSystem = StringField('מערכת תקולה', validators=[InputRequired(),Length(min=10, max=100)])
    AffectedSystem = StringField('מערכת מושפעת', validators=[InputRequired(),Length(min=10,max=100)])
    AdditionalAffectedSystems = StringField('מערכות מושפעות נוספות', validators=[InputRequired(), Length(min=10, max=100)])
    AffectDuration = StringField('זמן תחת השפעת התקלה', validators=[InputRequired()])
    Solution = TextAreaField('פתרון הבעיה:',validators=[Length(min=20, max = 200)])
    submit = SubmitField('שלח')


@app.route('/', methods=["GET","POST"])
def inquery():  # put application's code here
    form=InqueryForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template("home.html", form=form, templates="form-template")



@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run()
