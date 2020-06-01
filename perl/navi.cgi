#!/usr/bin/perl

if ($IN_HOME) {

print <<"HTML";
<!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
      <div class="container">
        <a class="navbar-brand js-scroll-trigger" href="/#page-top">BBSCoin</a>
        <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="/#page-top">$lang->{'navi_home'}</a>
            </li>
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="/#technology">$lang->{'navi_technology'}</a>
            </li>
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="/#roadmap">$lang->{'navi_roadmap'}</a>
            </li>
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="/download/#downloads">$lang->{'navi_download'}</a>
            </li>
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="/ecosystem/#ecosystem">$lang->{'navi_ecosystem'}</a>
            </li>
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="https://bbs.money" target="_blank">$lang->{'webwallet'}</a>
            </li>
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="/#followus">$lang->{'navi_followus'}</a>
            </li>
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="https://forum.bbscoin.xyz" target="_blank">$lang->{'navi_forums'}</a>
            </li>
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="#globeselect"><i title="Languages" class="fas fa-globe"></i></a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

HTML

}
