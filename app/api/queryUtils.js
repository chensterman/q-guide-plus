/**
 * Utility functions for building MongoDB queries from request parameters.
 * Extracted from query.js to enable unit testing.
 */

/**
 * Filter type definitions matching the original query.js structure.
 */
const regex = { 1: "" };
const text = { 2: "" };
const range = {
    "min": { 3: { "$gt": "" } },
    "max": { 4: { "$lt": "" } },
};

/**
 * Filter map defining how different fields should be queried.
 * Keys: 1 = regex, 2 = exact text, 3 = greater than, 4 = less than
 */
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
        "accessibility": range,
        "enthusiasm": range,
        "encouragement": range,
    }
};

/**
 * Build a MongoDB query object from request query parameters.
 * Matches the logic in query.js handler.
 * 
 * @param {Object} queryParams - The request query parameters
 * @returns {Object} MongoDB query object
 */
function buildQuery(queryParams) {
    const query = {};
    
    Object.entries(queryParams).forEach(([key, value]) => {
        const [category, field] = key.split(".");
        if (filterMap[category] && filterMap[category][field]) {
            const filter = filterMap[category][field];
            Object.entries(filter).forEach(([op, template]) => {
                const path = `${category}.${field}`;
                if (op == 1) {
                    query[path] = { "$regex": value, "$options": "i" };
                } else if (op == 2) {
                    query[path] = value;
                } else if (op == 3) {
                    query[path] = { "$gt": Number(value) };
                } else if (op == 4) {
                    query[path] = { "$lt": Number(value) };
                }
            });
        }
    });
    
    return query;
}

/**
 * Validate that a request method is GET.
 * 
 * @param {string} method - The HTTP method
 * @returns {boolean} True if method is GET
 */
function isValidMethod(method) {
    return method === 'GET';
}

/**
 * Get the filter map configuration.
 * 
 * @returns {Object} The filter map
 */
function getFilterMap() {
    return filterMap;
}

module.exports = {
    buildQuery,
    isValidMethod,
    getFilterMap,
    filterMap
};
