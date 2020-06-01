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

    <section class="bg-primary" id="ecosystem">
      <div class="container">
        <div class="row">
          <div class="col-lg-8 mx-auto text-center">
            <h2 class="section-heading text-white">$lang->{'navi_ecosystem'}</h2>
            <hr class="light my-4">
            <h3><p class="text-faded mb-4"><a href="/ecosystem/#mining"><span class="text-faded mb-4">$lang->{'mining'}</span></a> | <a href="/ecosystem/#exchanges"><span class="text-faded mb-4">$lang->{'exchanges'}</span></a> | <a href="/ecosystem/#webwallet"><span class="text-faded mb-4">$lang->{'webwallet'}</span></a> | <a href="/ecosystem/#API"><span class="text-faded mb-4">$lang->{'api'}</span></a></p></h3>
          </div>
        </div>
      </div>
    </section>

    <section id="mining">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <h2 class="section-heading">$lang->{'mining'}</h2>
            <hr class="my-4">
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fas fa-wrench"></i></div>
              <h3 class="mb-3">$lang->{'pools'}</h3>
              <p class="text-muted mb-0"><a href="http://pool.bbscoin.xyz/#network" target="_blank">$lang->{'pools_list'}</a></p>
              <p class="text-muted mb-0"><a href="http://pool.bbscoin.xyz/" target="_blank">$lang->{'official_pool'}</a></p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fas fa-binoculars"></i></div>
              <h3 class="mb-3">$lang->{'block_explorer'}</h3>
              <p class="text-muted mb-0"><a href="http://bbs.gonspool.com/#blockchain_blocks" target="_blank">bbs.gonspool.com</a></p>
              <p class="text-muted mb-0"><a href="https://explorer.bbscoin.xyz/" target="_blank">explorer.bbscoin.xyz</a></p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fab fa-chrome"></i></div>
              <h3 class="mb-3">$lang->{'web_miner_title'}</h3>
              <p class="text-muted mb-0"><a href="https://www.jscoinminer.com/" target="_blank">jscoinminer.com</a></p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="exchanges">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <h2 class="section-heading">$lang->{'exchanges'}</h2>
            <hr class="my-4">
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <img src="img/exchange/crex24.png" style="max-height: 150px;" />
              <br />
              <br />
              <br />
              <h3 class="mb-3">$lang->{'crex24'}</h3>
              <p class="text-muted mb-0"><a href="https://crex24.com/exchange/BBS-BTC" target="_blank">crex24.com</a></p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <img src="img/exchange/tradeogre.png" style="max-height: 150px;" />
              <br />
              <br />
              <br />
              <h3 class="mb-3">$lang->{'tradeogre'}</h3>
              <p class="text-muted mb-0"><a href="https://tradeogre.com/exchange/LTC-BBS" target="_blank">tradeogre.com</a></p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="webwallet">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <h2 class="section-heading">$lang->{'webwallet'}</h2>
            <hr class="my-4">
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <img src="img/exchange/bbsmoney.png" style="max-height: 150px;" />
              <br />
              <br />
              <br />
              <h3 class="mb-3">$lang->{'bbs.money'}</h3>
              <p class="text-muted mb-0"><a href="https://bbs.money" target="_blank">BBS.money</a></p>
            </div>
          </div>
      </div>
    </section>


    <section id="API">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <h2 class="section-heading">$lang->{'api'}</h2>
            <hr class="my-4">
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fas fa-plug"></i></div>
              <h3 class="mb-3">$lang->{'bbs.money_api'}</h3>
              <p class="text-muted mb-0"><a href="https://developers.bbs.money/" target="_blank">developers.bbs.money</a></p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fas fa-database"></i></div>
              <h3 class="mb-3">$lang->{'remote_node_title'}</h3>
              <p class="text-muted mb-0">remotenode.bbscoin.xyz:21204</p>
            </div>
          </div>
      </div>
    </section>
   
HTML

  require('./foot.cgi');


exit();