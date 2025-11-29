        <!-- HEADER START -->
        <header class="site-header header-style-1  nav-wide  mobile-sider-drawer-menu">
            <div class="sticky-header main-bar-wraper">
                <div class="main-bar bg-white">
                    <div class="container header-center">
                        <div class="wt-header-left">
                            <div class="logo-header">
                                <div class="logo-header-inner logo-header-one">
                                    <a href="<?php echo $path; ?>index.php">
                                        <img src="<?php echo $path; ?>images/logo-dark.png" width="171" height="49" alt="" />
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
                                    	<a href="<?php echo $path; ?>index.php" >Home</a>
                                    </li>
                                    <li>
                                        <a href="<?php echo $path; ?>about/index.php">About</a>
                                        <ul class="sub-menu">
                                            <li><a href="<?php echo $path; ?>about/pak-gusu/index.php">About Pak Gusu</a></li>
                                            <li><a href="<?php echo $path; ?>about/gusu-china/index.php">About GUSU China</a></li>
                                            <li><a href="<?php echo $path; ?>about/cleanroom-standards/index.php">Cleanroom Standards</a></li>
                                        </ul>
                                    </li>
                                    <li>
                                        <a href="javascript:;">Products</a>
                                        <ul class="sub-menu">
                                            <li><a href="<?php echo $path; ?>products/clean-room-panels/index.php">Clean Room Panels</a></li>
                                            <li><a href="<?php echo $path; ?>products/windows/index.php">Windows</a></li>
                                            <li><a href="<?php echo $path; ?>products/doors/index.php">Doors</a></li>
                                            <li><a href="<?php echo $path; ?>products/transfer-window/index.php">Transfer Window</a></li>
                                            <li><a href="<?php echo $path; ?>products/aluminum-profile/index.php">Aluminum Profile</a></li>
                                            <li><a href="<?php echo $path; ?>products/clean-led-lights/index.php">Clean LED Lights</a></li>
                                        </ul>
                                    </li>
                                    <li>
                                        <a href="javascript:;">Services</a>
                                        <ul class="sub-menu">
                                            <li><a href="<?php echo $path; ?>services/planning-design/index.php">Planning & Design</a></li>
                                            <li><a href="<?php echo $path; ?>services/clean-room-construction/index.php">Clean Room Construction</a></li>
                                            <li><a href="<?php echo $path; ?>services/installation/index.php">Installation</a></li>
                                            <li><a href="<?php echo $path; ?>services/after-sale-services/index.php">After Sale Services</a></li>
                                        </ul>
                                    </li>
                                    <li>
                                        <a href="javascript:;">Sectors</a>
                                        <ul class="sub-menu">
                                            <li><a href="<?php echo $path; ?>sectors/pharmaceutical/index.php">Pharmaceutical</a></li>
                                            <li><a href="<?php echo $path; ?>sectors/hospital/index.php">Hospital</a></li>
                                            <li><a href="<?php echo $path; ?>sectors/food-industry/index.php">Food Industry</a></li>
                                            <li><a href="<?php echo $path; ?>sectors/electronics/index.php">Electronics</a></li>
                                            <li><a href="<?php echo $path; ?>sectors/laboratories/index.php">Laboratories</a></li>
                                            <li><a href="<?php echo $path; ?>sectors/medical-devices/index.php">Medical Devices</a></li>
                                        </ul>
                                    </li>
                                    <li>
                                        <a href="<?php echo $path; ?>blog/index.php">Blog</a>
                                    </li>
                                    <li>
                                        <a href="<?php echo $path; ?>portfolio/index.php">Portfolio</a>
                                    </li>
                                    <li>
                                        <a href="<?php echo $path; ?>contact/index.php">Contact</a>
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
