const express = require("express");
const path = require("path");
const upload = require("express-fileupload");
const fs = require('fs')
const app = express();
const port = process.env.PORT || "5001";

app.use(upload());

// HTTP route handlers
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, '/index.html'));
  });

app.post("/upload", (req, res) => {
    if (!req.files) {
        res.status(400).send("No file submitted");
    } else {
        file = req.files.img;
        console.log(`Received ${file.name} with size ${file.size} bytes`);
        if (file.size > 10000000) {
            // ensure that file is not too large (10 MB)
            res.status(413).send("File is too large (must be less than 10 MB)");
        } else if (file.mimetype != 'image/png') {
            // ensure that file has correct MIME type
            res.status(415).send("Unsupported file type. Please upload your file as a .PNG")
        } else {
            out = __dirname + '/test/' + file.name.slice(0,-4) 
            out_ = out
            i = 1
            while (fs.existsSync(out_ + '.png')) {
                out_ = out + `(${i})`
                i = i + 1
            }
            file.mv(out_ + '.png');
            res.status(200).send("OK");
        }
    }
});

// start the server
app.listen(port, () => console.log(`Server started on port ${port}`));
