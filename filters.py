from PIL import Image

def load_img(name):
    name = Image.open(filename)
    return name
    
def show_img(name):
    name.show(filename)
    
def save_img(name_variable, filename):
    name_variable.save(name_variable, "jpeg")
    show_img(name_variable) 

def abomicon(filename, new_image):
    filename = image.getdata(band = none)
    new_image=[]
    for pixel in image:
        pixel_intensity = pixel[0] + pixel[1] + pixel[2]
        if(pixel_intensity < 182):
            new_image[pixel] = (0,51, 76)
        elif(pixel_intensity >= 182 and <=364):
            new_image[pixel] = (217,26,33)
        elif(pixel_intensity >= 364 and <= 546):
            new_image[pixel] = (112, 150,158)
        elif(pixel_intensity >= 546):
            new_image[pixel] = (252, 227, 166)
    newest_im = PIL.filename.new("RGB", (1000, 1000))
    return newest_im