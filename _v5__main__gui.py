#!/usr/bin/env python
# -*- coding: utf-8 -*-

# COPYRIGHT (C) 2014-2020 Mitsuo KONDOU.
# This software is released under the MIT License.
# https://github.com/konsan1101
# Thank you for keeping the rules.



import os
import time

import PySimpleGUI as sg
import psutil



class sgDashGraph(object):

    def __init__(self, graph_elem, starting_count, color):
        self.GRAPH_WIDTH = 120
        self.GRAPH_HEIGHT = 40

        self.graph_current_item = 0
        self.graph_elem = graph_elem
        self.prev_value = starting_count
        self.max_sent = 1
        self.color = color

    def graph_value(self, current_value):
        delta = current_value - self.prev_value
        self.prev_value = current_value
        self.max_sent = max(self.max_sent, delta)
        percent_sent = 100 * delta / self.max_sent
        self.graph_elem.draw_line((self.graph_current_item, 0),
                                  (self.graph_current_item, percent_sent),
                                  color=self.color)
        if self.graph_current_item >= self.GRAPH_WIDTH:
            self.graph_elem.move(-1, 0)
        else:
            self.graph_current_item += 1
        return delta

    def graph_percentage_abs(self, value):
        self.graph_elem.draw_line((self.graph_current_item, 0),
                                  (self.graph_current_item, value),
                                  color=self.color)
        if self.graph_current_item >= self.GRAPH_WIDTH:
            self.graph_elem.move(-1, 0)
        else:
            self.graph_current_item += 1

def bytes2str(bytes, units=['  Byte', ' KByte', ' MByte', ' GByte', ' TByte', ' PByte', ' EByte']):
    if (bytes < 1024):
        return '{:4d}'.format(bytes) + units[0]
    else:
        return bytes2str(int(bytes) >> 10, units[1:])

def sgGraphColumn(name, key):
    GRAPH_WIDTH = 120
    GRAPH_HEIGHT = 40

    layout = [
        [sg.Text(name, font=('Courier 8'), key=key+'TXT_')],
        [sg.Graph((GRAPH_WIDTH, GRAPH_HEIGHT),
                    (0, 0),
                    (GRAPH_WIDTH, 120),
                    background_color='black',
                    key=key+'GRAPH_')]]
    return sg.Col(layout, pad=(2, 2))

def sgButton(name, key):
    btn = sg.Button(name, key=key, size=(15,2),
                          button_color=('white','darkcyan'), pad=(1, 1))
    return btn

class main_gui_class:

    def __init__(self, ):

        # 初期化
        self.window = None


    def init(self, alpha_channel=1,):

        # pySimpleGUI
        sg.theme('Black')
        sg.set_options(element_padding=(0,0), margins=(1,1), border_width=0)

        # レイアウト
        red_x = "R0lGODlhEAAQAPeQAIsAAI0AAI4AAI8AAJIAAJUAAJQCApkAAJoAAJ4AAJkJCaAAAKYAAKcAAKcCAKcDA6cGAKgAAKsAAKsCAKwAAK0AAK8AAK4CAK8DAqUJAKULAKwLALAAALEAALIAALMAALMDALQAALUAALYAALcEALoAALsAALsCALwAAL8AALkJAL4NAL8NAKoTAKwbAbEQALMVAL0QAL0RAKsREaodHbkQELMsALg2ALk3ALs+ALE2FbgpKbA1Nbc1Nb44N8AAAMIWAMsvAMUgDMcxAKVABb9NBbVJErFYEq1iMrtoMr5kP8BKAMFLAMxKANBBANFCANJFANFEB9JKAMFcANFZANZcANpfAMJUEMZVEc5hAM5pAMluBdRsANR8AM9YOrdERMpIQs1UVMR5WNt8X8VgYMdlZcxtYtx4YNF/btp9eraNf9qXXNCCZsyLeNSLd8SSecySf82kd9qqc9uBgdyBgd+EhN6JgtSIiNuJieGHhOGLg+GKhOKamty1ste4sNO+ueenp+inp+HHrebGrefKuOPTzejWzera1O7b1vLb2/bl4vTu7fbw7ffx7vnz8f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJAALAAAAAAQABAAAAjUACEJHEiwYEEABniQKfNFgQCDkATQwAMokEU+PQgUFDAjjR09e/LUmUNnh8aBCcCgUeRmzBkzie6EeQBAoAAMXuA8ciRGCaJHfXzUMCAQgYooWN48anTokR8dQk4sELggBhQrU9Q8evSHiJQgLCIIfMDCSZUjhbYuQkLFCRAMAiOQGGLE0CNBcZYmaRIDLqQFGF60eTRoSxc5jwjhACFWIAgMLtgUocJFy5orL0IQRHAiQgsbRZYswbEhBIiCCH6EiJAhAwQMKU5DjHCi9gnZEHMTDAgAOw=="
        layout = [
                # タイトル
                [sg.Button('', image_data=red_x, key='-exit-',  button_color=('black', 'black'), tooltip='Closes'), sg.Text('Power of AI, RiKi,')],
                # 内容
                [
                    # Extention
                    sg.Frame(layout=[
                            [sg.Text('')],
                            [sg.Button('プログラム開始', key=u'RiKi,プログラム開始', size=(18,2))],
                            [sg.Text('')],
                            [sg.Button('プログラム終了', key=u'RiKi,プログラム終了', size=(18,2))],
                            [sg.Text('')],
                            [sg.Button('', key=u'13', size=(18,2), button_color=('white','black'))],
                            [sg.Text('')],
                            [sg.Button('', key=u'14', size=(18,2), button_color=('white','black'))],
                            [sg.Text('')],
                            [sg.Button('', key=u'15', size=(18,2), button_color=('white','black'))],
                            [sg.Text('')],
                            [sg.Button('', key=u'16', size=(18,2), button_color=('white','black'))],
                            [sg.Text('')],
                            [sg.Text('Now Telework !', key='_STS_TELEWORK_', size=(18,1), justification='center', background_color='gray')],
                        ], title='Extention Command'),
                    # vision
                    sg.Frame(layout=[
                            [sg.Text('')],
                            [sg.Button('カメラ開始', key=u'RiKi,カメラ開始', size=(18,2))],
                            [sg.Text('')],
                            [sg.Button('ミラー開始', key=u'RiKi,ミラー開始', size=(18,2))],
                            [sg.Text('')],
                            [sg.Button('', key=u'23', size=(18,2), button_color=('white','black'))],
                            [sg.Text('')],
                            [sg.Button('', key=u'24', size=(18,2), button_color=('white','black'))],
                            [sg.Text('')],
                            [sg.Button('', key=u'25', size=(18,2), button_color=('white','black'))],
                            [sg.Text('')],
                            [sg.Button('全て終了', key=u'RiKi,カメラ終了', size=(18,2))],
                            [sg.Text('')],
                            [sg.Text('')],
                        ], title='Vision Command'),
                    # desktop
                    sg.Frame(layout=[
                            [sg.Text('')],
                            [sg.Button('テレワーク開始', key=u'RiKi,テレワーク開始', size=(18,2))],
                            [sg.Text('')],
                            [sg.Button('１分記録', key=u'RiKi,１分記録', size=(18,2))],
                            [sg.Text('')],
                            [sg.Button('記録開始', key=u'RiKi,記録開始', size=(18,2))],
                            [sg.Text('')],
                            [sg.Button('録画開始', key=u'RiKi,録画開始', size=(18,2))],
                            [sg.Text('')],
                            [sg.Button('', key=u'35', size=(18,2), button_color=('white','black'))],
                            [sg.Text('')],
                            [sg.Button('全て終了', key=u'RiKi,記録・録画・テレワーク終了', size=(18,2))],
                            [sg.Text('')],
                            [sg.Text('Now Recording !', key='_STS_RECORD_', size=(18,1), justification='center', background_color='gray')],
                        ], title='Desktop Command'),
                    # kernel
                    sg.Frame(layout=[
                            [sg.Text('')],
                            [sg.Button('リセット', key=u'RiKi,リセット', size=(18,2))],
                            [sg.Text('')],
                            [sg.Button('リブート', key=u'RiKi,リブート', size=(18,2))],
                            [sg.Text('')],
                            [sg.Button('', key=u'43', size=(18,2), button_color=('white','black'))],
                            [sg.Text('')],
                            [sg.Button('', key=u'44', size=(18,2), button_color=('white','black'))],
                            [sg.Text('')],
                            [sg.Button('', key=u'45', size=(18,2), button_color=('white','black'))],
                            [sg.Text('')],
                            [sg.Button('システム終了', key=u'RiKi,システム終了', size=(18,2))],
                            [sg.Text('')],
                            [sg.Text('Speech READY !', key='_STS_SPEECH_', size=(18,1), justification='center', background_color='gray')],
                        ], title='Kernel Command'),
                    # status
                    sg.Frame(layout=[

                            # Graph
                            [sgGraphColumn('CPU Usage          ', '_CPU_')],
                            [sgGraphColumn('MEM Usage          ', '_MEM_')],
                            [sgGraphColumn('NET Out            ', '_NET_OUT_')],
                            [sgGraphColumn('NET In             ', '_NET_IN_')],
                            [sgGraphColumn('DISK Read          ', '_DISK_READ_')],
                            [sgGraphColumn('DISK Write         ', '_DISK_WRITE_')],
                            [sg.Text(' ', font=('Courier 6'))],

                        ], title='System Status'),
                ],
                #　ボタン
                [sg.Text('_' * 256, size=(120,1))],
                [sgButton('ＯＫ', key='-ok-'), sg.Text(' ', size=(5,2)), sgButton('キャンセル', key='-cancel-')],
        ]

        # 定義
        self.close()
        #try:
        if True:
            self.window = sg.Window('Power of AI, RiKi, ', layout,
                            keep_on_top=True,
                            no_titlebar=True,
                            alpha_channel=alpha_channel,
                            finalize=True,
                            size=(760, 480),
                            )

            # setup graphs & initial values
            self.cpu_usage_graph = sgDashGraph(self.window['_CPU_GRAPH_'], 0, '#d34545')
            self.mem_usage_graph = sgDashGraph(self.window['_MEM_GRAPH_'], 0, '#BE7C29')
            net_io = psutil.net_io_counters()
            net_in = self.window['_NET_IN_GRAPH_']
            self.net_graph_in = sgDashGraph(net_in, net_io.bytes_recv, '#23a0a0')
            net_out = self.window['_NET_OUT_GRAPH_']
            self.net_graph_out = sgDashGraph(net_out, net_io.bytes_sent, '#56d856')
            disk_io = psutil.disk_io_counters()
            self.disk_graph_write = sgDashGraph(self.window['_DISK_WRITE_GRAPH_'], disk_io.write_bytes, '#be45be')
            self.disk_graph_read = sgDashGraph(self.window['_DISK_READ_GRAPH_'], disk_io.read_bytes, '#5681d8')

            # status reset
            self.status_speech = False
            self.window['_STS_SPEECH_'].update('', background_color='black', )
            self.status_record = False
            self.window['_STS_RECORD_'].update('', background_color='black', )
            self.status_telework = False
            self.window['_STS_TELEWORK_'].update('', background_color='black', )

        #except:
        #    self.window = None

        if (not self.window is None):
            return True
        else:
            return False

    def open(self, ):
        # 更新・表示
        try:
            if (not self.window is None):
                self.window.refresh()
                return True
        except:
            pass
        return False

    def read(self, ):
        # update graphs
        cpu = psutil.cpu_percent(0)
        self.cpu_usage_graph.graph_percentage_abs(cpu)
        self.window['_CPU_TXT_'].update('CPU    {:5.1f} %'.format(cpu))
        mem_used = psutil.virtual_memory().percent
        self.mem_usage_graph.graph_percentage_abs(mem_used)
        self.window['_MEM_TXT_'].update('MEM    {:5.1f} %'.format(mem_used))
        net_io = psutil.net_io_counters()
        write_bytes = self.net_graph_out.graph_value(net_io.bytes_sent)
        read_bytes = self.net_graph_in.graph_value(net_io.bytes_recv)
        self.window['_NET_OUT_TXT_'].update('NET  O:{}'.format(bytes2str(write_bytes)))
        self.window['_NET_IN_TXT_'].update('NET  I:{}'.format(bytes2str(read_bytes)))
        disk_io = psutil.disk_io_counters()
        write_bytes = self.disk_graph_write.graph_value(disk_io.write_bytes)
        read_bytes = self.disk_graph_read.graph_value(disk_io.read_bytes)
        self.window['_DISK_WRITE_TXT_'].update('DISK W:{}'.format(bytes2str(write_bytes)))
        self.window['_DISK_READ_TXT_'].update('DISK R:{}'.format(bytes2str(read_bytes)))

        # update status
        if (self.status_speech != True):
            self.window['_STS_SPEECH_'].update('', background_color='black', )
        else:
            self.window['_STS_SPEECH_'].update('Speech READY !', background_color='green')
        if (self.status_record != True):
            self.window['_STS_RECORD_'].update('', background_color='black', )
        else:
            self.window['_STS_RECORD_'].update('Now Recording !', background_color='magenta')
        if (self.status_telework != True):
            self.window['_STS_TELEWORK_'].update('', background_color='black', )
        else:
            self.window['_STS_TELEWORK_'].update('Now Telework !', background_color='magenta')

        # 読取
        try:
            if (not self.window is None):
                event, values = self.window.read(timeout=20, timeout_key='-timeout-')
                return event, values
        except:
            pass
        return False, False

    def statusSet(self, key, value):
        if   (key == '_STS_SPEECH_'):
            self.status_speech = value
        elif (key == '_STS_RECORD_'):
            self.status_record = value
        elif (key == '_STS_TELEWORK_'):
            self.status_telework = value
        return True

    def close(self, ):
        # 消去
        if (not self.window is None):
            try:
                self.read()
                self.window.hide()
            except:
                pass
        return True

    def terminate(self, ):
        # 終了
        if (not self.window is None):
            try:
                self.read()
                self.window.close()
                del self.window
            except:
                pass
        self.window = None
        return True



if __name__ == '__main__':

    GUI = main_gui_class()

    GUI.init()
    GUI.open()

    chkTime = time.time()
    while ((time.time() - chkTime) < 30):
        event, values = GUI.read()
        #print(event)
        if (event in (None, '-exit-', '-cancel-')):
            break
        if (event == '-ok-'):
            print(event, values)
            break
        if (event[:5].lower() == 'riki,'):
            print(event, values)
            break

        if ((time.time() - chkTime) > 5):
            GUI.statusSet('_STS_SPEECH_',   True)
        if ((time.time() - chkTime) > 10):
            GUI.statusSet('_STS_RECORD_',   True)
        if ((time.time() - chkTime) > 15):
            GUI.statusSet('_STS_RECORD_',   False)
            GUI.statusSet('_STS_TELEWORK_', True)

        time.sleep(0.10)

    GUI.close()
    GUI.terminate()


