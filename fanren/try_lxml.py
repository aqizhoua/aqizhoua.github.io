import requests
from lxml import etree

url = "https://www.51shucheng.net/wangluo/fanrenxiuxianzhuan"
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

response_sina = requests.get(url,headers=headers)
response_sina.encoding = 'utf-8'


html = etree.HTML(response_sina.text)
print(html)

ret1 = html.xpath("//li/a/@title")

with open("index.html", "w",encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>�������ɴ�-�������ɴ�С˵ȫ�������Ķ�</title>
<meta name="keywords" content="�������ɴ�,�������ɴ�ȫ��">
<meta name="description" content="�������ɴ���������׫��һ������С˵�������������������С˵������һ����ͨ��ɽ����С�ӣ�żȻ֮�£����뵽һ������С���ɣ�����һ���������ӡ���Ȼ����ƽӹ������������Ŭ���ͺ�������������ɡ�">
<link rel="stylesheet" type="text/css" media="screen" href="www.css">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Cache-Control" content="no-siteapp">
</head>
<body>
	<div class="content">
		<div class="catalog">
			<h1>�������ɴ�</h1>
			<div class="summary">
				<b>���ݼ�飺</b>
				<div class="intro"><p>�������ɴ���������׫��һ������С˵�������������������С˵������һ����ͨ��ɽ����С�ӣ�żȻ֮�£����뵽һ������С���ɣ�����һ���������ӡ���Ȼ����ƽӹ������������Ŭ���ͺ�������������ɡ�</p>
</div>
			</div>

						<div class="ad">
				<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
				<!-- bookindex-top -->
				<ins class="adsbygoogle bookindex-top"
					style="display:block"
					data-ad-client="ca-pub-9405492286923119"
					data-ad-slot="1342023172"
					data-full-width-responsive="true"></ins>
				<script>
					(adsbygoogle = window.adsbygoogle || []).push({});
				</script>
			</div>
		<div class="mulu-title"><h2>�������ɴ�ȫ�������Ķ�</h2></div>
			<div class="mulu-list-2">
			<ul>""")
    for ret in ret1:
        f.write('<li><a href="{}" title="{}">{}</a></li>\n'.format(ret,ret,ret))
    f.write("""
    </ul>
		</div>
		<div class="ad-bottom">
			<div class="fr mfn">
				<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
				<!-- bookindex-bottom-right -->
				<ins class="adsbygoogle bookindex-bottom-right"
					style="display:inline-block"
					data-ad-client="ca-pub-9405492286923119"
					data-ad-slot="1449834380"
					data-full-width-responsive="true"></ins>
				<script>
					(adsbygoogle = window.adsbygoogle || []).push({});
				</script>
			</div>
			<div class="fl mhidden">
				<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
				<!-- bookindex-bottom-left -->
				<ins class="adsbygoogle bookindex-bottom-left"
					style="display:inline-block"
					data-ad-client="ca-pub-9405492286923119"
					data-ad-slot="6893732753"></ins>
				<script>
					(adsbygoogle = window.adsbygoogle || []).push({});
				</script>
			</div>
		</div>
		<div class="mulu-title">

</div>

	</div>
	</div>



</div>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-36301681-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-36301681-1');
</script>
</body>
</html>""")