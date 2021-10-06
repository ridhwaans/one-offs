const {PrismaClient} = require('@prisma/client')
const prisma = new PrismaClient();

const createTopic = async (params) => {
    params && console.log(`topic is ${JSON.stringify(params)}`)

    try {
        const topic = await prisma.topic.create({
            data: {
                account_id: parseInt(params.account_id),
                name: params.name,
                date_added: new Date()
            }
        })

        return { status: 200, topic: topic.id}
    } catch (e) {
        console.log("there was problem with db transaction", e)
        return { status: 500 }
    }
}


module.exports = {createTopic}