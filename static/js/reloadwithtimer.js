function runSlideShow(img,width,height,interval) {
    jQuery(img).fadeSlideShow({
		width: width, // default width of the slideshow
		height: height, // default height of the slideshow
		speed: 'slow', // default animation transition speed
		interval: interval, // default interval between image change
		PlayPauseElement: false, // default css id for the play / pause element
		PlayText: false, // default play text
		PauseText: false, // default pause text
		NextElement: false, // default id for next button
		NextElementText: false, // default text for next button
		PrevElement: false, // default id for prev button
		PrevElementText: false, // default text for prev button
		ListElement: false, // default id for image / content controll list
		ListLi: false, // default class for li's in the image / content controll 
		ListLiActive: false, // default class for active state in the controll list
		addListToId: false, // add the controll list to special id in your code - default false
		allowKeyboardCtrl: false, // allow keyboard controlls left / right / space
		autoplay: true // autoplay the slideshow
    });
};


$(function() {

	console.log(screen.width)
	if (screen.width <= 480) {
		runSlideShow('#img1',271,177,6000);
		runSlideShow('#img2',271,177,5000);
		runSlideShow('#img3',271,382,7000);
	} else if (screen.width <= 1024) {
		runSlideShow('#img1',462,379,6000);
		runSlideShow('#img2',462,379,5000);
		runSlideShow('#img3',462,758,7000);
	} else  {
		runSlideShow('#img1',610,379,6000);
		runSlideShow('#img2',610,379,5000);
		runSlideShow('#img3',610,758,7000);
	}
});
