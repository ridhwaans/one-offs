const express = require('express');
const qs = require('qs'); //used for processing query strings
const {createTopic} = require('../data')
const router = express.Router();

router.get('/v1/hello', (req, res) => {
    res.json('hello world')
})

router.post('/v1/topics', async (req,res) => {
    res.json(await createTopic(req.body))
})

// handles any requests that dont match the routes above
router.get('*', (req, res) => {
    res.json('not found')
})

module.exports = router;