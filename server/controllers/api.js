// Imports
const course = require("../models/course");

// Class with request functions
module.exports = class API {
    static async test(req, res) {
        res.send("API Test");
    }

    // Querying API function
    static async query(req, res) {
        try {
            // Define query parameter mappings
            const regex = {1: ""};
            const text = {2: ""};
            const range = {
                "min": {3: {"$gt": ""}},
                "max": {4: {"$lt": ""}},
            };
            const filterMap = {
                "courseSummary": {
                    "catalog": regex,
                    "title": regex,
                    "instructor": regex,
                    "department": text,
                    "term": text,
                },
                "courseStat": {
                    "enrollment": range,
                    "responses": range,
                },
                "courseRating": {
                    "overall": range,
                    "materials": range,
                    "assignments": range,
                    "feedback": range,
                    "section": range,
                },
                "instructorRating": {
                    "overall": range,
                    "lectures": range,
                    "accessability": range,
                    "enthusiasm": range,
                    "encouragement": range,
                    "feedback": range,
                    "returning": range,
                },
                "courseEval": {
                    "workload": range,
                    "recommend": range,
                    "sentiment": range,
                },
            };
            // Initialize empty list for $and query combination
            const query = [];

            // Get query parameters from URL and loop through them
            const params = req.query;
            for (const param in params) {
                var querySingle = filterMap;
                // Split parameter into map keys and find the resulting dictionary
                const paramArray = param.split(".");
                paramArray.forEach((s) => querySingle = querySingle[s]);
                // Check for each case
                if (1 in querySingle) {
                    querySingle = {};
                    querySingle[param] = {"$regex": params[param], "$options": "i"};
                    query.push(querySingle);
                }
                else if (2 in querySingle) {
                    querySingle = {};
                    querySingle[param] = params[param];
                    query.push(querySingle);
                }
                else if (3 in querySingle) {
                    querySingle = querySingle[3];
                    querySingle["$gt"] = params[param];
                    const field = paramArray[0] + "." + paramArray[1];
                    const tmp = querySingle;
                    querySingle = {};
                    querySingle[field] = tmp;
                    query.push(querySingle);
                }
                else if (4 in querySingle) {
                    querySingle = querySingle[4];
                    querySingle["$lt"] = params[param];
                    const field = paramArray[0] + "." + paramArray[1];
                    const tmp = querySingle;
                    querySingle = {};
                    querySingle[field] = tmp;
                    query.push(querySingle);
                }
            };
            // Make the final query (and $and of all the given queries)
            const courses = await course.find({"$and": query}, null, {
                "sort": {
                    "courseSummary.catalog": 1 //Sort by Date Added DESC
                }
            });
            res.status(200).send(courses);
        } catch(e) {
            res.status(400).json({ message: e.message} );
        }
    }
}