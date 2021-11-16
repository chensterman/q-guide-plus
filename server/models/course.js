// Imports
const mongoose = require("mongoose");

// Schema for course document
const courseSchema = mongoose.Schema({
    courseSummary: {
        catalog: String,
        title: String,
        instructor: String,
        department: String,
        term: String,
        url: String,
    },
    courseStat: {
        enrollment: Number,
        responses: Number,
        ratio: Number,
    },
    courseRating: {
        overall: Number,
        materials: Number,
        assignments: Number,
        feedback: Number,
        section: Number,
    },
    instructorRating: {
        overall: Number,
        lectures: Number,
        accessibility: Number,
        enthusiasm: Number,
        encouragement: Number,
        feedback: Number,
        returning: Number,
    },
    courseEval: {
        workload: Number,
        recommend: Number,
        sentiment: Number,
    },
})

// Export model
module.exports = mongoose.model("Course", courseSchema);