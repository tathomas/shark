angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

    $stateProvider.state({
        name: 'nfl',
        url: '/',
        templateUrl: 'public/components/nfl/templates/nfl.template',
        controller: 'NflController'
    });

    $urlRouterProvider.otherwise('/');
}]);
