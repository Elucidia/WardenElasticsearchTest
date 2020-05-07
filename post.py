import random
import time
import uuid
import json
from file import File

EndpointEnum = {
    0: {'name': 'Nics endpoint', 'guid': 'f8052141-a3a7-4805-bc0f-527facaddce0'},
    1: {'name': 'Mics endpoint', 'guid': 'e27d0029-b968-470a-9820-4fb0574c3457'},
    2: {'name': 'Jords endpoint', 'guid': '7b36eada-bfd5-4e32-b82f-d88416cd8e81'},
    3: {'name': 'Jacobs endpoint', 'guid': 'c4d2da05-780b-45b1-954f-0f7501958778'},
}

class Post:

    def __init__(self, amount_of_files=5, number_of_regex_per_file=5, hours_between_analyzed=24, insert_similar_files=True, endpoint_index = None):
        now = int(round(time.time()*1000, 0))
        self.files = [File(timestamp=now + (i*hours_between_analyzed*3600*1000)) for i in range(0, amount_of_files)]

        if insert_similar_files:
            content = self.files[-1].file['content']
            score = self.files[-1].file['score']
            hash = self.files[-1].file['hash']

            self.files[0].file['content'] = content
            self.files[0].file['score'] = score
            self.files[0].file['hash'] = hash


        if endpoint_index or str(endpoint_index) == '0':
            ep_index = endpoint_index
        else:
            ep_index = random.randrange(0, 3, 1)

        state = {
            'endpoint_id': EndpointEnum[ep_index]['name'],
            'timestamp': now + (hours_between_analyzed*amount_of_files*3600*1000),
            'build_number': 1.0
        }

        for f in self.files:
            f.file['state'] = state