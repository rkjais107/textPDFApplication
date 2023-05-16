from flask import Flask, request
import os

app = Flask(__name__)

# Members API Route


@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return {"message": 'No file selected', "status_code": 400}

    file = request.files['file']
    file.save('D:\\MERN Completed Projects\\react-flask\\uploads\\' + file.filename)

    return {"message": 'File uploaded successfully', "status_code": 201}


@app.route('/delete', methods=['POST'])
def delete_file():
    print(request.form.get('fileName'))
    file_name = request.form.get('fileName')
    print(file_name)
    file_path = 'D:\\MERN Completed Projects\\react-flask\\uploads\\' + file_name
    print(file_path)
    if file_name and file_path:
        try:
            os.remove(file_path)
            return 'File deleted successfully'
        except OSError as e:
            return str(e)
    else:
        return 'File path not provided'


if __name__ == "__main__":
    app.run(debug=True)
