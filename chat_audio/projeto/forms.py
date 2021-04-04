from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormularioCadastro(FlaskForm):     
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    confirmar_email = StringField('Confirmar Email', validators=[DataRequired(),  EqualTo('email')])

    senha = PasswordField('Senha', validators=[DataRequired()])
    
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(),  EqualTo('senha')])
                        
    submit = SubmitField('Cadastrar')

class FormularioLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    senha = PasswordField('Senha', validators=[DataRequired()])
    
    lembrar = BooleanField('Lembrar Senha')               

    submit = SubmitField('Login')