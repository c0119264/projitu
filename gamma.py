import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("ea7the.jpg",0)

def rectify(img,gamma):
    img = 255 * (img/255)**(1/ gamma)
    img = np.clip(img,0,255).astype(np.uint8)
    return img


    
fig= plt.figure(figsize=(10,2.5))
out = rectify(img,gamma=0.4)
ax=fig.add_subplot(1,1,1)
ax.imshow(out)
ax.axis("off")
ax.set_title("gamma={:.2f}".format(0.4))
cv2.imwrite("number222.jpg",out)
plt.show()    

