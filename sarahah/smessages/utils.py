from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw, ImageFont


def edit_photo(image,re):

    i = Image.new('RGB', (600, 750), color = 'black')
    im = Image.open(image)
    
    img_draw = ImageDraw.Draw(i)

    # Ffont = ImageFont.truetype('FreeMonoBold.ttf', 40)
    img_draw.text((10,80),'Anonymous\n',font=ImageFont.truetype('arial.ttf', 42), fill='skyblue')
    myFont = ImageFont.truetype('arial.ttf', 25)
    img_draw.text((10, 145), 'Hi {received},\nI imagify you as'.format(received=re),font=myFont, fill='white')
    i.paste(im,(100, 225))
    img_draw.text((225, 630), 'www.imagify.me ', font=myFont, fill='white')
    thumb_io = BytesIO()
    i= i.convert('RGB')
    i.save(thumb_io, 'JPEG', quality=85) 

    thumbnail = File(thumb_io, name=image.name)
    return thumbnail


    # print(pk)

def compressImage(uploadedImage):
    imageTemproary = Image.open(uploadedImage)
    outputIoStream = BytesIO()
    imageTemproary = imageTemproary.convert('RGB')
    imageTemproaryResized = imageTemproary.resize((400, 400))
    imageTemproary.save(outputIoStream, format='JPEG', quality=60)
    outputIoStream.seek(0)
    uploadedImage = File(outputIoStream, name=uploadedImage.name)
    return uploadedImage



