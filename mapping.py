mappings = {
    'dynamic': 'strict',  # Makes it so the index will reject data if it does not respect the mapping
    'properties': {
        'timestamp': {'type': 'date'},
        'endpoint_id': {'type': 'keyword'},
        'build_number': {'type': 'keyword'},

        'pii_files': {
            'type': 'nested',
            'properties': {

                'path': {'type': 'text'},  # This level represents a list of pii files
                'score': {'type': 'float'},

                'mime_type': {'type': 'keyword'},
                'hash': {'type': 'keyword'},
                'encrypted': {'type': 'boolean'},
                'timestamp': {'type': 'date'},

                'content': {
                    'type': 'nested',
                    'properties': {

                        'type_name': {'type': 'text'},  # This level represents the content of a pii file
                        'type_id': {'type': 'keyword'},
                        # Type name and id represent the name and id of the corresponding RegExs
                        'amount': {'type': 'integer'},
                        'correlations': {
                            'type': 'nested',
                            'properties': {

                                'type_name': {'type': 'text'},
                                'type_id': {'type': 'keyword'},  # This level represents the correlation level
                                'correlation': {'type': 'float'}
                                # This structure allows for correlation on multiple entities, not just names
                            }
                        }
                    }
                }
            }
        }
    }
}
