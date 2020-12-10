from flask import Flask, render_template, request, redirect


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sendmsg", methods=['POST'])
def sendmsg():
    number = request.form['phone']
    if (len(number) > 12) or (len(number) <= 10):
        error = "Invalid Format, Format: 91948111xxxx"
        return render_template("index.html", error=error)
    else:
        url = "https://wa.me/"+number
        return redirect(url)




if __name__ == "__main__":
    app.run(debug=True)
