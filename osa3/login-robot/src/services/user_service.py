import pdb
import sys
from entities.user import User
import re


class UserInputError(Exception):
    pass

class PasswordInputError(Exception):
    pass
class UserError(Exception):
    pass
class AuthenticationError(Exception):
    pass


class UserService:
   
    def __init__(self, user_repository):
        self._user_repository = user_repository


    def check_credentials(self, username, password):
        #pdb.Pdb(stdout=sys.__stdout__).set_trace()
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        # Validoi käyttäjänimi ja salasana
        self.validate(username, password)

        # Luo käyttäjä, jos validointi meni läpi
        user = self._user_repository.create(User(username, password))
        return user
            

    
    def delete_all_users(self):
        self._user_repository.delete_all()
        return

    def validate(self, username, password):

        if self._user_repository.find_by_username(username):
            raise UserError("UserError: Username already exists!")
        

        # Tarkista, että käyttäjänimi ja salasana eivät ole tyhjiä
        if not username or not password:
            raise UserInputError("Username and password are required")

        # Käyttäjänimen validointi: vähintään 3 kirjainta, a–z
        if not re.match(r"^[a-z]{3,}$", username):
            raise UserInputError("Username must be at least 3 characters and contain only letters a-z")

        # Salasanan validointi: vähintään yksi muu merkki kuin kirjain
        if re.match(r"^[a-zA-Z]+$", password):
            raise UserInputError("Password must include characters other than letters")

        # Salasanan pituus: vähintään 8 merkkiä
        if len(password) < 8:
            raise PasswordInputError("Password is too short!")
        

        
