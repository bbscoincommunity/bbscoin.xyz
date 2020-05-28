<?php if(!defined('IN_HOME')) exit;

$avail_langs = [
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
];

$lang = [];

require('lang/en.php');
if ($_SERVER['HTTP_HOST'] == 'zh.bbscoin.xyz') {
    require('lang/zh.php');
} elseif ($_SERVER['HTTP_HOST'] == 'ja.bbscoin.xyz') {
    require('lang/ja.php');
} elseif ($_SERVER['HTTP_HOST'] == 'ko.bbscoin.xyz') {
    require('lang/ko.php');
} elseif ($_SERVER['HTTP_HOST'] == 'pt-br.bbscoin.xyz') {
    require('lang/pt-br.php');
} elseif ($_SERVER['HTTP_HOST'] == 'es.bbscoin.xyz') {
    require('lang/es.php');
} elseif ($_SERVER['HTTP_HOST'] == 'ar.bbscoin.xyz') {
    require('lang/ar.php');
} elseif ($_SERVER['HTTP_HOST'] == 'id.bbscoin.xyz') {
    require('lang/id.php');
} elseif ($_SERVER['HTTP_HOST'] == 'ru.bbscoin.xyz') {
    require('lang/ru.php');
}

if (stripos($_SERVER['REQUEST_URI'], 'ncr') !== false) {
    setcookie('ncr', '1', time() + 2592000, '/', 'bbscoin.xyz');
    header('Location: https://bbscoin.xyz/');
    exit;
}

if ($_SERVER['HTTP_HOST'] == 'bbscoin.xyz' || $_SERVER['HTTP_HOST'] == 'www.bbscoin.xyz') {
    if (!$_COOKIE['ncr']) {
        $accept_languages = explode(',', str_replace(';', ',', $_SERVER['HTTP_ACCEPT_LANGUAGE']));
        foreach ($accept_languages as $item) {
            $item = strtolower($item);
            if ($avail_langs[$item]) {
                header('Location: https://'.$avail_langs[$item].'.bbscoin.xyz'.$_SERVER['REQUEST_URI']);
                exit;
            }
        }
    }
}

