from flask import Blueprint, render_template, request, redirect, url_for, flash

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def login():
    return 'Hello World'