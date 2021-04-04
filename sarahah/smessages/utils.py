from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw, ImageFont


def edit_photo(image,re):
    # m = Messages.objects.all()
    # for i in m :
    #     print(i.pic)
    i = Image.new('RGB', (2000, 1500), color = 'Black')
    im = Image.open(image)
    # print(im)
    img_draw = ImageDraw.Draw(i)
    myFont = ImageFont.truetype('arial.ttf', 40)
    img_draw.text((450, 50), 'Hi {received}\n I imagify you as '.format(received=re),font=myFont, fill='white')
    i.paste(im,(40, 200))
    img_draw.text((600, 1350), 'imagify.me ', font=myFont, fill='white')
    thumb_io = BytesIO()
    i= i.convert('RGB')
    i.save(thumb_io, 'JPEG', quality=85)  # save image to BytesIO object

    thumbnail = File(thumb_io, name=image.name)
    return thumbnail


    # print(pk)





