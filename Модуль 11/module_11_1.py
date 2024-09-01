from io import BytesIO

import requests
from PIL import Image


r = requests.get('https://cdn.futura-sciences.com/cdn-cgi/'
                 'image/width=1024,quality=60,format=auto/'
                 'sources/images/dossier/773/01-intro-773.jpg')
im_1 = Image.open(BytesIO(r.content))
im_1.save('image.jpg')
print(im_1.format, im_1.size, im_1.mode)
im_1.show()

im_2 = im_1.resize((400, 400))
im_2.save('image_2.jpg')
im_2.show()

im_3 = im_1.convert('L')
im_3.save('image_3.jpg')
im_3.show()
