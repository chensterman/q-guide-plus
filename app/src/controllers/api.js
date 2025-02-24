import axios from "axios";
// EXTREMELY IMPORTANT CHANGE TO CORRECT PRODUCTION URL
const path = "https://qguideplus.vercel.app/api/query";

export default class API {
    static async query(params) {
        const url = path + params;
        const res = await axios.get(url);
        return res.data;
    }
}