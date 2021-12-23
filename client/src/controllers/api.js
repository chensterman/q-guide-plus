import axios from "axios";
// EXTREMELY IMPORTANT CHANGE TO CORRECT PRODUCTION URL
const path = "https://secret-basin-84820.herokuapp.com/api/query";

export default class API {
    static async query(params) {
        const url = path + params;
        const res = await axios.get(url);
        return res.data;
    }
}