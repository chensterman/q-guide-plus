import axios from "axios";
const path = "/query";

export default class API {
    static async query(params) {
        const url = path + params;
        const res = await axios.get(url);
        return res.data;
    }
}