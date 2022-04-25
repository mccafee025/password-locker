import unittest
import pyperclip
from user_credentials import User, Credential

class TestUser(unittest.TestCase):
	'''
	Test class that defines test cases for the user class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def setUp(self):
		'''
		Function to create a user account before each test
		'''
		self.new_user = User('Shawn','Kairigo','ndovukuu')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of user instances is properly done
		'''
		self.assertEqual(self.new_user.first_name,'Shawn')
		self.assertEqual(self.new_user.last_name,'Kairigo')
		self.assertEqual(self.new_user.password,'ndovukuu')

	def test_save_user(self):
		'''
		Test to check if the new users info is saved into the users list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('Shawn','Kairigo','ndovukuu')
		self.new_user.save_user()
		user2 = User('Shawn','Njogu','ndovukuu')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

	def setUp(self):
		'''
		allows us to show account info before making a test
		'''
		self.new_credential = Credential('Shawn','VSCO','son_of_elephant','ndovukuu')

	def test__init__(self):
		'''
		if creattion of info has been well executed
		'''
		self.assertEqual(self.new_credential.user_name,'Shawn')
		self.assertEqual(self.new_credential.site_name,'VSCO')
		self.assertEqual(self.new_credential.account_name,'son_of_elephant')
		self.assertEqual(self.new_credential.password,'ndovukuu')

	def test_save_credentials(self):
		'''
		if the info is saved in the created list
		'''
		self.new_credential.save_credentials()
		VSCO = Credential('Shawn','VSCO','son_of_elephant','ndovukuu')
		VSCO.save_credentials()
		self.assertEqual(len(Credential.credentials_list),2)



	def tearDown(self):
		'''
		Function to clear the credentials list after every test
		'''
		Credential.credentials_list = []
		User.users_list = []

	def test_display_credentials(self):
		'''
		Test to check if the display_credentials method, displays the correct credentials.
		'''
		self.new_credential.save_credentials()
		VSCO = Credential('Shawn','VSCO','son_of_elephant','ndovukuu')
		VSCO.save_credentials()
		gmail = Credential('Shawn','VSCO','son_of_elephant','ndovukuu')
		gmail.save_credentials()
		self.assertEqual(len(Credential.display_credentials(VSCO.user_name)),2)

	def test_find_by_site_name(self):
		'''
		checking if find site brings back what we want
		'''
		self.new_credential.save_credentials()
		VSCO = Credential('Shawn','VSCO','son_of_elephant','ndovukuu')
		VSCO.save_credentials()
		credential_exists = Credential.find_by_site_name('VSCO')
		self.assertEqual(credential_exists,VSCO)

	def test_copy_credential(self):
		'''
		investigation if we copy exactly what we want
		'''
		self.new_credential.save_credentials()
		VSCO = Credential('Shawn','VSCO','son_of_elephant','ndovukuu')
		VSCO.save_credentials()
		find_credential = None
		for credential in Credential.user_credentials_list:
				find_credential =Credential.find_by_site_name(credential.site_name)
				return pyperclip.copy(find_credential.password)
		Credential.copy_credential(self.new_credential.site_name)
		self.assertEqual('ndovukuu',pyperclip.paste())
		print(pyperclip.paste())

if __name__ == '__main__':
	unittest.main(verbosity=2)
