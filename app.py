from flaskblog import app
import os

if __name__ == '__main__':
    app.run(threaded=True,port=int(os.getenv('PORT')))
