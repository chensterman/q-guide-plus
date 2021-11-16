// Imports
const express = require("express");
const api = require("../controllers/api")
const router = express.Router();

// Router paths
router.get("/", api.test);
router.get("/query", api.query)

// Export router
module.exports = router;