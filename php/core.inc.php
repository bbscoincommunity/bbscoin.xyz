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

// New language file format and detection by hostname
$host = explode('.', $_SERVER['HTTP_HOST']);

if (file_exists('./language/'.$host[0].'.json')) {
    $language = file_get_contents('./language/'.$host[0].'.json');
} else {
    $language = file_get_contents('./language/en.json');
}
// language in json now
$lang=json_decode($language, true);


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

