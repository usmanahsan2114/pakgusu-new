<!DOCTYPE html>
<html lang="en">

<head>

	<!-- META -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="keywords" content="" />
    <meta name="author" content="" />
    <meta name="robots" content="" />    
    <meta name="description" content="" />
    
    <!-- FAVICONS ICON -->
    <link rel="icon" href="images/favicon.ico" type="image/x-icon" />
    <link rel="shortcut icon" type="image/x-icon" href="images/favicon.png" />
    
    <!-- PAGE TITLE HERE -->
    <title>intoriza Template | Home Page Style 2</title>
    
    <!-- MOBILE SPECIFIC -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <link rel="stylesheet" href="css/bootstrap.min.css"><!-- BOOTSTRAP STYLE SHEET -->
    <link rel="stylesheet" href="css/fontawesome/css/font-awesome.min.css" /><!-- FONTAWESOME STYLE SHEET -->
    <link rel="stylesheet" href="css/owl.carousel.min.css"><!-- OWL CAROUSEL STYLE SHEET -->
    <link rel="stylesheet" href="css/magnific-popup.min.css"><!-- MAGNIFIC POPUP STYLE SHEET -->
    <link rel="stylesheet" href="css/loader.min.css"><!-- LOADER STYLE SHEET -->    
    <link rel="stylesheet" href="css/style.css"><!-- MAIN STYLE SHEET -->
    <link rel="stylesheet" href="css/flaticon.min.css"><!-- FLATICON STYLE SHEET -->
    <link rel="stylesheet" href="css/skin/skin-1.css" class="skin"><!-- THEME COLOR CHANGE STYLE SHEET -->
     

    <!-- REVOLUTION SLIDER CSS -->
    <link rel="stylesheet" type="text/css" href="plugins/revolution/revolution/css/settings.css">
    <!-- REVOLUTION NAVIGATION STYLE -->
    <link rel="stylesheet" type="text/css" href="plugins/revolution/revolution/css/navigation.css">
 	 <!-- BEFORE/AFTER ADD-ON FILES  MUST BE INSERTED AFTER THE SLIDER DOM ELEMENTS !-->
	<link rel='stylesheet' href='plugins/revolution/revolution-addons/beforeafter/css/revolution.addon.beforeafter.css' type='text/css' media='all' />	    
    
    <!-- GOOGLE FONTS -->
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,300i,400,400i,500,500i,600,600i,700,800,800i,900" rel="stylesheet"> 
    <link href="https://fonts.googleapis.com/css?family=Martel:200,300,400,600,700,800,900" rel="stylesheet"> 

</head>

<body>

	<div class="page-wraper"> 
       	
        <!-- HEADER START -->
        <header class="site-header header-style-1  nav-wide  mobile-sider-drawer-menu">
            <div class="sticky-header main-bar-wraper">
                <div class="main-bar bg-white">
                    <div class="container header-center">
                        <div class="wt-header-left">
                            <div class="logo-header">
                                <div class="logo-header-inner logo-header-one">
                                    <a href="index.php">
                                        <img src="images/logo-dark.png" width="171" height="49" alt="" />
                                    </a>
                                </div>
                            </div>
                        </div>
                        <div class="wt-header-center"> 
                             <!-- NAV Toggle Button -->
                            <button id="mobile-side-drawer" data-target=".header-nav" data-toggle="collapse" type="button" class="navbar-toggler collapsed">
                                <span class="sr-only">Toggle navigation</span>
                                <span class="icon-bar icon-bar-first"></span>
                                <span class="icon-bar icon-bar-two"></span>
                                <span class="icon-bar icon-bar-three"></span>
                            </button>                       
                            <!-- MAIN Vav -->
                            <div class="header-nav navbar-collapse collapse nav-dark">
                                <ul class=" nav navbar-nav nav-line-animation">
                                    <li class="active">
                                    	<a href="index.php" >Home</a>
                                    </li>
                                    <li>
                                        <a href="about/index.php">About</a>
                                        <ul class="sub-menu">
                                            <li><a href="<?php echo $path; ?>about/pak-gusu/index.php">About Pak Gusu</a></li>
                                            <li><a href="<?php echo $path; ?>about/gusu-china/index.php">About GUSU China</a></li>
                                            <li><a href="<?php echo $path; ?>about/cleanroom-standards/index.php">Cleanroom Standards</a></li>
                                        </ul>
                                    </li>
                                    <li>
                                        <a href="javascript:;">Products</a>
                                        <ul class="sub-menu">
                                            <li><a href="products/clean-room-panels/index.php">Clean Room Panels</a></li>
                                            <li><a href="products/windows/index.php">Windows</a></li>
                                            <li><a href="products/doors/index.php">Doors</a></li>
                                            <li><a href="products/transfer-window/index.php">Transfer Window</a></li>
                                            <li><a href="products/aluminum-profile/index.php">Aluminum Profile</a></li>
                                            <li><a href="products/clean-led-lights/index.php">Clean LED Lights</a></li>
                                        </ul>
                                    </li>
                                    <li>
                                        <a href="javascript:;">Services</a>
                                        <ul class="sub-menu">
                                            <li><a href="services/planning-design/index.php">Planning & Design</a></li>
                                            <li><a href="services/clean-room-construction/index.php">Clean Room Construction</a></li>
                                            <li><a href="services/installation/index.php">Installation</a></li>
                                            <li><a href="services/after-sale-services/index.php">After Sale Services</a></li>
                                        </ul>
                                    </li>
                                    <li>
                                        <a href="javascript:;">Sectors</a>
                                        <ul class="sub-menu">
                                            <li><a href="sectors/pharmaceutical/index.php">Pharmaceutical</a></li>
                                            <li><a href="sectors/hospital/index.php">Hospital</a></li>
                                            <li><a href="sectors/food-industry/index.php">Food Industry</a></li>
                                            <li><a href="sectors/electronics/index.php">Electronics</a></li>
                                            <li><a href="sectors/laboratories/index.php">Laboratories</a></li>
                                            <li><a href="sectors/medical-devices/index.php">Medical Devices</a></li>
                                        </ul>
                                    </li>
                                    <li>
                                        <a href="blog/index.php">Blog</a>
                                    </li>
                                    <li>
                                        <a href="portfolio/index.php">Portfolio</a>
                                    </li>
                                    <li>
                                        <a href="contact/index.php">Contact</a>
                                    </li>                               
                                </ul>
                            </div>
                        </div>
                        <div class="wt-header-right ">
                            <div class="site-bg-primary wt-header-right-child">
                                <!-- ETRA Nav -->
                                <div class="extra-nav">
                                    <div class="extra-cell">
                                        <a href="#search" class="site-search-btn"><i class="fa fa-search"></i></a>
                                    </div>
                                 </div>                                 
                                <!-- ETRA Nav -->
                                <div class="extra-nav">
                                    <div class="extra-cell">
                                        <div class="right-arrow-btn">
                                            <button type="button" class="btn-open contact-slide-show text-white notification-animate"><i class="fa fa-angle-left"></i></button>
                                        </div>                                         
                                    </div>
                                 </div>
                             </div>                                 
                       </div>  
                        <!-- Contact Nav -->                            
                        <div class="contact-slide-hide"> 
                            <div class="contact-nav">
                                 <a href="javascript:void(0)" class="contact_close">&times;</a>
                                 <div class="contact-nav-form p-a30">
                                    <form class="cons-contact-form" method="post" action="form-handler.php">
                                        <div class="m-b30">
                                            <!-- TITLE START -->
                                            <div class="section-head text-left">
                                                <h4 class="m-b5">Get In Touch</h4>
                                            </div>
                                            <!-- TITLE END --> 
                                            <div class="input input-animate">
                                                <label for="name">Name</label>
                                                <input type="text" name="username"  id="name" required>
                                                <span class="spin"></span>
                                            </div>
                                            <div class="input input-animate">
                                                <label for="email">Email</label>
                                                <input type="email" name="email"   id="email" required>
                                                <span class="spin"></span>
                                            </div>                                            
                                            <div class="input input-animate">
                                                <label for="message">Textarea</label>
                                                <textarea name="message"  id="message" required></textarea>
                                                <span class="spin"></span>
                                            </div>
                                            <div class="text-right">
                                                <button name="submit" type="submit" value="Submit" class="btn-half site-button m-b15">
                                                      <span>Submit</span>
                                                </button>
                                            </div>
                                        </div>
                                    </form>
                                    <div class="contact-info text-black m-b30">
                                        <!-- TITLE START -->
                                        <div class="section-head text-left">
                                            <h4 class="m-b5">Contact Info</h4>
                                        </div>
                                        <!-- TITLE END --> 
                                        <div class="wt-icon-box-wraper left p-b40 icon-shake-outer">
                                            <div class="icon-xs"><i class="flaticon-smartphone  icon-shake"></i></div>
                                            <div class="icon-content">
                                                <h5 class="m-t0 font-weight-500">Phone number</h5>
                                                <p>(456) 789 10 12</p>
                                            </div>
                                        </div>
                                        <div class="wt-icon-box-wraper left p-b40 icon-shake-outer">
                                            <div class="icon-xs"><i class="flaticon-email  icon-shake"></i></div>
                                            <div class="icon-content">
                                                <h5 class="m-t0 font-weight-500">Email address</h5>
                                                <p>demo@gmail.com</p>
                                            </div>
                                        </div>
                                        <div class="wt-icon-box-wraper left icon-shake-outer">
                                            <div class="icon-xs"><i class="flaticon-placeholder  icon-shake"></i></div>
                                            <div class="icon-content">
                                                <h5 class="m-t0 font-weight-500">Address info</h5>
                                                <p>55/11 Land Street, Modern New Yourk City, USA</p>
                                            </div>
                                        </div>
                                    </div>                                        
                                 </div>
                            </div> 
                        </div>       
                         <!-- Search popup -->
                        <div id="search"> 
                            <span class="close"></span>
                            <form role="search" id="searchform" action="/search" method="get" class="radius-xl">
                                <div class="input-group">
                                    <input value="" name="q" type="search" placeholder="Type to search"/>
                                    <span class="input-group-btn"><button type="button" class="search-btn"><i class="fa fa-search"></i></button></span>
                                </div>   
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <!-- HEADER END -->

        <!-- CONTENT START -->
        <div class="page-content"> 
               
            <!-- SLIDER START -->
            <div id="rev_slider_346_1_wrapper" class="rev_slider_wrapper fullscreen-container" data-alias="beforeafterslider1" data-source="gallery" style="background:#252525;padding:0px;">
                <!-- START REVOLUTION SLIDER 5.4.3.3 fullscreen mode -->
                <div id="rev_slider_346_1" class="rev_slider fullscreenbanner" style="display:none;" data-version="5.4.3.3">
                    <ul>	
                    	<!-- SLIDE 1 -->
                        <li data-index="rs-964" data-transition="fade" data-slotamount="default" data-hideafterloop="0" data-hideslideonmobile="off" data-easein="default" data-easeout="default" data-masterspeed="default" data-thumb="" data-rotate="0" data-saveperformance="off" data-title="Slide" data-param1="" data-param2="" data-param3="" data-param4="" data-param5="" data-param6="" data-param7="" data-param8="" data-param9="" data-param10="{&quot;revslider-weather-addon&quot; : { &quot;type&quot; : &quot;&quot; ,&quot;name&quot; : &quot;&quot; ,&quot;woeid&quot; : &quot;&quot; ,&quot;unit&quot; : &quot;&quot; }}" data-description="" data-beforeafter='{"moveto":"50%|50%|50%|50%","bgColor":"#e7e7e7","bgType":"image","bgImage":"images/main-slider/slider3/slide1.jpg","bgFit":"cover","bgPos":"center center","bgRepeat":"no-repeat","direction":"horizontal","easing":"Power2.easeInOut","delay":"500","time":"750","out":"fade","carousel":false}'>
                            <!-- MAIN IMAGE -->
                            <img src="images/main-slider/slider3/slide1-b.jpg" data-beforeafter="after"  data-bgcolor=''  alt=""  data-bgposition="center center" data-bgfit="cover" data-bgrepeat="no-repeat" data-bgparallax="off" class="rev-slidebg" data-no-retina>
                            <!-- LAYERS -->
                            
                            <!-- LAYER NR. 1 text -->
                            <div class="tp-caption   tp-resizeme rs-parallaxlevel-5" 
                                id="slide-964-layer-1" 
                                data-x="['center','center','center','center']" data-hoffset="['0','0','0','0']" 
                                data-y="['middle','middle','middle','middle']" data-voffset="['200','200','200','0']" 
                                data-fontsize="['120','120','120','60']"
                                data-lineheight="['120','120','120','60']"
                                data-letterspacing="['50','50','50','30']"
                                
                                data-height="none"
                                data-whitespace="normal"
                            
                                data-type="text" 
                                data-beforeafter="before" 
                                data-responsive_offset="on" 
                            
                                data-frames='[{"delay":600,"speed":2000,"frame":"0","from":"sX:1;sY:1;opacity:0;fb:40px;","to":"o:1;fb:0;","ease":"Power4.easeInOut"},
                                {"delay":"wait","speed":300,"frame":"999","to":"opacity:0;fb:0;","ease":"Power3.easeInOut"}]'
                                data-textAlign="['center','center','center','center']"
                                data-paddingtop="[0,0,0,0]"
                                data-paddingright="[0,0,0,0]"
                                data-paddingbottom="[0,0,0,0]"
                                data-paddingleft="[50,50,50,50]"
                            
                                style="z-index: 16; white-space: nowrap; font-size: 120px; line-height: 120px; font-weight: 700; color: #000; letter-spacing: 50px;font-family: 'Martel', serif;text-transform:uppercase;">intoriza</div>
                            <!-- LAYER NR. 2 text -->
                            <div class="tp-caption   tp-resizeme rs-parallaxlevel-5" 
                                id="slide-964-layer-2" 
                                data-x="['center','center','center','center']" data-hoffset="['0','0','0','0']" 
                                data-y="['middle','middle','middle','middle']" data-voffset="['300','300','300','100']" 
                                data-width="['960','960','960','320']"
                                data-height="none"
                                data-whitespace="normal"
                            
                                data-type="text" 
                                data-beforeafter="before" 
                                data-responsive_offset="on" 
                            
                                data-frames='[{"delay":600,"speed":2000,"frame":"0","from":"sX:1;sY:1;opacity:0;fb:40px;","to":"o:1;fb:0;","ease":"Power4.easeInOut"},
                                {"delay":"wait","speed":300,"frame":"999","to":"opacity:0;fb:0;","ease":"Power3.easeInOut"}]'
                                data-textAlign="['center','center','center','center']"
                                data-paddingtop="[0,0,0,0]"
                                data-paddingright="[0,0,0,0]"
                                data-paddingbottom="[0,0,0,0]"
                                data-paddingleft="[5,5,5,5]"
                            
                                style="z-index: 11; min-width: 960px; max-width: 960px; white-space: normal; font-size: 13px; line-height: 20px; font-weight: 400; color: #000; letter-spacing: 5px;font-family:Montserrat;text-transform:uppercase;">Exceptional designing for exceptional Spaces.</div>
                        
                            <!-- SLIDE RIGHT PART START-->
                            
                            <!-- LAYER NR. 1  text-->
                            <div class="tp-caption   tp-resizeme  tp-blackshadow rs-parallaxlevel-5" 
                                id="slide-964-layer-4" 
                                data-x="['center','center','center','center']" data-hoffset="['0','0','0','0']" 
                                data-y="['middle','middle','middle','middle']" data-voffset="['200','200','200','0']" 
                                data-fontsize="['120','120','120','60']"
                                data-lineheight="['120','120','120','60']"
                                data-letterspacing="['50','50','50','30']"
                                data-width="none"
                                data-height="none"
                                data-whitespace="nowrap"
                            
                                data-type="text" 
                                data-beforeafter="after" 
                                data-responsive_offset="on" 
                            
                                data-frames='[{"delay":2000,"speed":2000,"frame":"0","from":"sX:1;sY:1;opacity:0;fb:40px;","to":"o:1;fb:0;","ease":"Power4.easeInOut"},
                                {"delay":"wait","speed":300,"frame":"999","to":"opacity:0;fb:0;","ease":"Power3.easeInOut"}]'
                                data-textAlign="['center','center','center','center']"
                                data-paddingtop="[0,0,0,0]"
                                data-paddingright="[0,0,0,0]"
                                data-paddingbottom="[0,0,0,0]"
                                data-paddingleft="[50,50,50,50]"
                            
                            
                                style="z-index: 16; white-space: nowrap; font-size: 120px; line-height: 120px; font-weight: 700; color: #ffffff; letter-spacing: 50px;font-family: 'Martel', serif;text-transform:uppercase;">intoriza</div>
                            
                            <!-- LAYER NR. 2 text -->
                            <div class="tp-caption   tp-resizeme rs-parallaxlevel-5" 
                                id="slide-964-layer-5" 
                                data-x="['center','center','center','center']" data-hoffset="['0','0','0','0']" 
                                data-y="['middle','middle','middle','middle']" data-voffset="['300','300','300','100']" 
                                data-width="['960','960','960','320']"
                                data-height="none"
                                data-whitespace="normal"
                            
                                data-type="text" 
                                data-beforeafter="after" 
                                data-responsive_offset="on" 
                            
                                data-frames='[{"delay":2100,"speed":2000,"frame":"0","from":"sX:1;sY:1;opacity:0;fb:40px;","to":"o:1;fb:0;","ease":"Power4.easeInOut"},
                                {"delay":"wait","speed":300,"frame":"999","to":"opacity:0;fb:0;","ease":"Power3.easeInOut"}]'
                                data-textAlign="['center','center','center','center']"
                                data-paddingtop="[0,0,0,0]"
                                data-paddingright="[0,0,0,0]"
                                data-paddingbottom="[0,0,0,0]"
                                data-paddingleft="[5,5,5,5]"
                            
                                style="z-index: 17; min-width: 960px; max-width: 960px; white-space: normal; font-size: 13px; line-height: 20px; font-weight: 400; color: #ffffff; letter-spacing: 5px;font-family:Montserrat;text-transform:uppercase;">Exceptional designing for exceptional Spaces.
                            </div>
                            
                            <!-- LAYER NR. 3  button-->
                    
                        </li>
                
                    </ul>
                    <div class="tp-bannertimer tp-bottom" style="visibility: hidden !important;"></div>	
                </div>
            </div>
            <!-- SLIDER END -->
          
            <!-- COMPANY OVERVIEW START -->
            <?php include('include/sections/company_overview.php'); ?>
            <!-- COMPANY OVERVIEW END -->

            <!-- PRODUCT HIGHLIGHTS START -->
            <?php include('include/sections/product_highlights.php'); ?>
            <!-- PRODUCT HIGHLIGHTS END --> 
            
            <!-- WHAT WE DO SECTION START -->
            <div class="section-full p-t80 p-b50 bg-gray">
                <div class="container">
                    <!-- TITLE START -->
                    <div class="section-head text-center">
                        <div class="wt-separator-outer separator-center">
                            <div class="wt-separator">
                                <span class="site-text-primary text-uppercase sep-line-one ">what you prefer</span>
                            </div>
                        </div>
                        <h2>What we do</h2>
                    </div>
                    <!-- TITLE END -->
                    <div class="section-content">
                    	<div class="row">
                            <div class="col-md-4 col-sm-6 col-xs-6 col-xs-100pc m-b30">
                            	<div class="hover-box-effect  v-icon-effect">
                                    <div class="wt-box">
                                        <div class="wt-thum-bx wt-img-effect fade-in">
                                            <img src="images/gallery/pic1.jpg" alt="">
											<div class="wt-icon-box-sm bg-white">
                                                <span class="icon-cell site-text-primary"><i class="v-icon flaticon-sketch"></i></span>
                                            </div>                                            
                                        </div>
                                    	<div class="p-a20 bg-white">
                                            <div class="icon-content text-black">
                                                <h4 class="wt-tilte m-b25">Planning</h4>
                                                <p>Lorem ipsum dolor sit amet, iusto quando  vocibus te vim no mea.</p>
                                                <a href="<?php echo $path; ?>services/index.php" class="site-button-link" data-hover="Read More">Read More</a>
                                            </div>
                                        </div>                                        
                                    </div>
                                </div>
                            </div>                          
                            <div class="col-md-4 col-sm-6 col-xs-6 col-xs-100pc m-b30">
                            	<div class="hover-box-effect  v-icon-effect">
                                    <div class="wt-box">
                                        <div class="wt-thum-bx wt-img-effect fade-in">
                                            <img src="images/gallery/pic2.jpg" alt="">
											<div class="wt-icon-box-sm bg-white">
                                                <span class="icon-cell site-text-primary"><i class="v-icon flaticon-window"></i></span>
                                            </div>                                            
                                        </div>
                                    	<div class="p-a20 bg-white">
                                            <div class="icon-content text-black">
                                                <h4 class="wt-tilte m-b25">Interior</h4>
                                                <p>Lorem ipsum dolor sit amet, iusto quando  vocibus te vim no mea.</p>
                                                <a href="<?php echo $path; ?>services/index.php" class="site-button-link" data-hover="Read More">Read More</a>
                                            </div>
                                        </div>                                        
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-4 col-sm-6 col-xs-6 col-xs-100pc m-b30">
                            	<div class="hover-box-effect  v-icon-effect">
                                    <div class="wt-box">
                                        <div class="wt-thum-bx wt-img-effect fade-in">
                                            <img src="images/gallery/pic3.jpg" alt="">
											<div class="wt-icon-box-sm bg-white">
                                                <span class="icon-cell site-text-primary"><i class="v-icon flaticon-window-5"></i></span>
                                            </div>                                            
                                        </div>
                                    	<div class="p-a20 bg-white">
                                            <div class="icon-content text-black">
                                                <h4 class="wt-tilte m-b25">Exterior</h4>
                                                <p>Lorem ipsum dolor sit amet, iusto quando  vocibus te vim no mea.</p>
                                                <a href="<?php echo $path; ?>services/index.php" class="site-button-link" data-hover="Read More">Read More</a>
                                            </div>
                                        </div>                                        
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-4 col-sm-6 col-xs-6 col-xs-100pc m-b30">
                            	<div class="hover-box-effect  v-icon-effect">
                                    <div class="wt-box">
                                        <div class="wt-thum-bx wt-img-effect fade-in">
                                            <img src="images/gallery/pic4.jpg" alt="">
											<div class="wt-icon-box-sm bg-white">
                                                <span class="icon-cell site-text-primary"><i class="v-icon flaticon-plant"></i></span>
                                            </div>                                            
                                        </div>
                                    	<div class="p-a20 bg-white">
                                            <div class="icon-content text-black">
                                                <h4 class="wt-tilte m-b25">Decoration</h4>
                                                <p>Lorem ipsum dolor sit amet, iusto quando  vocibus te vim no mea.</p>
                                                <a href="<?php echo $path; ?>services/index.php" class="site-button-link" data-hover="Read More">Read More</a>
                                            </div>
                                        </div>                                        
                                    </div>
                                </div>
                            </div>                          
                            <div class="col-md-4 col-sm-6 col-xs-6 col-xs-100pc m-b30">
                            	<div class="hover-box-effect  v-icon-effect">
                                    <div class="wt-box">
                                        <div class="wt-thum-bx wt-img-effect fade-in">
                                            <img src="images/gallery/pic5.jpg" alt="">
											<div class="wt-icon-box-sm bg-white">
                                                <span class="icon-cell site-text-primary"><i class="v-icon flaticon-sofa"></i></span>
                                            </div>                                            
                                        </div>
                                    	<div class="p-a20 bg-white">
                                            <div class="icon-content text-black">
                                                <h4 class="wt-tilte m-b25">Furniture</h4>
                                                <p>Lorem ipsum dolor sit amet, iusto quando  vocibus te vim no mea.</p>
                                                <a href="<?php echo $path; ?>services/index.php" class="site-button-link" data-hover="Read More">Read More</a>
                                            </div>
                                        </div>                                        
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-4 col-sm-6 col-xs-6 col-xs-100pc m-b30">
                            	<div class="hover-box-effect  v-icon-effect">
                                    <div class="wt-box">
                                        <div class="wt-thum-bx wt-img-effect fade-in">
                                            <img src="images/gallery/pic6.jpg" alt="">
											<div class="wt-icon-box-sm bg-white">
                                                <span class="icon-cell site-text-primary"><i class="v-icon flaticon-review "></i></span>
                                            </div>                                            
                                        </div>
                                    	<div class="p-a20 bg-white">
                                            <div class="icon-content text-black">
                                                <h4 class="wt-tilte m-b25">Exclusively</h4>
                                                <p>Lorem ipsum dolor sit amet, iusto quando  vocibus te vim no mea.</p>
                                                <a href="<?php echo $path; ?>services/index.php" class="site-button-link" data-hover="Read More">Read More</a>
                                            </div>
                                        </div>                                        
                                    </div>
                                </div>
                            </div>
                        </div>                                
                    </div>
                </div>  
            </div>   
            <!-- WHAT WE DO  SECTION END --> 
                    
            <!-- INDUSTRIES SERVED START -->
            <?php include('include/sections/industries_served.php'); ?>
            <!-- INDUSTRIES SERVED END -->

            <!-- CTA BANNER START -->
            <?php include('include/sections/cta_banner.php'); ?>
            <!-- CTA BANNER END -->                
                                 

        </div>
        <!-- CONTENT END -->
        
        <!-- FOOTER START -->
        <footer class="site-footer footer-large  footer-light	footer-wide">
            
            <!-- FOOTER BLOCKES START -->  
            <div class="footer-top overlay-wraper">
                <div class="overlay-main"></div>
                <div class="container">
                    <div class="text-center">
                    	<div class="footer-link">
                            <ul>
                                <li><a href="about/index.php" data-hover="About">About</a></li>
                                <li><a href="contact/index.php" data-hover="Contact Us">Contact Us</a></li>
                            </ul>
                        </div>
                    </div>
                    <div class="row">
                        <!-- ABOUT COMPANY -->

                        <div class="col-lg-4 col-md-4">  
                            <div class="widget text-center getin-touch">
                                <h4 class="widget-title">Get In Touch</h4>
                                <div class="widget-section">
                                	<ul>
                                        <li>intoriza@gmail.com</li>
                                        <li>(+291) 912-3456-073</li>
                                    </ul>
                                </div>
                            </div>
                     
                        </div> 

                        <!-- TAGS -->
                        <div class="col-lg-4 col-md-4">
                            <div class="widget text-center widget_address m-b20">
                                <h4 class="widget-title">Address</h4>
                                <div class="widget-section">
                                    <ul>
                                        <li>92 Princess Road, parkvenue,Greater London, NW18JR, United Kingdom</li>
                                    </ul>
                                </div>
                                <div class="footer-social-icon">
                           			<ul class="social-icons f-social-link">
                                        <li><a href="javascript:void(0);" class="fa fa-google"></a></li>
                                        <li><a href="javascript:void(0);" class="fa fa-rss"></a></li>
                                        <li><a href="javascript:void(0);" class="fa fa-facebook"></a></li>
                                        <li><a href="javascript:void(0);" class="fa fa-twitter"></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                                                
                        <!-- USEFUL LINKS -->
                        <div class="col-lg-4 col-md-4">
                            <div class="widget text-center">
                                <h4 class="widget-title">Studio</h4>
                                <div class="widget-section">
                                    <ul>
                                        <li><a href="about/index.php">Terms of Condition</a></li>
                                        <li><a href="about/index.php">Privacy Policy</a></li>
                                    </ul>
                                </div>                                
                            </div>                           
                        </div>      

                        <!-- NEWSLETTER -->

                    </div>
                    
                </div>
            </div>
            <!-- FOOTER COPYRIGHT -->
            <div class="footer-bottom overlay-wraper">
                <div class="overlay-main"></div>
                <div class="container">
                    <div class="row">
                        <div class="wt-footer-bot-center">
                            <span class="copyrights-text">© 2024 Your Company. Designed By Thewebmax</span>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
        <!-- FOOTER END -->

        <!-- BUTTON TOP START -->
		<button class="scroltop"><span class="fa fa-angle-up  relative" id="btn-vibrate"></span></button>
        
     


     
    </div>

<!-- LOADING AREA START ===== -->
<div class="loading-area">
    <div class="loading-box"></div>
    <div class="loading-pic">
        <div class="cssload-box-loading"></div>
    </div>
</div>
<!-- LOADING AREA  END ====== -->



<!-- JAVASCRIPT  FILES ========================================= --> 
<script  src="js/jquery-3.7.1.min.js"></script><!-- JQUERY.MIN JS -->
<script  src="js/bootstrap.min.js"></script><!-- BOOTSTRAP.MIN JS -->
<script  src="js/magnific-popup.min.js"></script><!-- MAGNIFIC-POPUP JS -->
<script  src="js/waypoints.min.js"></script><!-- WAYPOINTS JS -->
<script  src="js/counterup.min.js"></script><!-- COUNTERUP JS -->
<script  src="js/waypoints-sticky.min.js"></script><!-- COUNTERUP JS -->
<script  src="js/imagesloaded.pkgd.min.js"></script><!-- MASONRY  -->
<script  src="js/isotope.pkgd.min.js"></script><!-- MASONRY  -->
<script  src="js/owl.carousel.min.js"></script><!-- OWL  SLIDER  -->
<script  src="js/jquery.owl-filter.js"></script>
<script  src="js/custom.js"></script><!-- CUSTOM FUCTIONS  -->
<script  src="js/shortcode.js"></script><!-- SHORTCODE FUCTIONS  -->


<!-- REVOLUTION JS FILES -->

<script  src="plugins/revolution/revolution/js/jquery.themepunch.tools.min.js"></script>
<script  src="plugins/revolution/revolution/js/jquery.themepunch.revolution.min.js"></script>

<!-- SLIDER REVOLUTION 5.0 EXTENSIONS  (Load Extensions only on Local File Systems !  The following part can be removed on Server for On Demand Loading) -->	
<script  src="plugins/revolution/revolution/js/extensions/revolution-plugin.js"></script>
<script  src='plugins/revolution/revolution-addons/beforeafter/js/revolution.addon.beforeafter.min.js'></script>

<!-- REVOLUTION SLIDER SCRIPT FILES -->
<script  src="js/rev-script-2.js"></script>





</body>

</html>
