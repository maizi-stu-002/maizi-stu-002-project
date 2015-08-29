$(function(){
// course_stage.html
	$(".btn-micv5").on("click", function(){
		// 点击按钮跳转到列表中第一个课程播放页面
	     url = $("article h3").find("a").first().attr("href");
	     if(typeof(url) != "undefined"){
	        location.href = url;
	     }
	});

	// course.html
	//课程列表通过ajax进行翻页
	//翻页动画
	var courselistAnimate = function(data){
		$(".course-list").animate({
			'opacity':0,
		},50,function(){
			var $courselist = $(".course-list");
			$courselist.html(data);
			$courselist.animate({
				'opacity':1,
			},550);
		});	
	};
	//数字按钮
	$(".page-num").on("click", function(){
		var $btn = $(this);
		if($btn.hasClass('active')){
			return false;
		}else{
			$.get("/course/", {'page':$btn.text()}, function(data, status){
				if(status==="success"){
					courselistAnimate(data);
					// $('.page-num').removeClass('active');
					// $btn.addClass("active");
					$btn.addClass("active").parent().siblings().children(".page-num").removeClass("active");
				}
			});
		}		
	});
	//向前翻页
	$(".v5-icon-prev").on("click", function(){
		var $active_btn = $('.page-num').filter('.active');
		if ($active_btn.text() === "1" ){
			return false;
		}else{
			var pageNum = parseInt($active_btn.text()) - 1;
			$.get("/course/", {'page':pageNum}, function(data, status){
				if(status==="success"){
					courselistAnimate(data);
					$('.page-num').removeClass('active');
					$active_btn.parent().prev().children(".page-num").addClass('active');
				}
			});
		}
	});
	//向后翻页
	$(".v5-icon-next").on("click", function(){
		var $active_btn = $('.page-num').filter('.active');
		var $last_btn_text = $('.page-num').last().text();
		if($active_btn.text() === $last_btn_text){
			return false;
		}else{
			var pageNum = parseInt($active_btn.text()) + 1;
			$.get("/course/", {'page':pageNum}, function(data, status){
				if(status==="success"){
					courselistAnimate(data);
					$('.page-num').removeClass('active');
					$active_btn.parent().next().children(".page-num").addClass('active');
				}
			});
		}
	});
});