from flask import Flask, render_template,abort, make_response,request, redirect, url_for, send_from_directory
import matplotlib.pyplot as plt
import numpy as np

app=Flask(__name__, static_url_path='')

@app.route('/sign in')
def signIn():
    return render_template('signIn.html')

@app.route('/post', methods=['POST'])
def post():
    X=request.form['x']
    X1=list(X.replace(',',''))
    print(X)
    print(X1)
    print(type(X1))
    X2=np.array(X1).astype(int)
    print(X2)
    print(type(X2))
    Y=request.form['y']
    Y1=list(Y.replace(',',''))
    Y2=np.array(Y1).astype(int)
    plt.close()
    plt.bar(X2,Y2)
    plt.savefig('images/grafik.png')
    # file='grafik.png'
    return render_template('grafik.html')

@app.route('/images/<path:x>')
def load(x):
    return send_from_directory('images',x)

@app.errorhandler(404)
def notfound(error):
    return '<h1>Error: 404 Not Found!</h1>'

if __name__ == '__main__':
    app.run(debug=True)