'use strict';

/**
 * @ngdoc overview
 * @name yapp
 * @description
 * # yapp
 *
 * Main module of the application.
 */
var states = [
        { name: 'base', state: { abstract: true, url: '', templateUrl: 'views/base.html', data: {text: "Base", visible: false } } },
        { name: 'wordQuiz', state: { url: '/wordQuiz', parent: 'base', templateUrl: 'views/wordQuiz.html', controller: 'WordQuizCtrl', data: {text: "WordQuizCtrl", visible: false } } },
        { name: 'allWords', state: { url: '/allWords', parent: 'base', templateUrl: 'views/allWords.html', controller: 'AllWordsCtrl', data: {text: "AllWordsCtrl", visible: false } } }

        
    ];
    console.log("suman");

var app = angular.module('iqDeployment', [
                'ui.router',
                'satellizer'
            ]);

app.config(function($stateProvider, $urlRouterProvider, $authProvider) {
    // $authProvider.google({
    //     clientId: '771308557555-eobkgorqrga3cn5egfitru1uvc5bnq9n.apps.googleusercontent.com',
    //     optionalUrlParams: ['access_type'],
    //     accessType: 'offline'
    // });

    $authProvider.google({
        url: '/auth/google',
        authorizationEndpoint: 'https://accounts.google.com/o/oauth2/auth',
        redirectUri: window.location.origin,
        requiredUrlParams: ['scope'],
        optionalUrlParams: ['display'],
        scope: ['profile', 'email'],
        scopePrefix: 'openid',
        scopeDelimiter: ' ',
        display: 'popup',
        oauthType: '2.0',
        popupOptions: { width: 452, height: 633 },
        clientId: '771308557555-9bn3b5ssng28mj0l6sj0fa1c0rfv26f0.apps.googleusercontent.com',
        optionalUrlParams: ['access_type'],
        accessType: 'offline'
    });



    // $urlRouterProvider.when('/dashboard', '/dashboard/overview');
    $urlRouterProvider.otherwise('/wordQuiz');
    
    angular.forEach(states, function (state) {
        $stateProvider.state(state.name, state.state);
    });
});

app.run(function ($rootScope, $state, $auth) {

    $rootScope.wordlist={
        "wordlist_type" :[{
            id: "baron",
            name:"Baron"
            }, {
                id: "manhattan_essentials",
                name:"Manhattan Essentials"
            }, {
                id: "manhattan_advanced",
                name:"Manhattan Advanced"
            },{
                id: "magoosh",
                name:"Magoosh"
            }],
        "selected_word_list": "baron",
        "change_wordlist_type" : function(wordlist_type) {
            console.log("suman hel ->",wordlist_type);

            this.selected_word_list=wordlist_type;
            localStorage.setItem("wordlist_type", wordlist_type);
            $state.go($state.current, {}, {reload: true});
        }
    };

    var selected_word_list=localStorage.getItem("wordlist_type");

    if(selected_word_list) {
        $rootScope.wordlist.selected_word_list=selected_word_list;
    } else {
        $rootScope.wordlist.selected_word_list="baron";
    }


    $rootScope.$on('$stateChangeStart',
        function (event, toState) {
            var requiredLogin = false;
            if (toState.data && toState.data.requiredLogin)
                requiredLogin = true;

            if (requiredLogin && !$auth.isAuthenticated()) {
                event.preventDefault();
                $state.go('wordQuiz');
        }
    });
});
