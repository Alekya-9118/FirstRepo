import pandas as pd
from PIL import Image, ImageFont, ImageDraw







#covert from RGBA to RGB 
import PIL.Image
rgba_image = PIL.Image.open('C:\\Users\\alekh\\Downloads\\aavega certificate.png')
rgb_image = rgba_image.convert('RGB')
rgb_image.save('C:\\Users\\alekh\\Downloads\\aavega certificate1.png')







#font setting
# data = pd.read_csv('C:\\Users\\manoj\\Downloads\\spardha.csv')
# fnt = ImageFont.truetype('times.ttf', 79)
# fnt1 = ImageFont.truetype('times.ttf', 77)
# fnt2 = ImageFont.truetype('times.ttf', 83)
# fnt3 = ImageFont.truetype('times.ttf', 95)for different sized names


# fnt4 = ImageFont.truetype('times.ttf', 87)
# fnt5 = ImageFont.truetype('times.ttf', 48)
# data = data.reset_index()
font = ImageFont.truetype('C:\\Users\\alekh\Downloads\\vollkorn\\Vollkorn-Regular.ttf',150)
print("1")





#open an image
#for index, row in data.iterrows():
img = Image.open('C:\\Users\\alekh\\Downloads\\aavega certificate1.png')
print(2)






#code for dynamic name start point adjustment
d = ImageDraw.Draw(img)
print(3)
# sss='V.Jyothsna'
# d.text((977+((25-len(sss))*25),917),sss , font=fnt, fill=(0,0,0))
# d.text((300+(35*(31-len(str(row['name'])))),920-(2*(31-len(str(row['name']))))),str(row['name']), font=ImageFont.truetype('D:\\all files\\programming practice\\my py practice\\Vollkorn-Regular.ttf',150+(1*(31-len(str(row['name']))))), fill=(0,0,0))
d.text((781,601),"Manoj", font=ImageFont.truetype('C:\\Users\\alekh\Downloads\\vollkorn\\Vollkorn-Regular.ttf',150), fill=(0,0,0))
print(4)

img.save('C:\\Users\\alekh\Downloads\\vollkorn\\'+"Manoj"+'.pdf')
print('done')
# img.show()





# Iterate thorugh rows in CSV and print on certificates
#
#
# for index, row in data.iterrows():
#     img = Image.open('C:\\Users\\manoj\\Downloads\\certificate8.png')
#     d = ImageDraw.Draw(img)
#     if(len(str(row['name']))>20):
#         d.text((1400,860),str(row['name']) , font=fnt, fill=(0,0,0))
#     else:
#         d.text((1500,860),str(row['name']) , font=fnt, fill=(0,0,0))
#     d.text((573,993), 'Vasireddy Venkatadri Institute of Technology Nambur', font=fnt, fill=(0,0,0))
#     if(str(row['cor'])=='Machine Learning'):
#         d.text((2175,1140), str(row['cor']), font=fnt2, fill=(0,0,0))
#         d.text((1252,1276), str(row['s']), font=fnt1, fill=(0,0,0))
#         d.text((1611,1270), str(row['e']), font=fnt2, fill=(0,0,0))
#     elif(str(row['cor'])=='Advanced Python'):
#         d.text((2175,1140), str(row['cor']), font=fnt2, fill=(0,0,0))
#         d.text((1311,1255), str(row['s']), font=fnt3, fill=(0,0,0))
#         d.text((1670,1255), str(row['e']), font=fnt3, fill=(0,0,0))
#     # else:
#     #     d.text((2136,1140), str(row['cor']), font=fnt, fill=(0,0,0))
#     #     d.text((1311,1260), str(row['s']), font=fnt3, fill=(0,0,0))
#     #     d.text((1635,1265), str(row['e']), font=fnt4, fill=(0,0,0))
#     img.save('D:\\cer1\\'+str(row["name"])+'_'+str(row["cor"])+'.pdf')
# print('done')