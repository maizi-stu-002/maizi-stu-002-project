$(function(){
	$(".btn-micv5").on("click", function(){
		// 点击按钮跳转到列表中第一个课程播放页面
	     url = $("article h3").find("a").first().attr("href");
	     if(typeof(url) != "undefined"){
	        location.href = url;
	     }
	});
});