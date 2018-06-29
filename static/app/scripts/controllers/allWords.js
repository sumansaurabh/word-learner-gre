/*
* @Author: sumansaurabh
* @Date:   2018-06-29 13:43:46
* @Last Modified by:   sumansaurabh
* @Last Modified time: 2018-06-29 23:44:42
*/
'use strict';

/**
 * @ngdoc function
 * @name yapp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of yapp
 */

app.controller('AllWordsCtrl', function($scope, $rootScope, $state, $http) {
    $scope.$state = $state;
    
    function create_table(data) {

		$("#all-words").html('<table id="all-words-table" class="display" width="100%"></table>');


		var columns = [{
            	title : "Words",
            	width: '10%',
            	text_width: '120px'
            },{
            	title : "Meaning",
            	width: '30%',
            	text_width: '350px'
            }, {
            	title : "Status",
            	width: '5%',
            	text_width: '30px'
            }, {
            	title : "Correct",
            	width: '5%',
            	text_width: '30px'
            }, {
            	title : "Incorrect",
            	width: '5%',
            	text_width: '30px'
            },{
            	title : "Attempt",
            	width: '5%',
            	text_width: '30px'
            }];

            var row_data = data.map(function(doc){
            	return [doc['word'], doc['meaning'], doc['status'], doc['correct'], doc['attempts']-doc['correct'], doc['attempts']]
            });;

            var graph_configuration = $('#all-words-table').DataTable( {
		        data: row_data,
		        columns: columns,
		        "columnDefs": [{ className: "word_row", "width": "10%", "targets": 0 },
		        	{ className: "word_meaning", "width": "30%", "targets": 1 },
		        	{ className: "word_meaning", "width": "5%", "targets": 2 },
		        	{ className: "word_meaning", "width": "5%", "targets": 3 },
		        	{ className: "word_meaning", "width": "5%", "targets": 4},
		        	{ className: "word_meaning", "width": "5%", "targets": 5 }],
		        "lengthMenu": [15, 40, 60, 80, 100],
        		"pageLength": 15,
        		"createdRow": function( row, data, dataIndex ) {
			            if ( data[2] === -1 ) {        
			        		$(row).addClass('brown');
			      		}

			      		if ( ((data[3]/data[5])*100)<70) {        
			        		$(row).addClass('red');
			      		}

			      		if ( ((data[3]/data[5])*100)>70 && ((data[3]/data[5])*100)<99) {        
			        		$(row).addClass('orange');
			      		}

			      		if ( ((data[3]/data[5])*100)===100) {        
			        		$(row).addClass('green');
			      		}


			     },
		        fixedColumns: true
		    });

		    function column_based_filter() {
		    	var table_container =  $('#all-words-table');

		    	var _thead = table_container.find('thead')
                var x1 =  _thead.find('.col-search-text');
                x1.remove();
                var org_idx_map = {}
                _thead.append('<tr class="col-search-text"></tr>');
                columns.forEach(function(series_item, idx){
                    var inp = '<th><div class="search-box-cnt" style="width:'+columns[idx]['width']+'">'+
                                '<input class="app-search-box transparent no_margin_right iq-table-col-search-'+idx+'" type="text" style="width:'+columns[idx]['text_width']+'" >'+
                              '</div></th>'

                    _thead.find('tr:last-child').append(inp)
                })

                graph_configuration.columns().every( function (idx) {
                    var that = this;
                    $('#all-words-table .iq-table-col-search-'+that[0]['0']).on( 'keyup change', function () {
                        that.search( this.value ).draw();
                    });
                });
		    }
		    column_based_filter();
	}

	$scope.change_page = function() {

	}


	function get_words() {
		 $http({
            method: 'GET',
            url: "/api/"+$rootScope.wordlist.selected_word_list+"/allWords"
        }).then(function (response) {
            var data=response['data']['data'];
            $scope.not_attempted=response['data']['not_attempted'];
            $scope.ignored_word=response['data']['ignored_word'];
            create_table(data);
        });

	}
	get_words();

    
});
