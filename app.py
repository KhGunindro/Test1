from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        age = request.form.get("age")

        return f"""
        <h2>Registration Successful</h2>
        Name: {name} <br>
        Email: {email} <br>
        Age: {age}
        """

    return open("index.html").read()

if __name__ == "__main__":
    app.run()