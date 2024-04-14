from PIL import Image

image = Image.open('image.png')
image = image.convert('RGB')
image.save('new_img.jpg', quality=30)