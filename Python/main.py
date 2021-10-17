from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route("/", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        passwd = request.form['passwd']
        return redirect(url_for("name", name = user, passwd = passwd))
    elif request.method == 'GET':
        message = "Hello folks"
        return render_template('index.html', message = message)
    else:
        message = "Enter correct password"
        return render_template('index.html', message = message)




@app.route('/name', methods = ['GET', 'POST'])
def name():
    name = request.form.get('name')
    passwd = request.form.get('passwd')
    return render_template('name.html', message = f"hello {name} your password is {passwd}")


if __name__ == '__main__':
    app.run(debug=True)