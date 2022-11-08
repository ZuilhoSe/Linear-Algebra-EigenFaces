import os
from PIL import Image


#Paths to the images
train_cat = "cat2dog/trainA"
train_dog = "cat2dog/trainB"
test_cat = "cat2dog/testA"
test_dog = "cat2dog/testB"  
test = 'test/'

basewidth = 64
img = Image.open('cat2dog/testA/13.jpg')
wpercent = (basewidth / float(img.size[0]))
hsize = 64
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save('resized_image.jpg')

for image in (os.listdir(test_cat)): 
    path = os.path.join(test_cat, image)
    img = Image.open(path)
    wpercent = (basewidth / float(img.size[0]))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(f'cat2dog_resized/test_cats/{image}')

for image in (os.listdir(test_dog)): 
    path = os.path.join(test_dog, image)
    img = Image.open(path)
    wpercent = (basewidth / float(img.size[0]))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(f'cat2dog_resized/test_dogs/{image}')

for image in (os.listdir(train_cat)):
    path = os.path.join(train_cat, image)
    img = Image.open(path)
    wpercent = (basewidth / float(img.size[0]))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(f'cat2dog_resized/train_cats/{image}')

for image in (os.listdir(train_dog)):
    path = os.path.join(train_dog, image)
    img = Image.open(path)
    wpercent = (basewidth / float(img.size[0]))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(f'cat2dog_resized/train_dogs/{image}')

for image in (os.listdir(test)): 
    path = os.path.join(test, image)
    img = Image.open(path)
    wpercent = (basewidth / float(img.size[0]))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(f'test/resize/{image}')