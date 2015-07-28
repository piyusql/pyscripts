#!/usr/bin/python
from datetime import datetime


class Resources(object):
    # keys are room capacity and values are rooms availability
    roomsCount = {10: 4, 20: 2, 50: 1}
    telephoneCount = 5
    projectorCount = 4
    chatRoomsCount = 3
    allocations = {}

    def current_availability(self):
        print "\nResource Current Availability\n", "=-=" * 10
        print "Rooms : %s" % (self.roomsCount)
        print "Telephones : %d" % (self.telephoneCount)
        print "Allocations : %s" % (self.allocations)

    def allocate_room(self, attendees):
        # check if the room is available for this no of attendees
        _key = self.get_room_keys(attendees)
        if _key:
            # allocate a room
            self.roomsCount[_key] -= 1
            print "Room for size %d allocated to %d people" % (_key, attendees)
            return _key
        else:
            raise ResourceUnavailable("no more rooms available")

    def de_allocate_room(self, _key):
        # de_allocate the previously acquired room
        # we can set the timing to make it auto de_allocate
        self.roomsCount[_key] += 1

    def get_room_keys(self, attendees):
        # check for the lowest capacity room to accomodate all the attendees
        # will keep the sorted rooms capacity in sorted dict or tuple
        for key, value in self.roomsCount.items():
            if key > attendees and value > 0:
                return key

    def allocate_telephone(self, _count):
        if self.telephoneCount < _count:
            print "not enough telephones available"
            return False
        else:
            self.telephoneCount -= _count
            print "%d-telephone allocated" % (_count)
            return _count

    def de_allocate_telephone(self, _count):
        self.telephoneCount += _count
        print "%d telephones freed and the currently telephones availability is %d" % (_count, self.telephoneCount)

    def allocate(self, attendees, telephone):
        print "\nRequested : %d attendees, %d telephone\n" % (attendees, telephone), "---" * 10
        try:
            # priority is to find a room
            _key = self.allocate_room(attendees)
            # check if all other resources are available
            """
            if not any((self.allocate_telephone(telephone),)):
                # de allocate telephone
                self.de_allocate_telephone(telephone)
            else:
                print "Successful Allocation of room-id : %s and %d telephones for a group of %d attendees." %(_key, telephone, attendees)
            """
            if not self.allocate_telephone(telephone):
                self.de_allocate_room(_key)
            else:  # when all the resources available
                meeting_id = self.get_a_unique_allocation_id(_key, attendees, telephone)
                self.allocations[meeting_id] = {'start': datetime.now(), 'attendees': attendees, 'telephone': telephone, 'room_key': _key}
                print "Successful Allocation : enjoy your meeting !!!, ID : %s" % (meeting_id)
                return meeting_id
        except ResourceUnavailable as e:
            print e.message

    def de_allocate(self, meeting_id):
        print "\nDe-Allocation Request for meeting ID : %s" % (meeting_id)
        if meeting_id not in self.allocations:
            print "no meeting forund for ID : %s" % (meeting_id)
            return
        # need the room key to de-allocate
        room_key = self.allocations[meeting_id]['room_key']
        telephone = self.allocations[meeting_id]['telephone']
        self.de_allocate_room(room_key)
        self.de_allocate_telephone(telephone)
        self.allocations[meeting_id]['end'] = datetime.now()

    def get_a_unique_allocation_id(self, room_key, attendees, telephone):
        """Its just the ID created so that we can refer to the data in future"""
        return "R-%d:P-%d:T-%d" % (room_key, attendees, telephone)


class ResourceUnavailable(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


def menu():
    print "\nUsage: You can request meeting as <A/D> <attendees> <telephone>, press bye to exit."
    resourse = Resources()
    input = raw_input("?\n")
    while(input != 'bye'):
        resourse.current_availability()
        try:
            method = input.split()[0]
            if method == 'A':
                attendees = int(input.split()[1])
                telephone = int(input.split()[2])
                resourse.allocate(attendees, telephone)
            elif method == 'D':
                meeting_id = input.split()[1]
                resourse.de_allocate(meeting_id)
            print resourse.current_availability()
        except IndexError:
            print "invalid input format : right way to do is A 12 4/ D <meeting_id>"
        input = raw_input("\ttry again or bye.\n")
        # EOL

if __name__ == '__main__':
    menu()
