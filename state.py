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


class State:
    def __init__(self, timestamp=None, endpoint_index=None):
        self.generate_state(endpoint_index=endpoint_index, timestamp=timestamp)

    def json(self):
        dict = {
            'timestamp': self.timestamp,
            'endpoint_id': self.endpoint_id,
            'build_number': self.build_number,
            'pii_files': self.pii_files,
        }

        return json.dumps(dict, indent=4, separators=[',', ':'])

    def generate_state(self, endpoint_index=None, timestamp=None):

        if endpoint_index:
            self.endpoint_id = EndpointEnum[endpoint_index]['name']
        else:
            self.endpoint_id = EndpointEnum[random.randrange(0, 3, 1)]['name']

        if timestamp:
            self.timestamp = timestamp
        else:
            self.timestamp = int(round(time.time() * 1000, 0))

        self.build_number = '1.0'

        self.pii_files = [
            {
                'path': f'path_{random.randint(0, 999)}',
                'score': random.random(),
                'mime_type': MimeTypeEnum[random.randint(0, 9)],
                'timestamp': self.timestamp,
                'hash': str(uuid.uuid1()),
                'encrypted': True,
                'content': [
                    {
                        'type_name': RegexEnum[i]['name'],
                        'type_id': RegexEnum[i]['guid'],
                        'amount': random.randint(0, 300),
                        'correlations': [
                            {
                                'type_name': RegexEnum[j]['name'],
                                'type_id': RegexEnum[j]['guid'],
                                'correlation': random.random()
                            }
                            for j in random.sample(list(RegexEnum.keys()), random.randint(0, 9))
                        ]
                    }
                    for i in random.sample(list(RegexEnum.keys()), random.randint(0, 9))
                ]
            }
            for _ in range(1, random.randint(1, 100))
        ]

    def get_timestamp(self):
        now = int(round(time.time() * 1000, 0))
        self.timestamp = now + random.randrange(0, 1000000, 5)


def get_state_timeserie(number_of_endpoints=1, states_per_endpoint=3):
    now = int(round(time.time() * 1000, 0))
    endpoints = []

    for k in range(0, number_of_endpoints):
        endpoint_index = k
        endpoints.append([State(endpoint_index=endpoint_index, timestamp=now + (i) * 24 * 3600 * 1000) for i in
                          range(0, states_per_endpoint)])

    return endpoints

def get_state(timestamp, end_point_index):
    return State(timestamp, end_point_index)