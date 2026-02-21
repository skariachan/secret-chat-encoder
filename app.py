from flask import Flask, render_template, request
import coder
import decoder

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    encoded_text = ""
    decoded_text = ""

    if request.method == "POST":
        user_text = request.form["message"]

        if "encode" in request.form:
            encoded_text = coder.encode(user_text)   # we will call your function
        elif "decode" in request.form:
            decoded_text = decoder.decode(user_text)

    return render_template("index.html",
                           encoded=encoded_text,
                           decoded=decoded_text)

if __name__ == "__main__":
    app.run(debug=True)