from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

zimmetler = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_zimmet():
    data = request.json
    zimmetler.append(data)
    return jsonify({"message": "Zimmet başarıyla eklendi!", "zimmetler": zimmetler})

@app.route("/delete", methods=["POST"])
def delete_zimmet():
    index = request.json.get("index")
    if 0 <= index < len(zimmetler):
        deleted = zimmetler.pop(index)
        return jsonify({"message": f"{deleted['calisan_adi']} için zimmet silindi!", "zimmetler": zimmetler})
    return jsonify({"error": "Geçersiz indeks!"}), 400

if __name__ == "__main__":
    app.run(debug=True)
