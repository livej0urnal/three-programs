import pyAesCrypt

password = input('Enter password to crypto: ')
#encrypt
pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)