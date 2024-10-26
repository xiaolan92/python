import aiohttp
import asyncio
from lxml import etree
import os

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'cookie': 'session_prefix=a8deca8a92186f471ac925712b91d135; Hm_lvt_2911e7fbbc2af45ce5bee6f3e22033c6=1726906172; yii_zhima_session=aop7bvpd1j2dp6249gejv6j6ak; Hm_lvt_e57b8b134e41424995fb7e19768f061e=1726906079,1729006468; HMACCOUNT=A830E05E69B01151; Hm_lvt_26b5094a3b36a601595d7a7521f2a840=1726906080,1729006501; Hm_lvt_a4964b2514693874bb3c7104e129d76e=1729330035; Hm_lpvt_e57b8b134e41424995fb7e19768f061e=1729330040; Hm_lpvt_26b5094a3b36a601595d7a7521f2a840=1729330040; Hm_lpvt_a4964b2514693874bb3c7104e129d76e=1729330953; SERVERID=21f68ac0dede9867d1fce83989ad9ba9|1729330951|1729330033; SERVERCORSID=21f68ac0dede9867d1fce83989ad9ba9|1729330951|1729330033'
}

dirName = 'images/'
async def getImg(url, Session):
    async with Session.get(url) as response:
        response.raise_for_status()
        html = await response.text()
        parse_html = etree.HTML(html)
        result_child = parse_html.xpath("//img[@class='syl-page-img aligncenter']")
        for k in result_child:
            href_child = k.get('src')
            result_content = await Session.get(href_child, headers=headers)
            img_name = href_child.split('/')[-1].split('?')[0] + '.png'
            if not os.path.exists(dirName):
                os.makedirs(dirName)
            with open(os.path.join(dirName, img_name), mode='wb') as f:
                content = await result_content.content.read()
                f.write(content)


async def getContent(url):
    async  with aiohttp.ClientSession() as Session:
        async with Session.get(url) as response:
            response.raise_for_status()
            html = await response.text()
            parse_html = etree.HTML(html)
            result = parse_html.xpath("//p[text()='行业案例']/following-sibling::ul/li/a/@href")
            for item in result:
                await getImg(item, Session)


async def main():
    url = 'https://xiaokefu.com.cn/'
    await getContent(url)


asyncio.run(main())
