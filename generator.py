import random
import time
import uuid

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


def generate_file():
    file = {
        'path': 'sdfg',
        'mime_type': MimeTypeEnum[int(random.random() * 10)],
        'hash': str(uuid.uuid4()),
        'score': random.random(),
        'encrypted': True,
        'content': {}
    }

    if random.random() > 0.1:
        file.update({
            'encrypted': False,
            'content': {
                'names': random.random() * 100,
                'sensitivityScore': random.random(),
                'pii': [
                    {
                        'name': RegexEnum[i]['name'],
                        'guid': RegexEnum[i]['guid'],
                        'quantity': random.random() * 100,
                        'correlation': [
                            {
                                'name': RegexEnum[j]['name'],
                                'guid': RegexEnum[j]['guid'],
                                'correlation': random.random()
                            }
                            for j in random.sample(list(RegexEnum.keys()), int(random.random() * 10))
                        ]
                    }
                    for i in random.sample(list(RegexEnum.keys()), int(random.random() * 10))
                ]
            }
        })
        return file

def generate_post(endpoint_id, number_of_files):
    post = {
        'endpoint_id': endpoint_id,
        'user': 'Roger',
        'timestamp': time.time(),
        'first_post': False,
        'build_number': 'dev 2.1.101',
        'pii_files': [
            generate_file()
            for _ in range(number_of_files)
        ],
        'event': []
    }
    return post