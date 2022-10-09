import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import cv2
import numpy as np
import base64


cred=credentials.Certificate('<Path to Certificate .json>')

firebase_admin.initialize_app(cred,{
    'databaseURL':'<url to firebase.io>'

})
'''ref=db.reference('/Emp')

s=ref.get()

print(s)'''


ref=db.reference('/Images')

prev=0

ones=np.ones((640,480))
cv2.imshow('x',ones)
while True:
    last_record = ref.order_by_key().limit_to_last(1).get()

    #print(last_record.values())
    if last_record ==None:
        continue

    k=last_record.keys()
    print('key',k)

    k_press=cv2.waitKey(1)
    if k_press==ord('q'):
        break

    if k!=prev:
        prev=k
        x="".join(last_record.values())

        x=str(x[2:-1])
        #print(x)
        b=bytes(x,'utf8')

        im_bytes = base64.b64decode(b)
        im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
        img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)


        print(type(img))

        cv2.imshow('x',img)
        #cv2.waitKey(0)

cv2.destroyAllWindows()