from app import socketio, app


socketio.run(app,port=8080,host='0.0.0.0')
