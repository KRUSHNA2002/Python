
import React from 'react'
import { useEffect, useState } from "react";
import axios from "axios";

const ShowFile = () => {
      const [files, setFiles] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/images")
      .then(res => setFiles(res.data));
  }, []);

  return (
    <div style={{ padding: 20, textAlign: "center" }}>
      <h1>📁 File Manager</h1>

      <table style={{
        width: "80%",
        margin: "auto",
        borderCollapse: "collapse"
      }}>
        <thead>
          <tr style={{ background: "#007bff", color: "white" }}>
            <th style={th}>ID</th>
            <th style={th}>Filename</th>
            <th style={th}>Type</th>
            <th style={th}>Action</th>
          </tr>
        </thead>

        <tbody>
          {files.map(file => (
            <tr key={file.id} style={{ borderBottom: "1px solid #ddd" }}>
              
              <td style={td}>{file.id}</td>
              <td style={td}>{file.filename}</td>
              <td style={td}>{file.content_type}</td>

              <td style={td}>
                <a
                  href={`http://127.0.0.1:8000/file/${file.id}`}
                  target="_blank"
                  style={{
                    padding: "6px 12px",
                    background: "#28a745",
                    color: "white",
                    borderRadius: 5,
                    textDecoration: "none"
                  }}
                >
                  View
                </a>
              </td>

            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

const th = {
  padding: 10,
  border: "1px solid #ddd"
};

const td = {
  padding: 10,
  border: "1px solid #ddd"
};
export default ShowFile