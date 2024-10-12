from flask import Flask,render_template,send_from_directory

app = Flask(__name__)

@app.route("/")
def home():

      return render_template("index.html")
@app.route("/download-cv")
def download():

    return send_from_directory('static/doc',"blue professional modern CV resume (2).pdf")
if __name__ == '__main__':
  app.run( debug = True )
