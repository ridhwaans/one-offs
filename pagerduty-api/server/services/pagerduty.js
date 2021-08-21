const axios = require('axios');
const qs = require('qs');
const Cookies  = require('universal-cookie');

const PAGERDUTY_API = 'api.pagerduty.com'
const wait = ms => new Promise(resolve => setTimeout(resolve, ms));
const cookies = new Cookies();

class PagerDutyClient {
    constructor () {} 

    async getUsers(delay=0, item = null) {
      let request_url = `https://${PAGERDUTY_API}/users`

      return wait(delay).then(() => axios.get(request_url, {
        headers: {
          'Authorization': "Token token=" + process.env.PAGERDUTY_API_KEY
        }
        })
        .then((response) => {
          return response.data
        })
        .catch((error) => {
          return error.response
        })
      )
    }
}

/**
 * OAuth function i.e. Spotify Authorization Flow
 * usage example:
 * let auth = await getAuth() // authorization header
 * let request_url = `https://${SPOTIFY_API}/albums/${item.id}?access_token=${auth}`
*/
const getAuth = async () => {
  let auth = cookies.get("auth")

  if (!auth) {
      await getAuthorizationToken()
      auth = cookies.get("auth")
  }

  return auth;
}

async function getAuthorizationToken() {
  return axios
    .post(
      "https://accounts.spotify.com/api/token",
      qs.stringify({
        grant_type: "client_credentials",
        client_id: process.env.SPOTIFY_CLIENT_ID,
        client_secret: process.env.SPOTIFY_CLIENT_SECRET,
      }),
      {
          headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          },
      }
    )
    .then(function (response) {
      cookies.set("auth", response.data.access_token, {
        maxAge: response.data.expires_in,
      });
  });
}

module.exports = PagerDutyClient