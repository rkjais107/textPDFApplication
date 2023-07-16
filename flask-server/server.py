from flask import Flask, request, jsonify
import os
import PyPDF2

uploads='F:\\ngnixServer\\textPDFApplication\\uploads\\'

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
    file.save(uploads + file.filename)

    return {"message": 'File uploaded successfully', "status_code": 201}


@app.route('/delete', methods=['POST'])
def delete_file():
    print(request.form.get('fileName'))
    file_name = request.form.get('fileName')
    print(file_name)
    file_path = uploads + file_name
    print(file_path)
    if file_name and file_path:
        try:
            os.remove(file_path)
            return 'File deleted successfully'
        except OSError as e:
            return str(e)
    else:
        return 'File path not provided'


@app.route('/read', methods=['POST'])
def read_pdf():
    print(request.form.get('fileName'))
    file_name = request.form.get('fileName')
    print(file_name)
    file_path = uploads + file_name
    print(file_path)
    if file_name and file_path:
        pdf_reader = PyPDF2.PdfReader(file_path)
        num_pages = len(pdf_reader.pages)

        # Read the contents of each page and concatenate them into a single string
        contents = ''
        for i in range(num_pages):
            page = pdf_reader.pages[i]
            contents += page.extract_text()

        # Return the contents as a JSON response
        return jsonify({'contents': contents})
    else:
        return 'File not provided'


if __name__ == "__main__":
    app.run(debug=True)
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=5000)
