#!/usr/bin/perl

if ($IN_HOME) {

%avail_langs = (
    'ja' => 'ja',
    'zh' => 'zh',
    'zh-cn' => 'zh',
    'zh-tw' => 'zh',
    'zh-sg' => 'zh',
    'zh-hk' => 'zh',
    'ko' => 'ko',
    'ko-kp' => 'ko',
    'ko-kr' => 'ko',
    'pt' => 'pt-br',
    'pt-br' => 'pt-br',
    'ar' => 'ar',
    'id' => 'id',
    'es' => 'es',
    'es-ar' => 'es',
    'es-bo' => 'es',
    'es-cl' => 'es',
    'es-co' => 'es',
    'es-cr' => 'es',
    'es-do' => 'es',
    'es-ec' => 'es',
    'es-sv' => 'es',
    'es-gt' => 'es',
    'es-hn' => 'es',
    'es-mx' => 'es',
    'es-ni' => 'es',
    'es-pa' => 'es',
    'es-py' => 'es',
    'es-pe' => 'es',
    'es-pr' => 'es',
    'es-es' => 'es',
    'es-uy' => 'es',
    'es-ve' => 'es',
    'ru' => 'ru',
    'ru-mo' => 'ru',
);

# Check for language designation on hostname.
@mylang = split(/\./, $ENV{'HTTP_HOST'});
#
local $/ = undef;
#
if (-e './language/'.$mylang[0].'.json') {
    open($language, "<:encoding(UTF-8)", "./language/".$mylang[0].".json");
}
else {
    open($language, "<:encoding(UTF-8)", "./language/en.json") || die("Default language file not found.");
}
#
$langdata = <$language>;
close $language;
#
use JSON::XS;
$lang=decode_json($langdata);

# This needs to be verified
#if ($ENV{'REQUEST_URI'} !=~m/ncr/) {
#    &SetCookies('ncr', '1', time() + 2592000, '/', 'bbscoin.xyz');
#    print "Location: https://bbscoin.xyz/\n\n";
#    exit;
#}

#if ($ENV{'HTTP_HOST'} eq 'bbscoin.xyz' || $ENV{'HTTP_HOST'} eq 'www.bbscoin.xyz') {
#    if (!$COOKIE{'ncr'}) { # need to check if cookie is up after DNS change.
#        @accept_languages = split(',', str_replace(';', ',', $ENV{'HTTP_ACCEPT_LANGUAGE'}));
#        foreach $item (@accept_languages) {
#            $item = lc($item);
#            if ($avail_langs{$item}) {
#                print "Location: https://".$avail_langs{$item}.".bbscoin.xyz".$ENV{'REQUEST_URI'}."\n\n";
#                exit;
#            }
#        }
#    }
#}

}
return 1;