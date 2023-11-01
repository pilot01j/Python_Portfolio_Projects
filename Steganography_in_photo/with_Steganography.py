import steganocryptopy

from steganocryptopy.steganography import Steganography

Steganography.generate_key('')
secret = Steganography.encrypt('key.key', 'img/3.jpeg', 'secret_message.txt')
secret.save('img/3_secret.jpeg')

result = Steganography.decrypt('key.key', 'img/3_secret.jpeg')
print(result)
