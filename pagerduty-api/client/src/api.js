import axios from "axios"

export async function getUsers(params = {}) {

    return await axios.get(`${process.env.REACT_APP_SERVER_BASE}/api/users`)
        .then(function (response) {
            return response

        })
}