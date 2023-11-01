from stegano import lsb

# 1. call the hide func from lsb direct , and send as parameter the picture location and secret message
secret = lsb.hide('img/1.png', 'You password: pilot01j')
secret.save('img/1_secret.png')

result = lsb.reveal('img/1_secret.png')
print(result)


