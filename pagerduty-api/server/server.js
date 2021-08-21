const path = require('path')
const express = require('express')
const bodyParser = require('body-parser');

const app = express();
const port = process.env.PORT || 5000;
require('dotenv').config();

// CORS
app.use((req,res,next) => {
    res.header("Access-Control-Allow-Origin", process.env.CLIENT_BASE_URL) // update to match the domain the request is coming from
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

// include routes
app.use(bodyParser.json());
app.use('/', require('./routes'));

app.listen(port, () => console.log(`Listening on port ${port}`))