#!/usr/bin/env python3
from testing import test

class SMS_store():
    def __init__(self):
        self.sms_list = []

    def add_new_arrival(self, from_number, time_arrived, text_of_sms):
        """ Makes new SMS tuple, inserts it after other messages
        in the store. When creating this message, its
        has_been_viewed status is set False.
        """
        self.sms_list.append((False, from_number, time_arrived, text_of_sms))

    def message_count(self):
        """ Returns the number of sms messages in my_inbox. """
        return len(self.sms_list)

    def get_unread_indexes(self):
        """ Returns list of indexes of all not-yet-viewed SMS messages. """
        not_read = []
        for index,sms in enumerate(self.sms_list):
            if sms[0] == False:
                not_read.append(index)
        return not_read
        pass

    def get_message(self, i):
        """ Return (from_number, time_arrived, text_of_sms) for message[i]
        Also change its state to "has been viewed".
        if there is not message at position i, return None
        """
        if i < len(self.sms_list):
            sms = self.sms_list[i]
            from_number = sms[1]
            time_arrived = sms[2]
            text_of_sms = sms[3]
            self.sms_list[i] = (True, from_number, time_arrived, text_of_sms)
            return (from_number, time_arrived, text_of_sms)
        else:
            return None

    def delete(self, i):
        """ Delete the message at index i. """
        if i < len(self.sms_list):
            self.sms_list.pop(i)

    def clear(self):
        """ Delete all messages from inbox. """
        self.sms_list.clear()

my_inbox = SMS_store()

sms1 = (555123456, "06-07-2020, 12:00", "This is your testing message.")
sms2 = (513123955, "10-07-2020, 07:00", "That's another message.")
sms3 = (799185333, "08-06-2020, 15:15", "That message has beed read.")

# Add three SMS messages to the store
my_inbox.add_new_arrival(*sms1)
my_inbox.add_new_arrival(*sms2)
my_inbox.add_new_arrival(*sms3)

# Check for unread SMS messages.
test(my_inbox.get_unread_indexes() == [0,1,2])

# Check for number of SMS messages in the store.
test(my_inbox.message_count() == 3)

# Get some existing and non-existing SMS messages.
test(my_inbox.get_message(3) == None)
test(my_inbox.get_message(0)[0] == sms1[0])
test(my_inbox.get_message(5) == None)

# Check whether the SMS message that we have read has changed the state.
test(my_inbox.get_unread_indexes() == [1,2])

# Delete 1st SMS message and check whether the 1st message is still the same.
# Check count.
my_inbox.delete(0)
test(not my_inbox.get_message(0) == sms1)
test(my_inbox.message_count() == 2)

# Clear the SMS store, check messages count.
my_inbox.clear()
test(my_inbox.message_count() == 0)
