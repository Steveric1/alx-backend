import redis, { createClient } from  'redis';

const client = createClient();

client.on('connect', () => {
    console.log('Redis  client connected');
});

await client.set('key', 'value');
const value = await client.get('key');
console.log(value);

client.on('error', (err) => {
    console.log('Redis client is not connected');
})