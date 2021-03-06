#!/usr/bin/env python
# -*- coding: utf-8 -*-

# COPYRIGHT (C) 2014-2020 Mitsuo KONDOU.
# This software is released under the MIT License.
# https://github.com/konsan1101
# Thank you for keeping the rules.



import sys
import os
import time
import datetime
import codecs
import glob

import queue
import threading
import subprocess

from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

#print(os.path.dirname(__file__))
#print(os.path.basename(__file__))
#print(sys.version_info)



# インターフェース
qCtrl_control_browser    = 'temp/control_browser.txt'
qCtrl_control_self       = qCtrl_control_browser



# 共通ルーチン
import  _v5__qRiKi
qRiKi = _v5__qRiKi.qRiKi_class()
import  _v5__qFunc
qFunc = _v5__qFunc.qFunc_class()
import  _v5__qLog
qLog  = _v5__qLog.qLog_class()

qPLATFORM        = qRiKi.getValue('qPLATFORM'        )
qRUNATTR         = qRiKi.getValue('qRUNATTR'         )
qHOSTNAME        = qRiKi.getValue('qHOSTNAME'        )
qUSERNAME        = qRiKi.getValue('qUSERNAME'        )
qPath_pictures   = qRiKi.getValue('qPath_pictures'   )
qPath_videos     = qRiKi.getValue('qPath_videos'     )
qPath_cache      = qRiKi.getValue('qPath_cache'      )
qPath_sounds     = qRiKi.getValue('qPath_sounds'     )
qPath_icons      = qRiKi.getValue('qPath_icons'      )
qPath_fonts      = qRiKi.getValue('qPath_fonts'      )
qPath_log        = qRiKi.getValue('qPath_log'        )
qPath_work       = qRiKi.getValue('qPath_work'       )
qPath_rec        = qRiKi.getValue('qPath_rec'        )

qPath_s_ctrl     = qRiKi.getValue('qPath_s_ctrl'     )
qPath_s_inp      = qRiKi.getValue('qPath_s_inp'      )
qPath_s_wav      = qRiKi.getValue('qPath_s_wav'      )
qPath_s_jul      = qRiKi.getValue('qPath_s_jul'      )
qPath_s_STT      = qRiKi.getValue('qPath_s_STT'      )
qPath_s_TTS      = qRiKi.getValue('qPath_s_TTS'      )
qPath_s_TRA      = qRiKi.getValue('qPath_s_TRA'      )
qPath_s_play     = qRiKi.getValue('qPath_s_play'     )
qPath_v_ctrl     = qRiKi.getValue('qPath_v_ctrl'     )
qPath_v_inp      = qRiKi.getValue('qPath_v_inp'      )
qPath_v_jpg      = qRiKi.getValue('qPath_v_jpg'      )
qPath_v_detect   = qRiKi.getValue('qPath_v_detect'   )
qPath_v_cv       = qRiKi.getValue('qPath_v_cv'       )
qPath_v_photo    = qRiKi.getValue('qPath_v_photo'    )
qPath_v_msg      = qRiKi.getValue('qPath_v_msg'      )
qPath_d_ctrl     = qRiKi.getValue('qPath_d_ctrl'     )
qPath_d_play     = qRiKi.getValue('qPath_d_play'     )
qPath_d_prtscn   = qRiKi.getValue('qPath_d_prtscn'   )
qPath_d_movie    = qRiKi.getValue('qPath_d_movie'    )
qPath_d_upload   = qRiKi.getValue('qPath_d_upload'   )

qBusy_dev_cpu    = qRiKi.getValue('qBusy_dev_cpu'    )
qBusy_dev_com    = qRiKi.getValue('qBusy_dev_com'    )
qBusy_dev_mic    = qRiKi.getValue('qBusy_dev_mic'    )
qBusy_dev_spk    = qRiKi.getValue('qBusy_dev_spk'    )
qBusy_dev_cam    = qRiKi.getValue('qBusy_dev_cam'    )
qBusy_dev_dsp    = qRiKi.getValue('qBusy_dev_dsp'    )
qBusy_dev_scn    = qRiKi.getValue('qBusy_dev_scn'    )
qBusy_s_ctrl     = qRiKi.getValue('qBusy_s_ctrl'     )
qBusy_s_inp      = qRiKi.getValue('qBusy_s_inp'      )
qBusy_s_wav      = qRiKi.getValue('qBusy_s_wav'      )
qBusy_s_STT      = qRiKi.getValue('qBusy_s_STT'      )
qBusy_s_TTS      = qRiKi.getValue('qBusy_s_TTS'      )
qBusy_s_TRA      = qRiKi.getValue('qBusy_s_TRA'      )
qBusy_s_play     = qRiKi.getValue('qBusy_s_play'     )
qBusy_v_ctrl     = qRiKi.getValue('qBusy_v_ctrl'     )
qBusy_v_inp      = qRiKi.getValue('qBusy_v_inp'      )
qBusy_v_QR       = qRiKi.getValue('qBusy_v_QR'       )
qBusy_v_jpg      = qRiKi.getValue('qBusy_v_jpg'      )
qBusy_v_CV       = qRiKi.getValue('qBusy_v_CV'       )
qBusy_d_ctrl     = qRiKi.getValue('qBusy_d_ctrl'     )
qBusy_d_inp      = qRiKi.getValue('qBusy_d_inp'      )
qBusy_d_QR       = qRiKi.getValue('qBusy_d_QR'       )
qBusy_d_rec      = qRiKi.getValue('qBusy_d_rec'      )
qBusy_d_telework = qRiKi.getValue('qBusy_d_telework' )
qBusy_d_play     = qRiKi.getValue('qBusy_d_play'     )
qBusy_d_browser  = qRiKi.getValue('qBusy_d_browser'  )
qBusy_d_upload   = qRiKi.getValue('qBusy_d_upload'   )
qRdy__s_force    = qRiKi.getValue('qRdy__s_force'    )
qRdy__s_fproc    = qRiKi.getValue('qRdy__s_fproc'    )
qRdy__s_sendkey  = qRiKi.getValue('qRdy__s_sendkey'  )
qRdy__v_mirror   = qRiKi.getValue('qRdy__v_mirror'   )
qRdy__v_reader   = qRiKi.getValue('qRdy__v_reader'   )
qRdy__v_sendkey  = qRiKi.getValue('qRdy__v_sendkey'  )
qRdy__d_reader   = qRiKi.getValue('qRdy__d_reader'   )
qRdy__d_sendkey  = qRiKi.getValue('qRdy__d_sendkey'  )



import _v5__qRiKi_key

config_file = '_v5__sub_browser_key.json'

qRiKi_key = _v5__qRiKi_key.qRiKi_key_class()
res, dic = qRiKi_key.getCryptJson(config_file=config_file, auto_crypt=False, )
if (res == False):
    dic['_crypt_']      = 'none'
    dic['engine']       = 'firefox'
    dic['url_home']     = 'https://google.co.jp'
    dic['url_search']   = 'https://www.google.com/search?q='
    dic['narou_home']   = 'https://syosetu.com/'
    dic['narou_base']   = 'https://ncode.syosetu.com/'
    dic['narou_speech'] = 'yes'
    res = qRiKi_key.putCryptJson(config_file=config_file, put_dic=dic, )



runMode = 'debug'



def clear_tts(proc_id, ):

    # TTSフォルダクリア
    path = qPath_s_TTS
    path_files = glob.glob(path + '*.' + proc_id + '.*')
    path_files.sort()
    if (len(path_files) > 0):
        for f in path_files:
            proc_file = f.replace('\\', '/')
            print(proc_file)
            qFunc.remove(proc_file)

    # Playフォルダクリア
    path = qPath_s_play
    path_files = glob.glob(path + '*.' + proc_id + '.*')
    path_files.sort()
    if (len(path_files) > 0):
        for f in path_files:
            proc_file = f.replace('\\', '/')
            print(proc_file)
            qFunc.remove(proc_file)

def html_narou_to_tts(abortQ=None, proc_id=None, base_url='', page_url='', html=None, autoPaging='yes', ):

    # 中断指示Q クリア
    if (not abortQ is None):
        if (abortQ.qsize() > 0):
            q_get  = abortQ.get()
            abortQ.task_done()

    # 無効 html ？
    if (html == None):
        return False

    # ページ情報
    page_sep = page_url.split('/')
    page_id  = ''
    page_seq = ''
    if (len(page_sep) >= 1):
        page_id  = page_sep[0]
    if (len(page_sep) >= 2):
        page_seq = page_sep[1]
    print(page_seq)

    # 無効 ページ ？
    if (page_seq == ''):
        return False
    if (not page_seq.isnumeric()):
        return False

    # TTS 出力（タイトル）
    try:
        soup = BeautifulSoup(html, 'html.parser')
        capter_title = ''
        try:
            capter_title = soup.find('p', class_='chapter_title')
        except:
            capter_title = soup.find('p', class_='margin_r20')
        print(capter_title.text)
        sub_title = soup.find('p', class_='novel_subtitle')
        print(sub_title.text)
        txt = 'ja,' + u'タイトル'
        qRiKi.tts(id=proc_id, text=txt, idolSec=0, maxWait=0, )
        time.sleep(1.2)
        txt = 'ja,' + capter_title.text + ' ' + sub_title.text
        qRiKi.tts(id=proc_id, text=txt, idolSec=0, maxWait=0, )
        time.sleep(1.2)
    except:
        pass

    # TTS 出力（本文）
    for i in range(1, 9999):

        # 中断処理
        if (not abortQ is None):
            if (abortQ.qsize() > 0):
                q_get  = abortQ.get()
                abortQ.task_done()
                return False

        try:
            p_list = soup.find_all('p', id='L' + str(i))
            if (len(p_list) == 0):
                break
            if (i == 1):
                txt = 'ja,' + u'本文'
                qRiKi.tts(id=proc_id, text=txt, idolSec=0, maxWait=0, )
                time.sleep(1.2)
            for p in p_list:
                txt = p.text
                print(txt)
                txt = txt.replace(u'「', '')
                txt = txt.replace(u'」', '')
                txt = txt.replace(u'…', ' ')
                txt = 'ja,' + txt
                qRiKi.tts(id=proc_id, text=txt, idolSec=0, maxWait=0, )
                time.sleep(1.2)
        except:
            pass

    # 自動ページング
    if (autoPaging != 'yes'):
        return True
    
    # 音声待機
    check = 5
    while (check > 0):
        if (qRiKi.statusWait_speech() == False): # busy
            check -= 1
        else:
            check = 5
        # 中断処理
        if (not abortQ is None):
            if (abortQ.qsize() > 0):
                q_get  = abortQ.get()
                abortQ.task_done()
                return True

    # ジャンプ
    next_page = base_url + page_id + '/' + str(int(page_seq) + 1) + '/'
    qFunc.txtsWrite(filename=qCtrl_control_self, txts=[next_page], exclusive=True, )

    return True



class main_browser:

    def __init__(self, name='thread', id='0', runMode='debug', ):
        self.runMode   = runMode

        self.breakFlag = threading.Event()
        self.breakFlag.clear()
        self.name      = name
        self.id        = id
        self.proc_id   = '{0:10s}'.format(name).replace(' ', '_')
        self.proc_id   = self.proc_id[:-2] + '_' + str(id)
        if (runMode == 'debug'):
            self.logDisp = True
        else:
            self.logDisp = False
        qLog.log('info', self.proc_id, 'init', display=self.logDisp, )

        self.proc_s    = None
        self.proc_r    = None
        self.proc_main = None
        self.proc_beat = None
        self.proc_last = None
        self.proc_step = '0'
        self.proc_seq  = 0

        self.browser_id    = None 
        self.browser_start = time.time() 
        self.browser_url   = ''
        self.browser_html  = None
        self.last_url      = None

        self.batch_thread  = None
        self.batch_abortQ  = queue.Queue()

        # 構成情報
        json_file = '_v5__sub_browser_key.json'
        self.engine       = 'firefox'
        self.url_home     = 'https://google.co.jp'
        self.url_search   = 'https://www.google.com/search?q='
        self.narou_home   = 'https://syosetu.com/'
        self.narou_base   = 'https://ncode.syosetu.com/'
        self.narou_speech = 'yes'
        res, json_dic = qRiKi_key.getCryptJson(config_file=json_file, auto_crypt=False, )
        if (res == True):
            self.engine       = json_dic['engine']
            self.url_home     = json_dic['url_home']
            self.url_search   = json_dic['url_search']
            self.narou_home   = json_dic['narou_home']
            self.narou_base   = json_dic['narou_base']
            self.narou_speech = json_dic['narou_speech']

    def __del__(self, ):
        qLog.log('info', self.proc_id, 'bye!', display=self.logDisp, )

    def begin(self, ):
        #qLog.log('info', self.proc_id, 'start')

        self.fileRun = qPath_work + self.proc_id + '.run'
        self.fileRdy = qPath_work + self.proc_id + '.rdy'
        self.fileBsy = qPath_work + self.proc_id + '.bsy'
        qFunc.statusSet(self.fileRun, False)
        qFunc.statusSet(self.fileRdy, False)
        qFunc.statusSet(self.fileBsy, False)

        self.proc_s = queue.Queue()
        self.proc_r = queue.Queue()
        self.proc_main = threading.Thread(target=self.main_proc, args=(self.proc_s, self.proc_r, ))
        self.proc_beat = time.time()
        self.proc_last = time.time()
        self.proc_step = '0'
        self.proc_seq  = 0

        self.proc_main.setDaemon(True)
        self.proc_main.start()

    def abort(self, waitMax=5, ):
        qLog.log('info', self.proc_id, 'stop', display=self.logDisp, )

        self.breakFlag.set()
        chktime = time.time()
        while (not self.proc_beat is None) and ((time.time() - chktime) < waitMax):
            time.sleep(0.25)
        chktime = time.time()
        while (os.path.exists(self.fileRun)) and ((time.time() - chktime) < waitMax):
            time.sleep(0.25)

    def put(self, data, ):
        self.proc_s.put(data)
        return True

    def checkGet(self, waitMax=5, ):
        chktime = time.time()
        while (self.proc_r.qsize() == 0) and ((time.time() - chktime) < waitMax):
            time.sleep(0.10)
        data = self.get()
        return data

    def get(self, ):
        if (self.proc_r.qsize() == 0):
            return ['', '']
        data = self.proc_r.get()
        self.proc_r.task_done()
        return data

    def main_proc(self, cn_r, cn_s, ):
        # ログ
        qLog.log('info', self.proc_id, 'start', display=self.logDisp, )
        qFunc.statusSet(self.fileRun, True)
        self.proc_beat = time.time()

        # 初期設定
        self.proc_step = '1'

        txts, txt = qFunc.txtsRead(qCtrl_control_self)
        if (txts != False):
            if (txt == '_end_'):
                qFunc.remove(qCtrl_control_self)

        # 待機ループ
        self.proc_step = '5'

        onece = True
        last_alive = time.time()

        while (self.proc_step == '5'):
            self.proc_beat = time.time()

            # 終了確認
            control = ''
            txts, txt = qFunc.txtsRead(qCtrl_control_self)
            if (txts != False):
                qLog.log('info', self.proc_id, '' + str(txt))
                if (txt == '_end_'):
                    break
                else:
                    qFunc.remove(qCtrl_control_self)
                    control = txt

            # 停止要求確認
            if (self.breakFlag.is_set()):
                self.breakFlag.clear()
                self.proc_step = '9'
                break

            # 活動メッセージ
            if  ((time.time() - last_alive) > 30):
                qLog.log('debug', self.proc_id, 'alive', display=True, )
                last_alive = time.time()

            # キュー取得
            if (cn_r.qsize() > 0):
                cn_r_get  = cn_r.get()
                inp_name  = cn_r_get[0]
                inp_value = cn_r_get[1]
                cn_r.task_done()
            else:
                inp_name  = ''
                inp_value = ''

            if (cn_r.qsize() > 1) or (cn_s.qsize() > 20):
                qLog.log('warning', self.proc_id, 'queue overflow warning!, ' + str(cn_r.qsize()) + ', ' + str(cn_s.qsize()))

            # レディー設定
            if (qFunc.statusCheck(self.fileRdy) == False):
                qFunc.statusSet(self.fileRdy, True)

            # ステータス応答
            if (inp_name.lower() == '_status_'):
                out_name  = inp_name
                out_value = '_ready_'
                cn_s.put([out_name, out_value])

            # 処理
            if (control != ''):
                self.sub_proc(control, )

            # 検査
            self.sub_check_url()

            # アイドリング
            slow = False
            if  (qFunc.statusCheck(qBusy_dev_cpu) == True):
                slow = True
            if  (qFunc.statusCheck(qBusy_dev_mic) == True):
                slow = True

            if (slow == True):
                time.sleep(1.00)
            else:
                if (cn_r.qsize() == 0):
                    time.sleep(0.50)
                else:
                    time.sleep(0.25)

        # 終了処理
        if (True):

            # レディー解除
            qFunc.statusSet(self.fileRdy, False)

            # 停止
            if (not self.browser_id is None):
                self.sub_proc('_stop_', )

            # ビジー解除
            qFunc.statusSet(self.fileBsy, False)
            if (str(self.id) == '0'):
                qFunc.statusSet(qBusy_d_browser, False)

            # キュー削除
            while (cn_r.qsize() > 0):
                cn_r_get = cn_r.get()
                cn_r.task_done()
            while (cn_s.qsize() > 0):
                cn_s_get = cn_s.get()
                cn_s.task_done()

            # ログ
            qLog.log('info', self.proc_id, 'end', display=self.logDisp, )
            qFunc.statusSet(self.fileRun, False)
            self.proc_beat = None



    # 処理
    def sub_proc(self, proc_text, ):

        if (proc_text.find(u'リセット') >=0):

            # 停止
            if (not self.browser_id is None):
                #self.sub_stop(proc_text, )
                self.sub_stop('_stop_', )

        elif (proc_text.lower() == '_stop_') \
          or (proc_text.find(u'WEB') >=0)      and (proc_text.find(u'停止') >=0) \
          or (proc_text.find(u'WEB') >=0)      and (proc_text.find(u'終了') >=0) \
          or (proc_text.find(u'ウェブ') >=0)   and (proc_text.find(u'停止') >=0) \
          or (proc_text.find(u'ウェブ') >=0)   and (proc_text.find(u'終了') >=0) \
          or (proc_text.find(u'ブラウザ') >=0) and (proc_text.find(u'停止') >=0) \
          or (proc_text.find(u'ブラウザ') >=0) and (proc_text.find(u'終了') >=0):

            # 停止
            if (not self.browser_id is None):
                #self.sub_stop(proc_text, )
                self.sub_stop('_stop_', )

        elif (proc_text.lower() == '_start_') \
          or (proc_text.find(u'WEB') >=0)     and (proc_text.find(u'開始') >=0) \
          or (proc_text.find(u'ウェブ') >=0)   and (proc_text.find(u'開始') >=0) \
          or (proc_text.find(u'ブラウザ') >=0) and (proc_text.find(u'開始') >=0):

            # 開始
            self.sub_start('_start_', )

        else:

            # 開始
            if (not self.browser_id is None):
                self.sub_start(proc_text, )



    # 開始
    def sub_start(self, proc_text, ):

        # ログ
        qLog.log('info', self.proc_id, 'open ' + proc_text, display=True,)

        # オープン
        if (self.browser_id is None):

            # ビジー設定
            if (qFunc.statusCheck(self.fileBsy) == False):
                qFunc.statusSet(self.fileBsy, True)
                if (str(self.id) == '0'):
                    qFunc.statusSet(qBusy_d_browser, True)

            # ヘッドレスモードオプション
            options = FirefoxOptions()
            #options.add_argument('-headless')

            # FirefoxのWebDriver作成
            self.browser_id   = Firefox(options=options)

            # ウィンドウサイズとズームを設定
            #driver.set_window_size(1920, 9999)
            #driver.execute_script("document.body.style.zoom='100%'")

        # URLを開く
        url   = ''
        if (proc_text == '_start_'):
            url = self.url_home     #'https://google.co.jp'
            #self.browser_id.get(url)
        elif (proc_text[:4] == 'http'):
            url = proc_text
            #self.browser_id.get(url)
        elif (proc_text == u'なろう') or (proc_text == u'本好き'):
            url = self.narou_home     #'https://syosetu.com/'
            #self.browser_id.get(url)

        if (url == ''):
            url = self.url_search + proc_text     #'https://www.google.com/search?q='
            #self.browser_id.get(url)

        # 開く
        try:
            self.browser_id.get(url)
        except Exception as e:
            self.sub_stop('_stop_', )



    # 停止
    def sub_stop(self, proc_text, ):

        if (not self.browser_id is None):

            # 音声読み上げキャンセル
            if (not self.batch_thread is None):
                self.batch_abortQ.put('_abort_')
                time.sleep(2.00)
                self.batch_thread = None
            clear_tts(self.proc_id, )

            # 停止
            self.browser_id.quit()
            self.browser_id = None

        # リセット
        #qFunc.kill('firefox', )
        qFunc.kill(self.engine, )

        # ビジー解除
        qFunc.statusSet(self.fileBsy, False)
        if (str(self.id) == '0'):
            qFunc.statusSet(qBusy_d_browser, False)



    # 検査
    def sub_check_url(self, ):

        # 表示中？
        if (self.browser_id is None):
            self.browser_url  = None
            self.browser_html = None
            self.last_url     = None
            return False

        # 変化？
        self.browser_url = self.browser_id.current_url
        if (self.browser_url == self.last_url):
            return False

        #visibility_of_all_elements_located
        #ページの全要素がDOM上に現れ, かつheight・widthが0以上になるまで待機
        self.browser_wait = WebDriverWait(self.browser_id, 10)
        element = self.browser_wait.until(EC.visibility_of_all_elements_located)

        # 画像保管
        self.browser_html = self.browser_id.page_source
        self.last_url     = self.browser_url
        print(self.browser_url)
        #self.browser_id.save_screenshot(file_name)

        # 音声読み上げキャンセル
        if (not self.batch_thread is None):
            self.batch_abortQ.put('_abort_')
            time.sleep(2.00)
            self.batch_thread = None
        clear_tts(self.proc_id, )

        # なろうページ読み上げ
        if (self.narou_speech == 'yes'):
            base_url = self.narou_base     #'https://ncode.syosetu.com/'
            if (self.browser_url[:len(base_url)] == base_url):

                page_url = self.browser_url[len(base_url):]
                # threading
                self.batch_thread = threading.Thread(target=html_narou_to_tts, args=(
                        self.batch_abortQ, self.proc_id, 
                        base_url, page_url, self.browser_html, 'yes', 
                        ))
                self.batch_thread.setDaemon(True)
                self.batch_thread.start()

        return True



# シグナル処理
import signal
def signal_handler(signal_number, stack_frame):
    print(os.path.basename(__file__), 'accept signal =', signal_number)

#signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGINT,  signal.SIG_IGN)
signal.signal(signal.SIGTERM, signal.SIG_IGN)



if __name__ == '__main__':
    main_name = 'browser'
    main_id   = '{0:10s}'.format(main_name).replace(' ', '_')

    # 共通クラス
    qRiKi.init()
    qFunc.init()

    # ログ
    nowTime  = datetime.datetime.now()
    filename = qPath_log + nowTime.strftime('%Y%m%d.%H%M%S') + '.' + os.path.basename(__file__) + '.log'
    qLog.init(mode='logger', filename=filename, )

    qLog.log('info', main_id, 'init')
    qLog.log('info', main_id, 'exsample.py runMode, ')

    # パラメータ

    if (True):

        if (len(sys.argv) >= 2):
            runMode  = str(sys.argv[1]).lower()

        qLog.log('info', main_id, 'runMode  =' + str(runMode  ))

    # 初期設定

    if (True):

        txts, txt = qFunc.txtsRead(qCtrl_control_self)
        if (txts != False):
            if (txt == '_end_'):
                qFunc.remove(qCtrl_control_self)

    # 起動

    if (True):

        qLog.log('info', main_id, 'start')

        main_core = main_browser(main_name, '0', runMode=runMode, )
        main_core.begin()

        main_start = time.time()
        onece      = True

    # 待機ループ

    while (True):

        # 終了確認
        txts, txt = qFunc.txtsRead(qCtrl_control_self)
        if (txts != False):
            if (txt == '_end_'):
                break

        # デバッグ
        if (runMode == 'debug'):

            # テスト開始
            if  ((time.time() - main_start) > 1):
                if (onece == True):
                    onece = False
                    qFunc.txtsWrite(qCtrl_control_self ,txts=['_start_'], encoding='utf-8', exclusive=True, mode='w', )
                    time.sleep(5.00)
                    qFunc.txtsWrite(qCtrl_control_self ,txts=['http://yahoo.co.jp'], encoding='utf-8', exclusive=True, mode='w', )
                    time.sleep(5.00)
                    qFunc.txtsWrite(qCtrl_control_self ,txts=[u'姫路城'], encoding='utf-8', exclusive=True, mode='w', )
                    time.sleep(5.00)
                    qFunc.txtsWrite(qCtrl_control_self ,txts=[u'本好き'], encoding='utf-8', exclusive=True, mode='w', )

            # テスト終了
            if  ((time.time() - main_start) > 40):
                    qFunc.txtsWrite(qCtrl_control_self ,txts=['_stop_'], encoding='utf-8', exclusive=True, mode='w', )
                    time.sleep(5.00)
                    qFunc.txtsWrite(qCtrl_control_self ,txts=['_end_'], encoding='utf-8', exclusive=True, mode='w', )

        # アイドリング
        slow = False
        if   (qFunc.statusCheck(qBusy_dev_cpu) == True):
            slow = True
        elif (qFunc.statusCheck(qBusy_dev_mic) == True):
            slow = True

        if (slow == True):
            time.sleep(1.00)
        else:
            time.sleep(0.50)

    # 終了

    if (True):

        qLog.log('info', main_id, 'terminate')

        main_core.abort()
        del main_core

        qLog.log('info', main_id, 'bye!')

        sys.exit(0)


