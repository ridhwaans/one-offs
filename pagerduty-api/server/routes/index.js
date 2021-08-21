const express = require('express');
const qs = require('qs')
const pagerDutyServiceConstructor = require('../services/pagerduty')
const pagerDutyService = new pagerDutyServiceConstructor()
const router = express.Router();

router.get('/api/users', async (req, res) => {
    let data = await pagerDutyService.getUsers();
    res.json(data.users);
})

// handles any requests that dont match the route above
router.get('*', (req, res) => {
    res.json('not found')
})

module.exports = router;