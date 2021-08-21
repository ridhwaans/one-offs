# PagerDuty API Exercise  

Ridhwaan S.  

This application contains the backend and frontend component that queries the PagerDuty API /users endpoint and displays its results  

Reference:  
https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1users/get  

Technologies used:  
- Nodejs 16  
- React 17  

## Instructions

1) Run `npm install` from the `client/` subdirectory, and also from the `server/` subdirectory  

2) Create a `.env` file in the `client/` directory, if it does not exist  
In `.env`, set the base url of the application server  
###### **`client/.env`**
```env
REACT_APP_SERVER_BASE = "http://localhost:5000"
```  

3) Create a `.env` file in the `server/` directory, if it does not exist  
In `.env`, set the API key and the base url of the client, for CORS/proxy request purposes  
###### **`server/.env`**
```env
PAGERDUTY_API_KEY = 'y_NbAkKc66ryYTWUXYEu'
CLIENT_BASE_URL = 'http://localhost:3000'
```

4) By default, the client port is `3000` and the server port is `5000`  

5) Open the browser and go to `http://localhost:3000/users`  

6) The plain API response is available at `http://localhost:5000/api/users`  