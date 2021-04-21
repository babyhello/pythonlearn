from urllib.request import urlopen
from PIL import Image

# manually create a directory photo
URL1 = "https://www.cwb.gov.tw/Data/satellite/FDK_IR1_CR_2750/FDK_IR1_CR_2750-2021-04-20-16-00.jpg"
fileToSave = urlopen(URL1)
image1 = Image.open(fileToSave)
image1.save("photo/orig.jpg")

halfsize = (image1.size[0] // 2, image1.size[1] // 2)
image2 = image1.resize(halfsize, Image.ANTIALIAS)
image2.save("photo/half.jpg")

image3 = image1.transpose(Image.ROTATE_90)
image3.save("photo/r90.jpg")

image4 = image1.transpose(Image.ROTATE_180)
image4.save("photo/r180.jpg")

image5 = image1.transpose(Image.ROTATE_270)
image5.save("photo/r270.jpg")
image6 = image1.rotate(60)
image6.save("photo/r60.jpg")