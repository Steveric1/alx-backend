import kue, { createQueue } from 'kue';

const queue = createQueue();

queue.process('push_notification_code', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
});


function sendNotification(phoneNumber, message) {
    console.log(
        'Sending notification to '+ phoneNumber + ', with message: '+ message
    );
}