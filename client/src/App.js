import { useState } from "react";
import axios from "axios";

function App() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setSelectedFile(file);
  };

  const handleFileUpload = () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append("file", selectedFile);

      axios
        .post("/upload", formData)
        .then((response) => {
          console.log(response.data);
          // File uploaded successfully
        })
        .catch((error) => {
          console.error(error);
          // Handle error
        });
    }
  };
  return (
    <div className="App">
      <div className="flex flex-col items-center justify-center h-screen">
        <label
          htmlFor="file-input"
          className="mb-4 cursor-pointer bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
        >
          Select File
        </label>
        <input
          id="file-input"
          type="file"
          className="hidden"
          onChange={handleFileChange}
        />
        {selectedFile && (
          <div className="mt-4">
            <span className="font-bold">Selected File:</span>{" "}
            {selectedFile.name}
          </div>
        )}
        <button
          className="mt-4 bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded"
          onClick={handleFileUpload}
        >
          Upload File
        </button>
      </div>
    </div>
  );
}

export default App;
