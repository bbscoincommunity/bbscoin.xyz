<?php define('IN_HOME', true); require('core.inc.php'); $subtitle = $lang['subtitle_ecosystem'];require('head.php'); ?>

  <body id="page-top">

<?php require('navi.php'); ?>

    <section class="bg-primary" id="ecosystem">
      <div class="container">
        <div class="row">
          <div class="col-lg-8 mx-auto text-center">
            <h2 class="section-heading text-white"><?php echo $lang['navi_ecosystem'];?></h2>
            <hr class="light my-4">
            <h3><p class="text-faded mb-4"><a href="/ecosystem/#mining"><span class="text-faded mb-4"><?php echo $lang['mining'];?></span></a> | <a href="/ecosystem/#exchanges"><span class="text-faded mb-4"><?php echo $lang['exchanges'];?></span></a> | <a href="/ecosystem/#webwallet"><span class="text-faded mb-4"><?php echo $lang['webwallet'];?></span></a> | <a href="/ecosystem/#API"><span class="text-faded mb-4"><?php echo $lang['api'];?></span></a></p></h3>
          </div>
        </div>
      </div>
    </section>

    <section id="mining">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <h2 class="section-heading"><?php echo $lang['mining'];?></h2>
            <hr class="my-4">
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fas fa-wrench"></i></div>
              <h3 class="mb-3"><?php echo $lang['pools'];?></h3>
              <p class="text-muted mb-0"><a href="http://pool.bbscoin.xyz/#network" target="_blank"><?php echo $lang['pools_list'];?></a></p>
              <p class="text-muted mb-0"><a href="http://pool.bbscoin.xyz/" target="_blank"><?php echo $lang['official_pool'];?></a></p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fas fa-binoculars"></i></div>
              <h3 class="mb-3"><?php echo $lang['block_explorer'];?></h3>
              <p class="text-muted mb-0"><a href="http://bbs.gonspool.com/#blockchain_blocks" target="_blank">bbs.gonspool.com</a></p>
              <p class="text-muted mb-0"><a href="https://explorer.bbscoin.xyz/" target="_blank">explorer.bbscoin.xyz</a></p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fab fa-chrome"></i></div>
              <h3 class="mb-3"><?php echo $lang['web_miner_title'];?></h3>
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
            <h2 class="section-heading"><?php echo $lang['exchanges'];?></h2>
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
              <h3 class="mb-3"><?php echo $lang['crex24'];?></h3>
              <p class="text-muted mb-0"><a href="https://crex24.com/exchange/BBS-BTC" target="_blank">crex24.com</a></p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <img src="img/exchange/tradeogre.png" style="max-height: 150px;" />
              <br />
              <br />
              <br />
              <h3 class="mb-3"><?php echo $lang['tradeogre'];?></h3>
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
            <h2 class="section-heading"><?php echo $lang['webwallet'];?></h2>
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
              <h3 class="mb-3"><?php echo $lang['bbs.money'];?></h3>
              <p class="text-muted mb-0"><a href="https://bbs.money" target="_blank">BBS.money</a></p>
            </div>
          </div>
      </div>
    </section>


    <section id="API">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <h2 class="section-heading"><?php echo $lang['api'];?></h2>
            <hr class="my-4">
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fas fa-plug"></i></div>
              <h3 class="mb-3"><?php echo $lang['bbs.money_api'];?></h3>
              <p class="text-muted mb-0"><a href="https://developers.bbs.money/" target="_blank">developers.bbs.money</a></p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fas fa-database"></i></div>
              <h3 class="mb-3"><?php echo $lang['remote_node_title'];?></h3>
              <p class="text-muted mb-0">remotenode.bbscoin.xyz:21204</p>
            </div>
          </div>
      </div>
    </section>

<?php require('foot.php'); ?>
