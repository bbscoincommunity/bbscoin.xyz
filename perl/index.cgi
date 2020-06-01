#!/usr/bin/perl

# Errors to browser
use CGI::Carp qw(fatalsToBrowser);

sub str_replace {

	$_[2]=~s/$_[0]/$_[1]/gi;

	return $_[2];

}


  require './cookie.lib';

  $IN_HOME = 1;
  require('./core.inc.cgi'); 
  $subtitle = $lang->{'subtitle_home'};

  print "Content-Type: text/html\n\n";

  require('./head.cgi');
  require('./navi.cgi');

print <<"HTML";


    <header class="masthead text-center text-white d-flex">
      <div class="container my-auto">
        <div class="row">
          <div class="col-lg-10 mx-auto">
            <h1 class="text-uppercase">
              $lang->{'home_desc'}
            </h1>
            <hr>
          </div>
          <div class="col-lg-8 mx-auto">
            <p class="text-faded mb-5">$lang->{'home_desc_below'}</p>
            <a class="btn btn-primary btn-xl js-scroll-trigger" href="#about">$lang->{'home_more_btn'}</a>
          </div>
        </div>
      </div>
    </header>

    <section class="bg-primary" id="about">
      <div class="container">
        <div class="row">
          <div class="col-lg-8 mx-auto text-center">
            <h2 class="section-heading text-white">$lang->{'home_about_title'}</h2>
            <hr class="light my-4">
            <p class="text-faded mb-4">$lang->{'home_about_desc'}</p>
          </div>
        </div>
      </div>
    </section>

    <section id="technology">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <h2 class="section-heading">$lang->{'navi_technology'}</h2>
            <hr class="my-4">
          </div>
        </div>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fas fa-lock"></i></div>
              <h3 class="mb-3">$lang->{'ring_signatures'}</h3>
              <p class="text-muted mb-0">$lang->{'ring_signatures_desc'}</p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fas fa-server"></i></div>
              <h3 class="mb-3">$lang->{'platform'}</h3>
              <p class="text-muted mb-0">$lang->{'platform_desc'}</p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fas fa-desktop"></i></div>
              <h3 class="mb-3">$lang->{'algo'}</h3>
              <p class="text-muted mb-0">$lang->{'algo_desc'}</p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fas fa-dollar-sign"></i></div>
              <h3 class="mb-3">$lang->{'184billion'}</h3>
              <p class="text-muted mb-0">$lang->{'184billion_desc'}</p>
            </div>
          </div>
        </div>
      </div>
    </section>


    <section class="bg-dark text-white">
      <div class="container text-center">
        <h2 class="mb-4">$lang->{'get_bbscoin'}</h2>
        <a class="btn btn-light btn-xl sr-button" href="/ecosystem/#ecosystem" target="_blank">$lang->{'navi_ecosystem'}</a>
      </div>
    </section>

    <section id="roadmap">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <h2 class="section-heading">$lang->{'navi_roadmap'}</h2>
            <hr class="my-4">
          </div>
        </div>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-lg-4 ml-auto text-center">
			<div style="color:#f05f40;font-size:90px;"><i class="fas fa-road"></i></div>
            <p><strong>$lang->{'first_half_2018'}</strong></p>
$lang->{'desktop_wallet'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'official_pool'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'pool_upgrade'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'discuz_integration'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'phpwind_integration'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'mybb_integration'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'smf_integration'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'first_exchange_listing'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'difficulty_algorithm_update'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'cnv7_update'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'webwallet'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'web_wallet_api'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'web_wallet_api_doc'} <strong style="color:red;">$lang->{'done'}</strong><br />
          </div>
          <div class="col-lg-4 mr-auto text-center">
			<div style="color:#f05f40;font-size:90px;"><i class="fas fa-fighter-jet"></i></div>
            <p>
              <strong>$lang->{'second_half_2018'}</strong>
            </p>
$lang->{'internationalization_websites'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'web_miner'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'update_all_plugins'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'increase_adoption'} <strong style="color:red;">$lang->{'done'}</strong><br />
$lang->{'more_exchanges'} <strong style="color:red;">$lang->{'done'}</strong><br />
          </div>
          <div class="col-lg-4 mr-auto text-center">
			<div style="color:#f05f40;font-size:90px;"><i class="fab fa-skyatlas"></i></div>
            <p>
              <strong>$lang->{'long_term'}</strong>
            </p>
$lang->{'bounty_program'}<br />
$lang->{'new_air_drop'}<br />
$lang->{'web_hook_for_api'}<br />
$lang->{'continuous_improving_api'}<br />
$lang->{'continuous_improving_web_wallet'}<br />
$lang->{'increase_adoption'}<br />
$lang->{'rewrite_desktop_wallet'}<br />
$lang->{'more_exchanges'}<br />
$lang->{'android_app'}<br />
$lang->{'iphone_app'}<br />
$lang->{'enhanced_integrations'}<br />
$lang->{'site_admin_service_platform'}<br />
          </div>
        </div>
      </div>
    </section>

    <section class="bg-dark text-white">
      <div class="container text-center">
        <h2 class="mb-4">$lang->{'learn_more_btn'}</h2>
      </div>
    </section>


    <section id="followus">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <h2 class="section-heading">$lang->{'follow_us_title'}</h2>
            <hr class="my-4">
          </div>
        </div>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-lg-2 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fab fa-twitter"></i></div>
              <h3 class="mb-3">$lang->{'twitter'}</h3>
              <p class="text-muted mb-0">$lang->{'bbscoin_twitter'}</p>
              <p class="text-muted mb-0"><a href="https://twitter.com/bbscoin_xyz" target="_blank">\@bbscoin_xyz</a></p>
            </div>
          </div>
          <div class="col-lg-2 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fab fa-discord"></i></div>
              <h3 class="mb-3">$lang->{'discord'}</h3>
              <p class="text-muted mb-0">$lang->{'bbscoin_discord'}</p>
              <p class="text-muted mb-0">English 日本語 中文 한국어 Русская</p>
              <p class="text-muted mb-0"><a href="https://discord.gg/e4QnNYa" target="_blank">discord.gg/e4QnNYa</a></p>
             </div>
          </div>
          <div class="col-lg-2 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fab fa-telegram"></i></div>
              <h3 class="mb-3">$lang->{'telegram'}</h3>
              <p class="text-muted mb-0">$lang->{'bbscoin_telegram'}</p>
              <p class="text-muted mb-0"><a href="https://t.me/bbscoin" target="_blank">English</a>
              <a href="https://t.me/bbscoin_ru" target="_blank">Русская</a></p>
              <p class="text-muted mb-0"><a href="https://t.me/bbscoin_korea" target="_blank">한국어</a>
              <a href="https://t.me/bbscoinid" target="_blank">Indonesia</a></p>
              <p class="text-muted mb-0"><a href="https://t.me/bbscoin_cn" target="_blank">中文</a>
              <a href="https://t.me/bbscoin_japan" target="_blank">日本語</a> <a href="https://t.me/joinchat/Ix6CZEpUT8ZXHxn1QCdjKQ" target="_blank">Türkçe</a>
              </p>
              <p class="text-muted mb-0"><a href="https://t.me/bbscoinptbr" target="_blank">Português Brasileiro</a>
              </p>
              <p class="text-muted mb-0"><a href="https://t.me/bbscoin_spain" target="_blank">español</a> <a href="https://t.me/bbscoin_arabic" target="_blank">Arabic</a>
              </p>
         </div>
          </div>
          <div class="col-lg-2 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fab fa-medium"></i></div>
              <h3 class="mb-3">$lang->{'medium'}</h3>
              <p class="text-muted mb-0">$lang->{'bbscoin_medium'}</p>
              <p class="text-muted mb-0"><a href="https://medium.com/bbscoin" target="_blank">\@bbscoin</a></p>
            </div>
          </div>
          <div class="col-lg-2 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fab fa-github"></i></div>
              <h3 class="mb-3">$lang->{'github'}</h3>
              <p class="text-muted mb-0">$lang->{'bbscoin_github'}</p>
              <p class="text-muted mb-0"><a href="https://github.com/bbscoin" target="_blank">github.com/bbscoin</a></p>
            </div>
          </div>
          <div class="col-lg-2 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fab fa-discourse"></i></div>
              <h3 class="mb-3">$lang->{'community'}</h3>
              <p class="text-muted mb-0"><a href="https://forum.bbscoin.xyz/" target="_blank">$lang->{'official_forum'}</a></p>
              <p class="text-muted mb-0"><a href="http://Bbscoin.kr/" target="_blank">$lang->{'korea_community'}</a></p>
              <p class="text-muted mb-0"><a href="https://coinbbs.co/" target="_blank">COINBBS.co</a></p>
              <p class="text-muted mb-0"><a href="http://www.blocktoken.tech/" target="_blank">blocktoken.tech</a></p>
            </div>
          </div>
        </div>
      </div>
    </section>

HTML

  require('./foot.cgi');


exit();