import axios from "axios";
// EXTREMELY IMPORTANT CHANGE TO CORRECT PRODUCTION URL
const path = "http://localhost:8080/api/query";

export default class API {
    static async query(params) {
        const url = path + params;
        const res = await axios.get(url);
        return res.data;
    }
}