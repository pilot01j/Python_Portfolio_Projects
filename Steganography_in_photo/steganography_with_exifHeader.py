from stegano import exifHeader

# 1. call the hide func from exifHeader direct , and send as param .the picture location, the picture with secret and secret message
secret = exifHeader.hide('img/2.jpg', 'img/2_secret.jpg', 'You second pasword: Cluj4578!')
result = exifHeader.reveal('img/2_secret.jpg')
result = result.decode()
print(result)
