from flaskblog import app

if __name__ == '__main__':
    app.run(threaded=True,port=int(os.getenv('PORT')))
