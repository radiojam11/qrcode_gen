#
#pip install myqr

from MyQR import myqr

'''
words：content
version：error rates, from 1 to 40
save_name：保存的名字
'''
myqr.run(words='https://google.com/',
         version=1,
         save_name='google_myqr.png')
