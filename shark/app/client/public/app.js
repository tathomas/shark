'use strict';

var nfl = angular.module("nfl", ['ngResource']);

angular
    .module('SampleApplication', [
        'appRoutes',
        'nfl',
        'ngResource'
    ]);
