import unittest
import os
from dotenv import load_dotenv
from bigbluebutton_api_python import BigBlueButton

load_dotenv()
URL = os.getenv("URL")
SECRET = os.getenv("SECRET")
b = BigBlueButton(URL, SECRET)
meeting_id = 'Test'
moderator_user='Moderator'
moderator_pw='moderatorPW'
attendee_user='Attendee'
attendee_pw='attendeePW',
maxParticipants=2

class TestBigbluebuttonApiPython(unittest.TestCase):

    def test_1_is_meeting_running(self):
        running = b.is_meeting_running(meeting_id).is_meeting_running()
        self.assertTrue(isinstance(running, bool))

    def test_2_create_meeting(self):
        params = {
            'meeting_id': meeting_id,
            'name': meeting_id,
            'maxParticipants': maxParticipants,
            'attendeePW': attendee_user,
            'moderatorPW': moderator_pw,
        }
        create = b.create_meeting(meeting_id,params)
        self.assertEqual(create.get_meetingid(), meeting_id)

    def test_3_get_meeting_info(self):
        info = b.get_meeting_info(meeting_id)
        maxUsers = info.get_meetinginfo().get_max_users()
        maxUsers = int(maxUsers)
        self.assertEqual(maxUsers, maxParticipants)

    def test_4_get_meetings(self):
        meetings = b.get_meetings().get_meetings()
        self.assertTrue(isinstance(meetings, list))

    def test_5_get_join_meeting_url(self):
        url = b.get_join_meeting_url(moderator_user,meeting_id, moderator_pw)
        print(f'\n{url}')
        self.assertTrue('checksum' in url and '/api/join' in url)

    def test_6_get_api_version(self):
        version = b.get_api_version().get_version()
        version = float(version)
        self.assertTrue(isinstance(version, float))

    def test_7_get_recordings(self):
        recordings = b.get_recordings(meeting_id).get_recordings()
        self.assertTrue(isinstance(recordings, list))

    def test_8_end_meeting(self):
        if b.is_meeting_running(meeting_id).is_meeting_running():
            end = b.end_meeting(meeting_id, moderator_pw)    






    






