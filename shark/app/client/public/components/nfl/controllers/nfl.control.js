nfl
    .controller('NflController', function($scope, Team, Game) {
		$scope.games = Game.query();

		Team.query().$promise.then(function(data) {
            $scope.teams = data;
        });

		var entry = Team.get({ id: 1 }, function() {
    		console.log(team);
  		});

});
