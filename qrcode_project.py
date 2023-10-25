import qrcode
#data to encode, can be an url, link to download an app in apple store/google playstore
data = input("Enter the data:  ")

#Each version has a different module configuration or number of modules. (The module refers to the black and white dots that make up QR Code.) 
version = int(input("Enter the version (complexity):  ")) #max 15
box_size = int(input("Enter the box size:  ")) #max 10

#creating an instance of QRCode class
qr= qrcode.QRCode(version, box_size, border=5)

#Adding data to the instance 'qr'
qr.add_data(data)
img = qr.make_image(fill_color = 'black', back_color='white')

f=input("Name it as: ") #image name

img.save(f'{f}.png')

print("qr code generated and save in the gallery")

