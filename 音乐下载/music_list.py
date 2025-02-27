import requests
import urllib.parse
import os
import time

'''
整体思路是定义一个类，输入下载的个数和搜索内容
'''


class Music:
    def __init__(self, music_list, search_url, download_url, headers1, headers2, path):
        self.url = search_url
        self.download_url = download_url
        self.search_headers = headers1
        self.download_headers = headers2
        self.music_info = []
        self.music = {}
        self.path = path
        self.c = []
        self.music_list = music_list

    def parse_list(self, id):
        playlist_id = id
        addr = 'https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?type=1&json=1&utf8=1&onlysong=0&new_format=1&disstid=7766417428&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
        header = {
            'origin': 'https://y.qq.com',
            'referer': 'https://y.qq.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'

        }
        response = requests.get(url=addr, headers=header)
        info = eval(response.text)
        print(1)
        name = []
        singer = []
        for i in range(len(info['cdlist'][0]['songlist'])):
            name.append(info['cdlist'][0]['songlist'][i]['name'])
            singer.append((info['cdlist'][0]['songlist'][i]['singer'][0]['name']))

        self.c = list(zip(name, singer))
        # print(self.c)
        # print(len(self.c))

    def search(self, name):
        # print(name)
        # print(urllib.parse.quote(name))
        # 这里是字符串格式化的，第一次已经填充过了，所以第二次就不会填充了
        self.url[1] = [urllib.parse.quote(name)]
        # print(type(self.url[1]))
        s_url = self.url[0][0] + self.url[1][0] + self.url[2][0]
        # print(self.url)
        response = requests.get(url=s_url, headers=self.search_headers)
        rec = response.json()
        # print(rec)
        '''
        得到歌曲信息 name id
        '''
        self.music['name'] = rec['data']['list'][0]['name']
        self.music['id'] = rec['data']['list'][0]['rid']
        self.music['singer'] = rec['data']['list'][0]['artist']
        self.music_info.append(self.music)
        print(self.music)

    def download(self):
        self.parse_list(self.music_list)
        for i in range(len(self.c)):
            self.search(self.c[i][0] + ' ' + self.c[i][1])
            file_name = str(self.music_info[0]['singer']) + ' - ' + str(
                self.music_info[0]['name'])
            # download(music_info[int(index[i]) - 1]['id'], file_name)
            info_url = self.download_url.format(format(self.music_info[0]['id']))
            get_download_url = requests.get(url=info_url, headers=self.download_headers)

            download_url = get_download_url.json()['url']
            if download_url == '':
                print('没有资源')
            else:
                time.sleep(1)
                download_music = requests.get(url=download_url)
                self.mkdir()
                with open(r'D:\MUSIC\kuwo\{0}.mp3'.format(file_name), 'wb') as f:
                    f.write(download_music.content)
                print('{}   下载完成!'.format(file_name))

    def mkdir(self):
        folder = os.path.exists(self.path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(self.path)  # makedirs 创建文件时如果路径不存在会创建这个路径


if __name__ == '__main__':
    # search_name, number, search_url, download_url, headers1, headers2
    playlist_id = '7766417428'
    search_url = [['http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key='], [], ['&pn=1&rn=30&reqId=24b2acb0-e1f4-11e9-9c10-df22c38d9fb9']]
    download_url = 'http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=320kmp3&from=web&t=1569668134762&reqId=717bbfe5-a891-49c2-b549-c923ea781cec'
    headers1 = {
        'Cookie': 'Cookie: _ga=GA1.2.1209502700.1578305434; _gid=GA1.2.570101734.1578305434; _gat=1; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1578305434; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1578305434; kw_token=EQ4EIPN5TE7',
        'Host': 'www.kuwo.cn',
        'csrf': 'EQ4EIPN5TE7',
        'Referer': 'http://www.kuwo.cn/search/list?key=%E8%AE%B8%E5%B5%A9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    headers2 = {
        'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1569666496,1569668107; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1569677402',
        'Host': 'www.kuwo.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

    path = r'D:\MUSIC\kuwo'
    music = Music(playlist_id, search_url, download_url, headers1, headers2, path)
    music.download()



