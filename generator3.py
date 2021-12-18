#
#pip install myqr

from MyQR import myqr

'''
picture：Background picture
colorized：False black and white，True color
'''
myqr.run(words='https://google.com/',
         version=1,
         picture='bg.jpg',
         colorized=True,
         save_name='goole_myqr.png')
