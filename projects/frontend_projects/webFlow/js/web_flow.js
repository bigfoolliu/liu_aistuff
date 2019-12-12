//<script type="text/javascript">
createDiv()

//创建每一个div卡片
function createDiv() {
	for(var i = 0; i < 20; i++) {
		var div = document.createElement('div'); //创建div
		var rnd = Math.floor(Math.random() * 600 + 400) //div的高度在50到350之间
		div.style.height = rnd + "px";
		div.innerHTML = i; //内部镶嵌的标签
		document.body.appendChild(div); //将div存到body里
	};
	change() //自适应窗口的大小
}

//自适应窗口的大小
function change() {
	var aDiv = document.getElementsByTagName('div');
//	 alert(aDiv.length);
	var windowCW = document.documentElement.clientWidth; //窗口视口的宽度
//	alert(windowCW)
	var n = Math.floor(windowCW / 420); //一行能容纳多少个div，并向下取整
	if(n <= 0) {
		return
	};
//	 alert(n);
	var t = 0;
	var center = (windowCW - n * 420) / 2; //居中
	var arrH = []; //定义一个数组存放div的高度
	//遍历每一个div
	for(var i = 0; i < aDiv.length; i++) {
		var j = i % n;

		if(arrH.length == n) { //一行排满n个后到下一行                    
			var min = findMin(arrH); //从最“矮”的排起，可以从下图的序号中看得出来，下一行中序号是从矮到高排列的
			aDiv[i].style.left = center + min * 420 + "px";
			aDiv[i].style.top = arrH[min] + 10 + "px";
			arrH[min] += aDiv[i].offsetHeight + 10;
			// alert(min);
		} else {
			arrH[j] = aDiv[i].offsetHeight;
			aDiv[i].style.left = center + 420 * j + 10 * j + "px";
			aDiv[i].style.top = 0;
		}

	};
}
window.onresize = function() { //窗口改变也调用函数  
	change();
}
window.onscroll = function() {
	// 页面总高度
	var bodyHeight = document.documentElement.offsetHeight;
	// 可视区高度
	var windowHeight = document.documentElement.clientHeight;
	//滚动条的高度    
	var srcollTop = document.documentElement.scrollTop || document.body.scrollTop;
	var srcollH = document.body.scrollHeight;
	// alert(srcollH);
	if(srcollTop + windowHeight >= srcollH - 20) {
		createDiv();
	};
}

//找到一行当中高度最小的
function findMin(arr) {
	var m = 0;
	for(var i = 0; i < arr.length; i++) {
		m = Math.min(arr[m], arr[i]) == arr[m] ? m : i;
	}
	return m;
}
//</script>