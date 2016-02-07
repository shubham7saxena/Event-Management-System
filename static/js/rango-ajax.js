$(document).ready(function() {
	

	$('#likes').click(function(){
	        var catid;
	        catid = $(this).attr("data-catid");
	         $.get('/registeration/like_category/', {category_id: catid}, function(data){
	                   $('#like_count').html(data);
	                   $('#likes').hide();
	               });
	    });


    	$('#suggestion').keyup(function(){
		var query;
		query = $(this).val();
		$.get('/registeration/suggest_category/', {suggestion: query}, function(data){
                 $('#cats').html(data);
		});
	});

    
	$('.registeration-add').click(function(){
	    var catid = $(this).attr("data-catid");
        var url = $(this).attr("data-url");
        var title = $(this).attr("data-title");
        var me = $(this)
	    $.get('/registeration/auto_add_page/', {category_id: catid, url: url, title: title}, function(data){
	                   $('#pages').html(data);
	                   me.hide();
	               });
	    });

});
