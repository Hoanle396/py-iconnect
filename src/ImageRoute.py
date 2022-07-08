import os
from flask import request ,send_file
from PIL import Image
from flask_cors import cross_origin 
import cv2
import numpy as np
def ImageRoute(app):
   @app.route('/api/image/resize',methods=['POST'])
   @cross_origin()
   def resizeImage():
      image=request.files['image']
      if image.filename!='':
         try:
            image.save('../data/image.png')
            img= Image.open('../data/image.png')
            (width, height) = img.size
            x = width if width < height else height
            y = height if height > width else width
            start=int((y-x)/2)
            box = (start,0 , (x+start), x) if width>height else(0,start,x,(x+start))
            imgc=img.crop(box)
            imgc.show()
            return send_file(path_or_file=imgc,mimetype='image/*'),200
         except Exception:
            import traceback 
            print(traceback.format_exc())
            return {'error':'error server'},500
      return {'error':'Bad request','message':'No Image'},400
