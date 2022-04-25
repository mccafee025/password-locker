#!/usr/bin/python
import pyperclip
from credentials import User, Credential 

def create_user(fname,lname,password):
    new_user = User(fname,lname,password)
    return new_user
def save_user(user):
    User.save_user(user)

