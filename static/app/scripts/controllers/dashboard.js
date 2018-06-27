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
    

    $scope.word_list=[]
    $http({
            method: 'GET',
            url: "/api/fetch"
    }).then(function (response) {
        $scope.word_list=response['data']['data'];
        console.log($scope.word_list)
    });

    $scope.submit_answer = function(question_idx, option_idx) {
        console.log($scope.word_list[question_idx])
        option_idx+=1
        if($scope.word_list[question_idx].state==="ACTIVE") {

            console.log("sdsdfs");

            if($scope.word_list[question_idx].answer_idx===option_idx) {
                $scope.word_list[question_idx].state="CORRECT";
            } else {
                $scope.word_list[question_idx].state="INCORRECT";
            }
        } else {

        }

        $http({
            method: 'POST',
            url: "/api/submit",
            data: $scope.word_list[question_idx]
        }).then(function (response) {
            console.log(response)
        });



        console.log("sdvmksdvm")



    }

    
});
