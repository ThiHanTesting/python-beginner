from urllib.request import urlretrieve

link = input('image download link : ')

fileName = input('file name : ')

urlretrieve(link,'C:/Users/Khun Thi Han/Desktop/python/Beginning/image/'+fileName+'.jpg')
