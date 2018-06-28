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
    

    // var firework_container = document.getElementById('dashboard-page')
    // var options = {
    //   maxRockets: 3,            // max # of rockets to spawn
    //   rocketSpawnInterval: 150, // millisends to check if new rockets should spawn
    //   numParticles: 100,        // number of particles to spawn when rocket explodes (+0-10)
    //   explosionMinHeight: 0.9,  // percentage. min height at which rockets can explode
    //   explosionMaxHeight: 0.7,  // percentage. max height before a particle is exploded
    //   explosionChance: 0.08     // chance in each tick the rocket will explode
    // };

    // var fireworks = new Fireworks(firework_container, options)
    // var stop = fireworks.start()
    // stop() // stop rockets from spawning
    // fireworks.stop() // also stops fireworks.
    // fireworks.kill() // forcibly stop fireworks
    // fireworks.fire() // fire a single rocket.

















    /**********************************/
    

    $scope.word_list=[];
    var queue=[];
    $scope.show_words=true;

    function fetch_words() {
        $http({
            method: 'GET',
            url: "/api/fetch"
        }).then(function (response) {
            $scope.word_list=response['data']['data'];
            console.log($scope.word_list)
        });

        $scope.current_score = get_ls();
    }

    function update_ls() {
        var d=new Date();
        var key=d.toLocaleDateString();
        var data=JSON.stringify($scope.current_score);
        localStorage.setItem("revison-"+key, data);
    }

    function get_ls() {
        var d=new Date();
        var key=d.toLocaleDateString();
        var data =localStorage.getItem("revison-"+key);

        if(data==null) {
            return {
                "correct": 0,
                "attempts": 0 
            }
        }
        return JSON.parse(data);

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
                achievement();
            } else {
                $scope.word_list[question_idx].state="INCORRECT";
            }
        }

        update_ls();

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

    function achievement() {
        var stop;
        // if($scope.current_score.correct %5==0) {
        //     $scope.show_words=false;
        //     stop = fireworks.start()
        // }

        // setTimeout(function(){
        //     stop();
        //     $scope.show_words=true;
        //     $scope.$apply();
        // }, 5000)




    }

    
});
