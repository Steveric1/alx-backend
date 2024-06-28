import { createQueue } from "kue";

const queue = createQueue();

const blacklistedNumber = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);
    if (blacklistedNumber.includes(phoneNumber)) {
        const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
        job.failed().error(error);
        done(error)
    } else {
        job.progress(50, 100);
        console.log('Sending notification to '+ phoneNumber + ', with message: '+ message);
        setTimeout(() => {
            job.progress(50, 100);
            done();
        }, 1000)
    }
    done();
}


queue.process('push_notification_code_2', 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done)
});
