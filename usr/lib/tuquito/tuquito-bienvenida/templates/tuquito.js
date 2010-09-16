document.onmousedown = new Function("return false");
document.onselectstart = new Function ("return false");
if (window.sidebar) {
	document.onmousedown = new Function("return false");
	document.onclick = new Function("return true");
}

function changeTitle(title) {
	document.title = title;
	document.title = "nop";
}

function closeWindow() {
	if (document.myForm.showDialog.checked == true) {
		changeTitle("event_close_true");
	} else {
		changeTitle("event_close_false");
	}
}

function assessCheckbox() {
	if (document.myForm.showDialog.checked == true) {
		changeTitle("checkbox_checked");
	} else {
		changeTitle("checkbox_unchecked");
	}
}

$(document).ready(function(){
	cont = $("#com").html();
	$("#ajax").hide().html(cont).fadeIn(1800);

	$("#btn_descarga").click(function(){
		cont = $("#doc").html();
		$("#ajax").hide().html(cont).fadeIn();
	});
	$("#btn_donacion").click(function(){
		cont = $("#sop").html();
		$("#ajax").hide().html(cont).fadeIn();
	});
	$("#btn_participar").click(function(){
		cont = $("#pro").html();
		$("#ajax").hide().html(cont).fadeIn();
	});
	$("#btn_exito").click(function(){
		cont = $("#com").html();
		$("#ajax").hide().html(cont).fadeIn();
	});
});
