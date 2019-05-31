from flask import Flask

app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    app.run(debug=True, port=8082,host='0.0.0.0')

# https://softwareengineering.stackexchange.com/questions/324730/mvc-and-restful-api-service

# https://www.google.com/search?q=mvc&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjy5YuCo8LiAhVHTd8KHWNHBRMQ_AUIDigB&biw=1536&bih=792#imgdii=gy2yKJtnHDG3UM:&imgrc=9Rjt4VneIKRggM:

# https://stackoverflow.com/questions/18872991/mvc-should-view-talk-with-model-directly