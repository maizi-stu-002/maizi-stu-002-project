
$(document).ready(function(){
	var player = videojs("video-player");
	var _id_lesson = $('.active_null .active').attr('lessonId');
	var is_poppup_exam = false;
	//在线测试
	var onlinetest = function(){
		player.pause();
		$('#onlinetestModal').modal('show');
		var _section = $('.onlinetest-wp').find('section');
		var _button = $('.onlinetest-wp').find('button');
		var _this_section_length = _section.length;
		var _this_section_width = _section.outerWidth();
		$('.onlinetest-wp').width(_this_section_width*_this_section_length);
		  _button.click(function(){
		  $(this).addClass('active').siblings().removeClass('active');
		  $(this).parents('.onlinetest-wp').animate({marginLeft:'-='+_this_section_width},500);
		});
		$('.closetest').click(function(){
		  $('#onlinetestModal').modal('hide');
		  player.play();
		});
	};
	//获取播放进度
	var getCurPos = function(){
	  	//将当前实际的播放进度保存到cookie
	  	var cur_time = player.currentTime();
	  	if (cur_time && !player.paused()){
	  		$.cookie(('lesson_' + _id_lesson), cur_time, {expires: 7});
	  		//判断视频是否播放到整体进度的95%
	  		if ((cur_time/player.duration() > 0.95) && !is_poppup_exam){
				v5_popover_tpl('v5-popover-test','popover_test',
					'popover-test-container','bottom','manual');
				$("#popover_test").removeClass('hidden');
				$('.popover-test-container').popover('show');
				is_poppup_exam = true;
				$('.start-test').click(function(event){
				  event.preventDefault();
				  $('.popover-test-container').popover('hide');
				  onlinetest();
				});                  
				v5_popover_tpl('v5-popover-ewm','ewm','downloadv','bottom','hover');		
	  		}
	  	}
	  	setTimeout(getCurPos, 5000);	
	};
	//空格键暂停播放
	var tag = player.L;
	var doc = tag.ownerDocument || document;
	$(".course-play-box").on("focus",function(){
		
		$(doc).on('keydown', function (e) {
		    if (32 == e.keyCode) {
		    	e.preventDefault();
		        if (player.paused()) {
		            player.play();
		        } else {
		            player.pause();
		        }
		    }
		});
	});
	$(".course-play-box").on("blur",function(){
		$(doc).off("keydown");
	});
	//鼠标双击全部切换
	$(player.tag || player.L).on('dblclick', function(){
	  if (player.isFullscreen()){
	    player.exitFullscreen();
	  }else{
	    player.requestFullscreen();
	  }
	});
	//左右键快进后退
	$(window).on("keyup",function(e){
	  if(e.keyCode==39)
	      player.currentTime(player.currentTime() + 10);
	  else if(e.keyCode==37)
	      player.currentTime(player.currentTime() - 10);
	});
	var start_from_time = $.cookie('lesson_' + _id_lesson) || 0;
	var check_locker = function(){
		if ($("#playlist li.active_null a.active").next().hasClass('v5-icon-lock')) {
		    player.pause();
		    $('#loginModal').modal('show');
		    return false;
		}	
	};
	player.on(["play"], check_locker);
	player.ready(function(){
		player.currentTime(start_from_time);
		//check locker
		player.play();
		//check time

	});
	player.on("durationchange",function(){
		getCurPos();
	});
	//上传作业
	var uploading = false;
	var zysub=function(str,n){
	    var r=/[^\x00-\xff]/g;
	    if(str.replace(r,"mm").length<=n){return str;}
	    var m=Math.floor(n/2);
	    for(var i=m;i<str.length;i++){
	        if(str.substr(0,i).replace(r,"mm").length>=n){
	            return str.substr(0,i)+"...";
	        }
	    }
	    return str;
	};
	//on ended
	player.on("ended", function () {
	    // getPlayPostion();
	    $.cookie('lesson_' + _id_lesson, null);

	    if (uploading) {
	        return;
	    }

	    $("#playlist .active_null").nextAll().find("a").each(function () {
	        var lesson_id = $(this).attr("lessonId");
	        if (lesson_id)
	            location.href = "/lesson/" + lesson_id;
	        return false;
	    });
	});
		//init time
	//upload 
	$('#file_upload').fileupload({
	    dropZone: null,
	    url: '/lesson/student/job/upload/',
	    formData: {'lesson_id': _id_lesson, 'enctype':"multipart/form-data",},
	    add: function (e, data) {
	        var uploadErrors = [];
	        var acceptFileTypes = /^(zip|rar)$/i;
	        var filesize = data.originalFiles[0].size / (1024) / (1024);
	        Ntype = data.originalFiles[0].name;
	        Ntype = Ntype.substring(Ntype.length - 3, Ntype.length);
	        if (!acceptFileTypes.test(Ntype)) {
	            $("#submit .tips-error").html("文件格式不正确（zip，rar）").show().delay(3000).fadeOut();
	            uploadErrors.push('Not an accepted file type');
	        }
	        if (parseInt(filesize) > 10) {
	            $("#submit .tips-error").html("文件超过10M大小").show().delay(3000).fadeOut();
	            uploadErrors.push('Filesize is too big');
	        }
	        if (uploadErrors.length === 0) {
	            uploading = true;
	            data.submit();
	        }
	    },
	    dataType: 'json',
	    autoUpload: true,
	    done: function (e, data) {
		    $('.job-sub .sub-work > span').html('重新上传');
	        $('.work-pro').delay(1000).fadeOut();
	        $("#submit .success-msg").show().delay(1000).fadeOut();
	        uploading = false;
	    },
	    progressall: function (e, data) {
	        var progress = parseInt(data.loaded / data.total * 100, 10);
	        $('.work-pro').show();
	        $('#progress .progress-bar').css(
	                'width',
	                progress + '%'
	        );
	        $('#progress .progress-bar').html(progress + '%');
	    }
	}).prop('disabled', !$.support.fileInput).parent().addClass($.support.fileInput ? undefined : 'disabled');

	

  //播放列表滚动条
  $('.scroll-pane').jScrollPane({
      autoReinitialise: true
    });
  //二维码
  $('#code').qrcode({
    height:120,
    width:120,
    text:"www.maiziedu.com",
    background:"#f1f1f1",
    foreground:"#000000",
  });

// Add X-CSRFToken to POSTData 
	var csrftoken = getCookie('csrftoken');
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});

	// reply
	$(".media-list").on("click", ".reply", function(){
		event.preventDefault();
		var $lm = $(this).closest("li.media");
		var $m = $lm.find(".media").last();
		var text = "回复" + $(this).siblings(".user-name").text().trim() + ":";
		$m.removeClass("hidden").find(".comment-input .form-control").val(text).focus();
	});

	$(".media-list").on("click", ".close-btn", function(){
		event.preventDefault();
		$(this).closest(".media").addClass("hidden");
	});

	$(".no-reply").on("click", function(){
		event.preventDefault();
		$('#loginModal').modal('show');
	});
	//提交课时评论

	$("#comm").on("click",".comment-input .btn", function(){
		var $text_entry = $(this).parent().siblings('.form-control');
		var comment = $text_entry.val();
		var pat = /^回复.+:$/;
		if (!comment.trim() || pat.test(comment)) return false;
		var pid = $(this).closest("li.media").attr("id");
		var lid = $(".active_null .active").attr("lessonId");
		$.ajax({
			cache: false,
			type: "post",
			url: "/course/add/comment/",
			data:{
				"parent_id":pid,
				"lesson_id":lid,
				"comment":comment,
			},
			success:function(data){
				$text_entry.val("");
				$.get("/lesson/" + lid + "/comment/",
					function(data, status){
						if (status=="success"){
							$("ul.media-list").html(data);
						}

					});
			}

		});
	});
	
});