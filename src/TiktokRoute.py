from flask import jsonify, request, send_file,make_response
from flask_cors import cross_origin
from TikTok.Tiktok import Tiktok
import json
import pandas as pd
def TiktokRoute(app):
   @app.route("/api/tiktok/username",methods=['POST'])
   @cross_origin()
   def nsertUser():
      username=request.json['username']
      if username!='':
         try:
            data=username
            df=pd.DataFrame(data)
            df.to_csv(path_or_buf='../data/username.csv', sep='\t', index=None,mode='w', encoding='utf-8', header=None)
            return {"status":"OK" ,"message":"Successfuly!"},200
         except Exception:
            return {"status":"Server error" ,"message":"Server Err"},500
      return {"status":"BadRequest" ,"message":"No data username!"},400
   @app.route("/api/tiktok/getusername", methods=["POST"])
   @cross_origin()
   def getLikesByUser():
      username=request.form['username']
      if username != '':
         Api = Tiktok()
         print(username)
         data = Api.scrap(username=username,browser_name="Chrome")
         if data!=False:
            return make_response(jsonify(json.loads(data))),200 
         else:return make_response(jsonify({'error':'not found user by username'}),400)
      return make_response(jsonify({"status":"Bad request","data":"Error to load username", "code":400}),400)
   @app.route('/api/tiktok/trend',methods=['GET'])
   @cross_origin()
   def getTrend():
      api=Tiktok()
      data= api.Trend("chrome")
      if data!=False:
         return make_response(jsonify(json.loads(data))),200 
      else:return make_response(jsonify({'error':'Crawl data false'}),400)