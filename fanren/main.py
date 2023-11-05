# coding=utf-8
import requests
from lxml import etree
import json
import re


class FanrenSpider:
    def __init__(self):
        self.start_url = "https://www.51shucheng.net/wangluo/fanrenxiuxianzhuan/14002.html "
        self.part_url = "https://www.51shucheng.net/wangluo/fanrenxiuxianzhuan/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}

    def parse_url(self, url):  # 发送请求，获取响应
        print(url)
        response = requests.get(url, headers=self.headers)
        #response.encoding = 'iso-8859-1'
        try:
            return response.text.encode("iso-8859-1")
        except:
            return response.text.encode("utf-8")

    def get_content_list(self, html_str):  # 提取数据
        html = etree.HTML(html_str)
        print(html_str)
        # print("*"*100)
        content = \
        re.findall(r'<div class="neirong" id="neirong">(.*?)<div class="ad-bottom">', html_str.decode(), re.S)[0]
        # print(content)
        this_title = html.xpath("//h1/text()")[0] if len(html.xpath("//h1/text()")) > 0 else None
        last_title = html.xpath('//a[@id="BookPrev"]/@title')[0] if len(
            html.xpath('//a[@id="BookPrev"]/@title')) > 0 else None

        next_title = html.xpath('//a[@id="BookNext"]/@title')[0] if len(
            html.xpath('//a[@id="BookNext"]/@title')) > 0 else None
        next_url = html.xpath("//a[@id='BookNext']/@href")[0] if len(
            html.xpath("//a[@id='BookNext']/@href")) > 0 else None
        return content, last_title, this_title, next_title, next_url

    def save_content(self, content, last_title, this_title, next_title):  # 保存数据
        file_path = "凡人修仙传 "+this_title + ".html" if this_title != None else "error.html"
        with open(file_path, "w",encoding="utf-8") as f:  # "李毅—第4页.html"
            f.write("""<html lang="zh-CN">
            <meta charset="UTF-8">
            <link rel="stylesheet" type="text/css" media="screen" href="www.css">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <div class="content book-content">
            <div class="neirong" id="neirong">""")
            f.write("<h1 align='center'>{}</h1>".format(this_title))
            f.write(content)
            f.write(f"""	<div class="book-nav">
        <div class="prev" align="center" >
        <a id="BookPrev" title="凡人修仙传 第一卷 七玄门风云 第三章 七玄门" href="{last_title}.html">上一章</a>		</div>

        <div class="next" align="center" >
        <a id="BookNext" title="凡人修仙传 第一卷 七玄门风云 第三章 七玄门" href="{next_title}.html">下一章</a>		</div>
            <div class="home" align="center" >
            回目录：<a id="BookHome" title="《凡人修仙传》全集在线阅读" href=index.html>《凡人修仙传》</a></div>
    </div>""")

        print("next_url:", next_title)
        print("this_url:", this_title)
        print("保存成功")



    def run(self):  # 实现主要逻辑
        next_url = self.start_url  # 下一个
        while next_url is not None:
            # 1.start_url
            # 2.发送请求，获取响应
            html_str = self.parse_url(next_url)
            # 3.提取数据，提取下一页的url地址
            # 3.1提取列表页的url地址和标题
            # 3.2请求列表页的url地址，获取详情页的第一页
            # 3.3提取详情页第一页的图片，提取下一页的地址
            # 3.4请求详情页下一页的地址，进入循环3.2-3.4

            content, last_title, this_title, next_title, next_url = self.get_content_list(html_str)
            title_list = [last_title, this_title, next_title]
            title_new = []
            for title in title_list:
                if title.find('?') != -1:
                    title = title.split("?")[0]
                title_new.append(title)


            last_title, this_title, next_title = title_new
                # 4.保存数据
            self.save_content(content, last_title, this_title, next_title)
            # 5.请求下一页的url地址，进入循环2-5不


if __name__ == '__main__':
    spider = FanrenSpider()
    spider.run()
