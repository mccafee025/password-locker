#!/usr/bin/python
import pyperclip
from credentials import User, Credential 

def create_user(fname,lname,password):
    new_user = User(fname,lname,password)
    return new_user
def save_user(user):
    User.save_user(user)
def verify_user(first_name,password):
    checking_user = Credential.check_user(first_name,password)
    return checking_user
def generate_password():
    gen_pass = Credential.generate_password()
    return gen_pass
def create_credential(user_name,site_name,account_name,password):
    new_credential=Credential(user_name,site_name,account_name,password)
    return new_credential
def save_credential(credential):
    Credential.save_credentials(credential)
def display_credentials(user_name):
    return Credential.display_credentials(user_name)


