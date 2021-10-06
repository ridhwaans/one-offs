const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = process.env.PORT || 5000;

// include routes
app.use(bodyParser.json());
app.use('/', require('./routes'))

app.listen(port, ()=> console.log(`listening on port ${port}`))