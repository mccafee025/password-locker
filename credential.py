import random
import pyperclip
import string

global users_list
class User:
    users_list = []
	def __init__(self,first_name,last_name,password):
		self.first_name = first_name
		self.last_name = last_name
		self.password = password
	def save_user(self):
		User.users_list.append(self)

class Credential:
	credentials_list =[]
	user_credentials_list = []
	@classmethod
