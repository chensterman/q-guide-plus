// Imports
require("dotenv").config({ path: "../.env" });
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors")

const app = express();
const uri = process.env.DB_URI;
const port = process.env.PORT || 5000;

// Middlewares
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Database connection
mongoose.connect(uri).then(() => console.log("Database connected.")).catch((e) => console.log(e));

// Route prefixes
app.use("/", require("./routes/routes"));

// Start server
app.listen(port, () => console.log("Server running at http://localhost:" + String(port) + "."));
