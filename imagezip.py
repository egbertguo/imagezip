from PIL import Image

class IMAGE:
    def __init__(self):
        pass
    def zipfun(self,image_tmp,longth,width):
        im = Image.open(image_tmp)
        print(im.format, im.size, im.mode)
        im.thumbnail((longth, width))
        im.save('new_image/'+image_tmp, 'JPEG')
        
myim = IMAGE()
myim.zipfun("image/308129.jpg", 300, 200)