#!/usr/bin/perl

if ($IN_HOME) {
print <<"HTML";

    <section class="bg-dark text-white">

      <div class="container">
        <div class="row">
          <div class="col-lg-4 ml-auto text-left">
          	<p class="text-muted mb-0"><a href="https://explorer.bbscoin.xyz/" target="_blank">$lang->{'block_explorer'}</a></p>
          	<p class="text-muted mb-0"><a href="http://pool.bbscoin.xyz/" target="_blank">$lang->{'pool'}</a></p>
          	<p class="text-muted mb-0"><a href="https://bbs.money/" target="_blank">$lang->{'webwallet'}</a></p>
          </div>
          <div class="col-lg-4 ml-auto text-left">
          	<p class="text-muted mb-0"><a href="$lang->{'whitepaper_url'}" target="_blank">$lang->{'whitepaper'}</a></p>
          	<p class="text-muted mb-0"><a href="https://forum.bbscoin.xyz/" target="_blank">$lang->{'navi_forums'}</a></p>
          	<p class="text-muted mb-0"><a href="https://github.com/bbscoin/" target="_blank">$lang->{'github'}</a></p>
          </div>
          <div class="col-lg-4 ml-auto text-left">
          	<p class="text-muted mb-0"><a href="https://twitter.com/bbscoin_xyz" target="_blank">$lang->{'twitter'}</a></p>
          </div>
        </div>
        <br />
        <div class="row" id="globeselect">
          <div class="col-lg-12 ml-auto text-left">Global Sites: <a href="https://bbscoin.xyz/ncr">English</a>, <a href="https://ar.bbscoin.xyz/">Arabic</a>, <a href="https://zh.bbscoin.xyz/">中文(简体)</a>, <a href="https://es.bbscoin.xyz/">español</a>, <a href="https://id.bbscoin.xyz/">Indonesia</a>, <a href="https://ja.bbscoin.xyz/">日本語</a>, <a href="https://ko.bbscoin.xyz/">한국어</a>, <a href="https://pt-br.bbscoin.xyz/">Português Brasileiro</a>, <a href="https://ru.bbscoin.xyz/">русский</a>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-12 ml-auto text-left"><br /><br /><br />BBSCoin&copy;date('Y') BBSCoin Foundation, page designed by Blackrock Digital LLC.
          </div>
        </div>
      </div>



    </section>

    <!-- Bootstrap core JavaScript -->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="vendor/jquery-easing/jquery.easing.min.js"></script>
    <script src="vendor/scrollreveal/scrollreveal.min.js"></script>
    <script src="vendor/magnific-popup/jquery.magnific-popup.min.js"></script>

    <!-- Custom scripts for this template -->
    <script src="js/creative.min.js"></script>
    <script src="js/fontawesome.min.js"></script>

    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-119908894-1"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'UA-119908894-1');
    </script>


  </body>

</html>

HTML
}