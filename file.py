import random
import time
import uuid
import json

RegexEnum = {
    0: {'name': 'creditCard', 'guid': 'f8052141-a3a7-4805-bc0f-527facaddce0'},
    1: {'name': 'phone', 'guid': 'e27d0029-b968-470a-9820-4fb0574c3457'},
    2: {'name': 'email', 'guid': '7b36eada-bfd5-4e32-b82f-d88416cd8e81'},
    3: {'name': 'nas', 'guid': 'c4d2da05-780b-45b1-954f-0f7501958778'},
    4: {'name': 'driveLicence', 'guid': 'd704fe07-8644-4a14-b3e3-45768603f18e'},
    5: {'name': 'americanNas', 'guid': 'cc984986-a293-4080-8d13-653f8c22109f'},
    6: {'name': 'frenchNas', 'guid': '12780e72-0333-4890-ad07-bfc08e4d00ef'},
    7: {'name': 'britishNas', 'guid': '252a2163-cbb5-4f74-9998-ce99d0764f85'},
    8: {'name': 'germanNas', 'guid': '79209af6-dc6e-4bcf-aeac-0c62f6f2e472'},
    9: {'name': 'australianNas', 'guid': 'b8ba8d40-4265-40bc-9e78-672cb20e6e2b'},
}

MimeTypeEnum = {
    0: 'image/bmp',
    1: 'text/csv',
    2: 'application/msword',
    3: 'image/gif',
    4: 'image/jpeg',
    5: 'audio/mpeg',
    6: 'application/vnd.oasis.opendocument.spreadsheet',
    7: 'text/plain',
    8: 'application/zip',
    9: 'application/vnd.oasis.opendocument.spreadsheet'
}

EndpointEnum = {
    0: {'name': 'Nics endpoint', 'guid': 'f8052141-a3a7-4805-bc0f-527facaddce0'},
    1: {'name': 'Mics endpoint', 'guid': 'e27d0029-b968-470a-9820-4fb0574c3457'},
    2: {'name': 'Jords endpoint', 'guid': '7b36eada-bfd5-4e32-b82f-d88416cd8e81'},
    3: {'name': 'Jacobs endpoint', 'guid': 'c4d2da05-780b-45b1-954f-0f7501958778'},
}


class File:

    def __init__(self, number_of_regexes = 3, timestamp = None):
        self.generate_random_file()


    def json(self):
        return json.dumps(self.file)


    def generate_random_file(self, number_of_regexes = 3, timestamp=None):
        file = {
            'path': f'path_{random.randrange(0, 1000, 1)}',
            'score': random.randrange(0, 100)/100,
            'mime_type': MimeTypeEnum[random.randrange(0, 9, 1)],
            'timestamp': int(round(time.time()*1000, 0)),
            'hash': str(uuid.uuid1()),
            'encrypted': True,
            'content': [self.get_random_content() for i in range(0, number_of_regexes)]
            }

        if timestamp:
            file['timestamp'] = timestamp

        self.file = file

    def get_random_content(self):
        type = RegexEnum[random.randrange(0, 9, 1)]
        return {
            'type_name': type['name'],
            'type_id': type['guid'],
            'amount': random.randrange(0, 300, 5),
            'correlations': [
                {
                'type_name': "name", 'type_id': RegexEnum[random.randrange(0, 9, 1)]['guid'],  'correlation': random.randrange(0, 100, 1)/100
                },
                {
                'type_name': "emails", 'type_id': RegexEnum[random.randrange(0, 9, 1)]['guid'], 'correlation': random.randrange(0, 100, 1)/100
                },
             ]
        }
        