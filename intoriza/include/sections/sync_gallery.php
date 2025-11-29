<div class="wt-box wt-product-gallery on-show-slider"> 
    <div id="sync1" class="owl-carousel owl-theme owl-btn-vertical-center m-b5">
        <div class="item">
            <div class="mfp-gallery">
                <div class="wt-box">
                    <div class="wt-thum-bx">
                        <img src="<?php echo $path; ?>images/gallery/portrait-2/pic1.jpg" alt="">
                    </div>
                </div>
            </div>
        </div>
        <div class="item">
            <div class="mfp-gallery">
                <div class="wt-box">
                    <div class="wt-thum-bx">
                        <img src="<?php echo $path; ?>images/gallery/portrait-2/pic2.jpg" alt="">
                    </div>
                </div>
            </div>
        </div>
        <div class="item">
            <div class="mfp-gallery">
                <div class="wt-box">
                    <div class="wt-thum-bx">
                        <img src="<?php echo $path; ?>images/gallery/portrait-2/pic3.jpg" alt="">
                    </div>
                </div>
            </div>
        </div>
        <div class="item">
            <div class="mfp-gallery">
                <div class="wt-box">
                    <div class="wt-thum-bx">
                        <img src="<?php echo $path; ?>images/gallery/portrait-2/pic4.jpg" alt="">
                    </div>
                </div>
            </div>
        </div>
        <div class="item">
            <div class="mfp-gallery">
                <div class="wt-box">
                    <div class="wt-thum-bx">
                        <img src="<?php echo $path; ?>images/gallery/portrait-2/pic5.jpg" alt="">
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div id="sync2" class="owl-carousel owl-theme">
        <div class="item">
            <div class="wt-media">
                <img src="<?php echo $path; ?>images/gallery/thumb/pic1.jpg" alt="">
            </div>
        </div>
        <div class="item">
            <div class="wt-media">
                <img src="<?php echo $path; ?>images/gallery/thumb/pic2.jpg" alt="">
            </div>
        </div>
        <div class="item">
            <div class="wt-media">
                <img src="<?php echo $path; ?>images/gallery/thumb/pic3.jpg" alt="">
            </div>
        </div>
        <div class="item">
            <div class="wt-media">
                <img src="<?php echo $path; ?>images/gallery/thumb/pic4.jpg" alt="">
            </div>
        </div>
        <div class="item">
            <div class="wt-media">
                <img src="<?php echo $path; ?>images/gallery/thumb/pic5.jpg" alt="">
            </div>
        </div>
    </div>
</div>

<script>
jQuery(document).ready(function() {
  var sync1 = $("#sync1");
  var sync2 = $("#sync2");
  var slidesPerPage = 4; //globaly define number of elements per page
  var syncedSecondary = true;

  sync1.owlCarousel({
    items : 1,
    slideSpeed : 2000,
    nav: true,
    autoplay: true,
    dots: false,
    loop: true,
    responsiveRefreshRate : 200,
    navText: ['<i class="fa fa-chevron-left"></i>', '<i class="fa fa-chevron-right"></i>'],
  }).on('changed.owl.carousel', syncPosition);

  sync2
    .on('initialized.owl.carousel', function () {
      sync2.find(".owl-item").eq(0).addClass("current");
    })
    .owlCarousel({
    items : slidesPerPage,
    dots: false,
    nav: false,
    margin:5,
    smartSpeed: 200,
    slideSpeed : 500,
    slideBy: slidesPerPage, 
    responsiveRefreshRate : 100
  }).on('changed.owl.carousel', syncPosition2);

  function syncPosition(el) {
    var count = el.item.count-1;
    var current = Math.round(el.item.index - (el.item.count/2) - .5);
    
    if(current < 0) {
      current = count;
    }
    if(current > count) {
      current = 0;
    }
    
    //end block

    sync2
      .find(".owl-item")
      .removeClass("current")
      .eq(current)
      .addClass("current");
    var onscreen = sync2.find('.owl-item.active').length - 1;
    var start = sync2.find('.owl-item.active').first().index();
    var end = sync2.find('.owl-item.active').last().index();
    
    if (current > end) {
      sync2.data('owl.carousel').to(current, 100, true);
    }
    if (current < start) {
      sync2.data('owl.carousel').to(current - onscreen, 100, true);
    }
  }
  
  function syncPosition2(el) {
    if(syncedSecondary) {
      var number = el.item.index;
      sync1.data('owl.carousel').to(number, 100, true);
    }
  }
  
  sync2.on("click", ".owl-item", function(e){
    e.preventDefault();
    var number = $(this).index();
    sync1.data('owl.carousel').to(number, 300, true);
  });
});
</script>
