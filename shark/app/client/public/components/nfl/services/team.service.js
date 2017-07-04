nfl
    .factory('Team', function($resource) {
        return $resource(
            'http://localhost:8000/teams/:id/',
            {},
            {
                'query': {
                    method: 'GET',
                    isArray: true,
                    headers: {
                        'Content-Type':'application/json'
                    }
                }
            },
            {
                stripTrailingSlashes: false
            }
        );
    });
