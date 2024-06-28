import kue, { createQueue } from 'kue';

const queue = createQueue();

const job = queue.create('push_notification_code', {
    phoneNumber: '09022216794',
    message: 'Account registered',
});

// Set up event listener for the job
job
  .on('enqueue', () => console.log('Notification job created: ', job.id))
  .on('complete', () => console.log('Notification job completed'))
  .on('failed attempt', () => console.log('Notification job failed'));

job.save();