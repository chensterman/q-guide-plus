// Imports
const course = require("../models/course");

// Class with request functions
module.exports = class API {
    static async test(req, res) {
        res.send("API Test");
    }

    // Querying API function
    static async query(req, res) {
        const regex = {1: [".*", "."]};
        const text = {2: ""};
        const range = {
            "min": {3: {"$gt": ""}},
            "max": {4: {"$lt": ""}},
        };
        const filterMap = {
            "cs": {
                "c": regex,
                "t": regex,
                "i": regex,
                "d": text,
                "te": text,
            },
            "cst": {
                "e": range,
                "r": range,
            },
            "cr": {
                "o": range,
                "m": range,
                "a": range,
                "f": range,
                "s": range,
            },
            "ir": {
                "o": range,
                "l": range,
                "a": range,
                "e": range,
                "en": range,
                "f": range,
                "r": range,
            },
            "ce": {
                "w": range,
                "r": range,
                "s": range,
            },
        };
        // Initialize empty list for $and query combination
        const query = [];

        // Get query parameters from URL and loop through them
        const params = req.query;
        for (const param in params) {
            var querySingle;
            const paramArray = param.split(".");
            for (const str in paramArray) {
                querySingle = filterMap[str];
            };
            if (1 in querySingle) {
                const regexStr = querySingle[1][0] + params[param] + querySingle[1][1];
                querySingle = {param: {"$regex": regexStr, "$options": "i"}};
                query.push(querySingle);
            }
            else if (2 in querySingle) {
                querySingle[2] = params[param];
                querySingle = {param: querySingle[2]};
                query.push(querySingle);
            }
            else if (3 in querySingle) {
                querySingle = querySingle[3];
                querySingle["$gt"] = params[param];
                const field = paramArray[0] + "." + paramArray[1];
                querySingle = {field: querySingle};
                query.push(querySingle);
            }
            else if (4 in querySingle) {
                querySingle = querySingle[4];
                querySingle["$lt"] = params[param];
                const field = paramArray[0] + "." + paramArray[1];
                querySingle = {field: querySingle};
                query.push(querySingle);
            }
        };
        try {
            // Make the final query
            const courses = await course.find({"$and": query});
            res.status(200).send(courses);
        } catch(e) {
            res.status(400).json({ message: e.message} );
        }
    }
}