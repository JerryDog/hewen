// Mav dropdown menu

function nt_nav() {
	/*$('#nt_nav ul').css({display:'none'});*/ // Opera Fix
	$('#nt_nav li').hover(
		function () {
			$(this).find('ul:first').css({display:'none'}).stop(true, true).slideDown(300);
		},
		
		function () {
		
			$(this).find('ul:first').stop(true, true).slideUp(300);
		
		});
}
 
$(document).ready(function() {
	nt_nav();
	});


startList = function() {
	if (document.all&&document.getElementById) {
	
		navRoot = document.getElementById("nav");

		for (i=0; i<navRoot.childNodes.length; i++) {
			node = navRoot.childNodes[i];
			if (node.nodeName == "LI") {
				node.onmouseover = function() {
				this.className+= "over";
  				}
				node.onmouseout = function() {
					this.className = this.className.replace("over", "");
				}
			}
		}
	}
}

window.onload=startList;