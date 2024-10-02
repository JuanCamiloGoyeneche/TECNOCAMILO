from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route('/') 
def home():
    return render_template ('index.html')

@app.route('/contacto', methods=['POST'])
def contacto():
    if request.method == 'POST':
        nam = request.form['nombre']
        emm = request.form['email']
    return render_template ('mensaje.html', res=nam, ress=emm)


if __name__ == '__main__':
    app.run()

