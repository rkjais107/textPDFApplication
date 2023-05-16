from flask import Flask, request

app = Flask(__name__)

# Members API Route


@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file selected', 400

    file = request.files['file']
    file.save('D:\\MERN Completed Projects\\react-flask\\uploads\\' + file.filename)

    return 'File uploaded successfully'


if __name__ == "__main__":
    app.run(debug=True)
