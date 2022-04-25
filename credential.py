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
    def check_user(cls,first_name,password):
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

    def __init__(self,user_name,site_name,account_name,password):
		self.user_name = user_name
		self.site_name = site_name
		self.account_name = account_name
		self.password = password
    def save_credentials(self):
		Credential.credentials_list.append(self)
