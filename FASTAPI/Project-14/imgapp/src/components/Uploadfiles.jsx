import React, { useState } from "react";
import axios from "axios";

const Uploadfiles = () => {
  const [file, setFile] = useState([]);
  const [message, setMessage] = useState("");

  const handleFileChange = (e) => {
    setFile([...e.target.files]);
  };

  const handleUpload = async () => {
    if (file.length === 0) {
      setMessage("Please select a file");
      return;
    }

    const formData = new FormData();

    file.forEach((f)=>{
      formData.append("files",f)
    })
    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }
      );

      setMessage("Upload successful ✅");
      console.log(res.data);

    } catch (err) {
      console.log(err);
      setMessage("Upload failed ❌");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: 50 }}>
      <h2>📤 Upload File</h2>

      <input type="file" multiple onChange={handleFileChange} />

      <br /><br />

      <button
        onClick={handleUpload}
        
        style={{
          padding: "10px 20px",
          background: "#007bff",
          color: "white",
          border: "none",
          borderRadius: 5,
          cursor: "pointer",
          
        }}
      >
        Upload
      </button>

      <p>{message}</p>
    </div>
  );
};

export default Uploadfiles;