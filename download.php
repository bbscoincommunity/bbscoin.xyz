<?php define('IN_HOME', true); require('core.inc.php'); $subtitle = $lang['subtitle_download'];require('head.php'); ?>

  <body id="page-top">

<?php require('navi.php'); ?>

    <section class="bg-primary" id="downloads">
      <div class="container">
        <div class="row">
          <div class="col-lg-8 mx-auto text-center">
            <h2 class="section-heading text-white"><?php echo $lang['navi_download'];?></h2>
          </div>
        </div>
      </div>
    </section>

    <section id="downloads-list">
      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fab fa-windows"></i></div>
              <h3 class="mb-3"><?php echo $lang['windows'];?></h3>
              <p class="text-muted mb-0"><a href="https://raw.githubusercontent.com/bbscoin/bbscoin-releases/master/6.0.0/bbscoinwallet_win_x64_v6.0.0.zip" target="_blank"><?php echo $lang['desktop_wallet_x64'];?> 6.0.0</a></p>
              <p class="text-muted mb-0"><a href="https://raw.githubusercontent.com/bbscoin/bbscoin-releases/master/6.0.0/bbscoin_bins_win_x64_v6.0.0.zip" target="_blank"><?php echo $lang['command_line_x64'];?> 6.0.0</a></p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fab fa-linux"></i></div>
              <h3 class="mb-3"><?php echo $lang['linux'];?></h3>
              <p class="text-muted mb-0"><?php echo $lang['wallet_for_ubuntu'];?> 6.0.0</p>
              <p class="text-muted mb-0"><a href="https://raw.githubusercontent.com/bbscoin/bbscoin-releases/master/6.0.0/bbscoinwallet_ubuntu_18_04_x64_v6.0.0.deb" target="_blank">Ubuntu 18.04</a> | <a href="https://raw.githubusercontent.com/bbscoin/bbscoin-releases/master/6.0.0/bbscoinwallet_ubuntu_16_04_x64_v6.0.0.deb" target="_blank">Ubuntu 16.04</a></p>
              <p class="text-muted mb-0"><?php echo $lang['cli_for_ubuntu'];?> 6.0.0</p>
              <p class="text-muted mb-0"><a href="https://raw.githubusercontent.com/bbscoin/bbscoin-releases/master/6.0.0/bbscoin_bins_ubuntu_18_04_v6.0.0.tar.xz" target="_blank">Ubuntu 18.04</a> | <a href="https://raw.githubusercontent.com/bbscoin/bbscoin-releases/master/6.0.0/bbscoin_bins_ubuntu_16.04_v6.0.0.tar.gz" target="_blank">Ubuntu 16.04</a></p>
              <p class="text-muted mb-0"><?php echo $lang['cli_for_centos'];?> 6.0.0</p>
              <p class="text-muted mb-0"><a href="https://raw.githubusercontent.com/bbscoin/bbscoin-releases/master/6.0.0/bbscoin_bins_centos_7_v6.0.0.tar.gz" target="_blank">CentOS 7.0</a></p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fab fa-apple"></i></div>
              <h3 class="mb-3"><?php echo $lang['macosx'];?></h3>
              <p class="text-muted mb-0"><?php echo $lang['wallet_for_macos'];?> 6.0.0</p>
              <p class="text-muted mb-0"><a href="https://raw.githubusercontent.com/bbscoin/bbscoin-releases/master/6.0.0/bbscoinwallet_macOS_10.14_v6.0.0.dmg" target="_blank">macOS 10.14</a></p>
              <p class="text-muted mb-0"><?php echo $lang['cli_for_macos'];?> 6.0.0</p>
              <p class="text-muted mb-0"><a href="https://raw.githubusercontent.com/bbscoin/bbscoin-releases/master/6.0.0/bbscoin_bins_macOS_10.14_v6.0.0.zip" target="_blank">macOS 10.14</a></p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fas fa-plug"></i></div>
              <h3 class="mb-3"><?php echo $lang['plugins'];?></h3>
              <p class="text-muted mb-0"><a href="https://raw.githubusercontent.com/bbscoin/bbscoin-releases/master/plugins/bbscoin_mybb_v1_0_3.zip" target="_blank"><?php echo $lang['for_mybb'];?> v1.0.3</a> / <a href="https://github.com/bbscoin/mybb-plugin/archive/master.zip" target="_blank">v2.0</a></p>
              <p class="text-muted mb-0"><a href="https://raw.githubusercontent.com/bbscoin/bbscoin-releases/master/plugins/bbscoin_smf_v1_0_1.zip" target="_blank"><?php echo $lang['for_smf'];?> v1.0.1</a> / <a href="https://github.com/bbscoin/smf-plugin/archive/master.zip" target="_blank">v2.0</a></p>
              <p class="text-muted mb-0"><a href="https://raw.githubusercontent.com/bbscoin/bbscoin-releases/master/plugins/bbscoin_discuz_v1_1_2.zip" target="_blank"><?php echo $lang['for_discuz'];?> v1.1.2</a> / <a href="https://github.com/bbscoin/discuz-plugin/archive/master.zip" target="_blank">v2.0.1</a></p>
              <p class="text-muted mb-0"><a href="https://raw.githubusercontent.com/bbscoin/bbscoin-releases/master/plugins/bbscoin_phpwind_v1_1_2.zip" target="_blank"><?php echo $lang['for_phpwind'];?> v1.1.2</a> / <a href="https://github.com/bbscoin/phpwind-plugin/archive/master.zip" target="_blank">v2.0</a></p>
              <p class="text-muted mb-0"><a href="https://github.com/idsu/bbscoing5" target="_blank"><?php echo $lang['for_gnubb'];?></a></p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box mt-5 mx-auto">
              <div style="color:#f05f40;font-size:90px;"><i class="fas fa-link"></i></div>
              <h3 class="mb-3"><?php echo $lang['blockchain'];?></h3>
              <p class="text-muted mb-0"><a href="https://www.dropbox.com/s/6juxbm3h1mr4lwo/206303.zip?dl=0" target="_blank"><?php echo $lang['height'];?> 206303</a></p>
            </div>
          </div>
        </div>
      </div>
    </section>

<?php require('foot.php'); ?>
