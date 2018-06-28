'use strict';

/**
 * @ngdoc function
 * @name yapp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of yapp
 */

app.controller('DashboardCtrl', function($scope, $state, $http) {
    $scope.$state = $state;
    var hello = "hellp";

    console.log("in dashbaord cteel");
    $scope.menuItems = [];
    angular.forEach($state.get(), function (item) {
        if (item.data && item.data.visible) {
            $scope.menuItems.push({name: item.name, text: item.data.text});
        }
    });
    
    

    $scope.word_list=[];
    var queue=[];

    function fetch_words() {
        $http({
            method: 'GET',
            url: "/api/fetch"
        }).then(function (response) {
            $scope.word_list=response['data']['data'];
            console.log($scope.word_list)
        });

        $scope.current_score = {
            "correct" : 0,
            "attempts" : 0
        };

    }

    function fetch_average_score() {
        $http({
            method: 'GET',
            url: "/api/average_score"
        }).then(function (response) {
            $scope.average_score = response.data.data;
        });
    }


    fetch_words();
    fetch_average_score();
    

    $scope.submit_answer = function(question_idx, option_idx) {
        
        option_idx+=1;
        $scope.current_score.attempts+=1;
        queue.push(question_idx);
        if($scope.word_list[question_idx].state==="ACTIVE") {
            if($scope.word_list[question_idx].answer_idx===option_idx) {
                $scope.current_score.correct+=1;
                $scope.word_list[question_idx].state="CORRECT";
            } else {
                $scope.word_list[question_idx].state="INCORRECT";
            }
        }

        fetch_limited_question();

        $http({
            method: 'POST',
            url: "/api/submit",
            data: $scope.word_list[question_idx]
        }).then(function (response) {
            $scope.average_score = response.data.data;
        });
    }

    $scope.reset_word_list=function () {
        fetch_words();
        fetch_average_score();
    }

    $scope.ignore_word=function(question_idx) {
        $http({
            method: 'POST',
            url: "/api/ignore_word",
            data: $scope.word_list[question_idx]
        }).then(function (response) {
            console.log(response)
            $scope.word_list.splice(question_idx,1);

        });
    }

    function fetch_limited_question() {

        if(queue.length <= 2) {
            return
        }

        var question_idx=queue.shift();

        $http({
            method: 'GET',
            url: "/api/fetch_limited/1"
        }).then(function (response) {
            $scope.word_list[question_idx]=response.data.data[0];
        });

    }

    
});
