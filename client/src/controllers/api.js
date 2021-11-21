import axios from "axios";
const path = "http://localhost:5000/query";

export default class API {
    static async query(params) {
        const url = path + params;
        const res = await axios.get(url);
        return res.data;
    }
}