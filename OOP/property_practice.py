# practicing on instance property

from string import digits, ascii_lowercase, ascii_uppercase

with open(r'C:\Users\Назар\Favorites\Desktop\PYTHON\EGOROV_CHANNEL_YOUTUBE\OOP\Top304Thousand-probable-v2.txt', 'r') as password_file:
    deserialized_file = password_file.read()

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password            # Some features is here when the attribute becomes a property with descriptor getter
        self.__secret = 'Here is your Secret information'

    @property
    def secret(self):
        inp = input('Enter your password: ')
        if inp == self.password:
            return self.__secret
        raise ValueError('You password incorrect...')
    
    @staticmethod
    def password_in_file(password):
        if not password in deserialized_file:
            return True
        return False

    @staticmethod
    def digits_in_password(password):
        for digit in digits:
            if digit in password:
                return True
        return False
    
    @staticmethod
    def lowercase_letters_in_password(password):
        for small_letter in ascii_lowercase:
            if small_letter in password:
                return True
        return False
    
    @staticmethod
    def uppercase_letters_in_password(password):
        for big_letter in ascii_uppercase:
            if big_letter in password:
                return True
        return False

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('The password must be a string')
        
        if len(value) <= 4 or len(value) >= 12:
            raise ValueError('The length of password must be equal or grater than 4 symbols and equal or less than 12 symbols')
        
        if not User.digits_in_password(value) or not User.lowercase_letters_in_password(value) or not User.uppercase_letters_in_password(value):
            raise ValueError('The password must contain digits, lowercase letters and uppercase letters')
        
        if not User.password_in_file(value):
            raise ValueError('The password is too weak')

        self.__password = value

user = User('Ashley', 'a123123B')
print(user.password)
user.password = 'BIGsmall123'
print(user.password)
print(user.secret)
