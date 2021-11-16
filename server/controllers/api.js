// Imports
const course = require("../models/course");

// Class with request functions
module.exports = class API {
    static async test(req, res) {
        res.send("API Test");
    }

    // Querying API function
    static async query(req, res) {
        // Initialize empty query
        const matches = {};

        // Get query parameters from URL and loop through them
        const query = req.query;
        for (const key in query) {
            // For each matching parameter add the corresponding query to matches
            if (key.startsWith("courseSummary")) {
                matches[key] = query[key];
            }
            else if (key.startsWith("courseRating")) {
                matches[key] = {"$gt": query[key]};
            }
            else if (key.startsWith("instructorRating")) {
                matches[key] = {"$gt": query[key]};
            }
            else if (key.startsWith("courseEval.workload")) {
                matches[key] = {"$lt": query[key]};
            }
            else if (key.startsWith("courseEval")) {
                matches[key] = {"$gt": query[key]};
            }
        }
        try {
            // Make the final query
            const courses = await course.find(matches);
            res.status(200).send(courses);
        } catch(e) {
            res.status(400).json({ message: e.message} );
        }
    }
}