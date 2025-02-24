import dbConnect from './db';
import Course from './models/course';

export default async function handler(req, res) {
    if (req.method !== 'GET') {
        return res.status(405).json({ message: 'Method not allowed' });
    }

    try {
        await dbConnect();

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
                "accessibility": range,
                "enthusiasm": range,
                "encouragement": range,
            }
        };

        // Build query from request parameters
        const query = {};
        Object.entries(req.query).forEach(([key, value]) => {
            const [category, field] = key.split(".");
            if (filterMap[category] && filterMap[category][field]) {
                const filter = filterMap[category][field];
                Object.entries(filter).forEach(([op, template]) => {
                    const path = `${category}.${field}`;
                    if (op === 1) {
                        query[path] = { "$regex": value, "$options": "i" };
                    } else if (op === 2) {
                        query[path] = value;
                    } else if (op === 3) {
                        query[path] = { "$gt": Number(value) };
                    } else if (op === 4) {
                        query[path] = { "$lt": Number(value) };
                    }
                });
            }
        });

        // Query database
        const courses = await Course.find(query);
        res.status(200).json(courses);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Error querying courses' });
    }
}
