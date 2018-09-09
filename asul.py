from ASULBOT import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from multiprocessing import Pool, Process
from ffmpy import FFmpeg
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pytz, wikipedia, pafy, youtube_dl, atexit

print ("\n\n ---  ASUL BOT PY3 ยินดีต้อนรับ  ---\n")

botStart = time.time()

line = ASUL("Eww3ioLLLvipR5B9bco6.xxD+zgW3gaYtM/L6PqLWLG.55rbVTeS6v+h4v3UlOVFbVbSUpdnp/hsALnip7dBE2w=")
#line = ASUL("EusluwKjSfKXnfAvzFH1.KaptOybxCrifYDMnQKDtuq.cUjlo0FXzIMK949AR/qSrXOgNXlIchCUJdSgL6CUc0E=")#ร่างคิก
#line = ASUL("Email","Password")
line.log("Auth Token : " + str(line.authToken))
channelToken = line.getChannelResult()
#line.log("Channel Token : " + str(channelToken))

#as1 = ASUL("Etb0ASZe1ecdQHKxfgA6.u1a+KpknCNGv1jGvlGx9vG.6xX3kweoGWQZUSO56pHhoXZeYvnKEmbhSFPYhDNCrRU=")
#as1 = ASUL("EvLk6domTEjne1EuFZz6.u1a+KpknCNGv1jGvlGx9vG.wGLgaHee1Fj5EoHTOcxzcCenkCy/wQSQbjyjbs0Vm60=")#ราชา
#as1 = ASUL("Email","Password")
#as1 = ASUL()
#as1.log("Auth Token : " + str(as1.authToken))
#channelToken = as1.getChannelResult()
#as1.log("Channel Token : " + str(channelToken))

as1 = line

ki2 = ASUL

AsulLogged = False

#readOpen = codecs.open("read.json","r","utf-8")
#settingsOpen = codecs.open("temp.json","r","utf-8")

lineMID = line.profile.mid
as1MID = as1.profile.mid
lineProfile = line.getProfile()
as1Profile = as1.getProfile()
lineSettings = line.getSettings()
as1Settings = as1.getSettings()

oepoll = ASULPoll(line)
oepoll1 = ASULPoll(as1)

responsename = line.getProfile().displayName
responsename2 = as1.getProfile().displayName


#read = json.load(readOpen)
#settings = json.load(settingsOpen)

#settings["myProfile"]["displayName"] = lineProfile.displayName 
#settings["myProfile"]["statusMessage"] = lineProfile.statusMessage
#settings["myProfile"]["pictureStatus"] = lineProfile.pictureStatus

admin=[lineMID,"u5d777f646c37180c939be97aa5097096"]

Owner=[lineMID,"u5d777f646c37180c939be97aa5097096"]

Bots=[lineMID,as1MID]

KAC=[as1]

#==============================================================================#
settings = {
    "autoAdd": True,
    "autoBlock": False,
    "autoJoin": True,
    "autoLeave": True,
    "autoRead": False,
    "Api": False,
    "lang":"JP",
    "blacklist":{},
    "wblack": False,
    "wblacklist": False,
    "dblack": False,
    "dblacklist": False,
    "protect": False,
    "qrprotect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "detectMention": True,
    "Mentionkick": False,
    "admin": False,
    "checkContact": False,
    "changeGroupPicture":[],
    "changePicture": {},
    "changePicture1": {},
    "Sambutan": True,
    "Sider":{},
    "checkSticker": False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

lgncall = ""
def logincall(this):
    line.sendMessage(lgncall,"Asul login url: " + this)

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

cctv = {
    "cyduk":{},
    "point":{},
    "MENTION":{},
    "sidermem":{}
}

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus

user1 = lineMID
user2 = ""
#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMessage(to, Message, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes._from = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

        
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[คนที่อ่าน {} คน]\n╠ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠⎆ "
            else:
                try:
                    textx += "╚══[กลุ่ม👉 {} ]".format(str(line.getGroup(to).name))
                except:
                    pass
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def helpmessage():
    helpMessage = "╔══[ASUL BOT PY3]" + "\n" + \
                  "╠ Help" + "\n" + \
                  "╠ Translate" + "\n" + \
                  "╠ TextToSpeech" + "\n" + \
                  "╠══[ Status Command ]" + "\n" + \
                  "╠ Restart" + "\n" + \
                  "╠ Runtime" + "\n" + \
                  "╠ Speed" + "\n" + \
                  "╠ Status" + "\n" + \
                  "╠ About" + "\n" + \
                  "╠══[ Settings Command ]" + "\n" + \
                  "╠ AutoAdd「On/Off」" + "\n" + \
                  "╠ AutoJoin「On/Off」" + "\n" + \
                  "╠ AutoLeave「On/Off」" + "\n" + \
                  "╠ AutoRead「On/Off」" + "\n" + \
                  "╠ CheckSticker「On/Off」" + "\n" + \
                  "╠ DetectMention「On/Off」" + "\n" + \
                  "╠══[ Self Command ]" + "\n" + \
                  "╠ Me" + "\n" + \
                  "╠ MyMid" + "\n" + \
                  "╠ MyName" + "\n" + \
                  "╠ MyBio" + "\n" + \
                  "╠ MyPicture" + "\n" + \
                  "╠ MyVideoProfile" + "\n" + \
                  "╠ MyCover" + "\n" + \
                  "╠ StealContact「Mention」" + "\n" + \
                  "╠ StealMid「Mention」" + "\n" + \
                  "╠ StealName「Mention」" + "\n" + \
                  "╠ StealBio「Mention」" + "\n" + \
                  "╠ StealPicture「Mention」" + "\n" + \
                  "╠ StealVideoProfile「Mention」" + "\n" + \
                  "╠ StealCover「Mention」" + "\n" + \
                  "╠ CloneProfile「Mention」" + "\n" + \
                  "╠ RestoreProfile" + "\n" + \
                  "╠══[ Group Command ]" + "\n" + \
                  "╠ GroupCreator" + "\n" + \
                  "╠ GroupId" + "\n" + \
                  "╠ GroupName" + "\n" + \
                  "╠ GroupPicture" + "\n" + \
                  "╠ GroupTicket" + "\n" + \
                  "╠ GroupTicket「On/Off」" + "\n" + \
                  "╠ GroupList" + "\n" + \
                  "╠ GroupMemberList" + "\n" + \
                  "╠ GroupInfo" + "\n" + \
                  "╠══[ Special Command ]" + "\n" + \
                  "╠ Mimic「On/Off」" + "\n" + \
                  "╠ MimicList" + "\n" + \
                  "╠ MimicAdd「Mention」" + "\n" + \
                  "╠ MimicDel「Mention」" + "\n" + \
                  "╠ Mention" + "\n" + \
                  "╠ Lurking「On/Off/Reset」" + "\n" + \
                  "╠ Lurking" + "\n" + \
                  "╠══[ Media Command ]" + "\n" + \
                  "╠ Kalender" + "\n" + \
                  "╠ CheckDate「Date」" + "\n" + \
                  "╠ InstagramInfo「UserName」" + "\n" + \
                  "╠ InstagramPost「UserName」" + "\n" + \
                  "╠ SearchYoutube「Search」" + "\n" + \
                  "╠ SearchMusic「Search」" + "\n" + \
                  "╠ SearchLyric「Search」" + "\n" + \
                  "╠ SearchImage「Search」" + "\n" + \
                  "╠ ScreenshootWebsite「LinkURL」" + "\n" + \
                  "╚══[ASUL Bot Py3]\n [By:┅═हवさູ১さั৩ழণ১ह═┅]"
    return helpMessage
    
def helpmessage2():
    helpMessage2 = """||<<<<✒️✒️ASUL BOT PY3✒️✒>>>>
|| <<<ชุดคำสั่ง>>>️ 
||✒️✒ ️คำสั่ง 
||✒️✒️ คท
||✒️✒️ คท @
||✒️✒ ล่องหน  「ดึงคท.ล่องหน」
||✒️✒️ ไอดี
||✒️✒️ ไอดี @
||✒️✒ ไอดีล่องหน  「ดึงไอดีล่องหน」
||✒️✒️ ปก
||✒️✒️ ปก @
||✒️✒️ ดิส
||✒️✒️ ดิส @
||✒️✒ เปลี่ยนดิส
||✒️✒️ ตัส
||✒️✒️ ตัส @
||✒️✒️ วีดีโอ
||✒️✒️ วีดีโอ @
||✒️✒️ ชื่อ
||✒️✒️ ชื่อ @
||✒️✒ อัพชื่อ 「ใส่ชื่อ」
||✒️✒ Restart  
||✒️✒ Runtime
||✒️✒ Speed
||✒️✒ ข้อมูล
||✒️✒ Copy @
||✒️✒ กลับร่าง
||✒️✒ พูด 「ใส่ข้อความ」
||✒️✒ หารูป 「ใส่ที่ต้องการค้นหา」
||✒️✒ แทค
||✒️✒ แทคล่องหน
||✒️✒ เตะล่องหน
||✒️✒ Virus  「ปล่อยไวรัส」
||✒️✒ ยูทูป 「ใส่ที่ต้องการค้นหา」
||✒️✒ ออก 「ชื่อกลุ่ม」
||✒️✒ ลบรัน,Reject
||✒️✒ ขอลิ้ง  「ขอลิ้งให้เพื่อนล็อคอิน」
||✒️✒ .     「เชคสถานะล็อคอิน」
||✒️✒ ลบรัน1  「ลบรันให้เพื่อน」
||✒️✒ ดำ  -เพิ่มบัญชีดำ
||✒️✒ ขาว  -แก้บัญชีดำ
||✒️✒ เชคดำ
||✒️✒ ล้างดำ
|| <<<คำสั่งเชคคนอ่าน>>>
||✒️✒ เปิดอ่าน  -เชครวม
||✒️✒ ปิดอ่าน
||✒️✒ อ่าน
||✒️✒ เปิดเชค  -เชคคนอ่านรายบุคคล
||✒️✒ ปิดเชค  -ปิดเชคคนอ่านรายบุคคล
|| <<<คำสั่งกลุ่ม>>>
||✒️✒ GroupInfo
||✒️✒ GroupMemberList
||✒️✒ GroupList
||✒️✒ GroupName
||✒️✒ GroupCreator
||✒️✒ GroupId
||✒️✒ GroupPicture
||✒️✒ GroupTicket
||✒️✒ เปิดหมด/ปิดหมด -เปิด/ปิดป้องกันทั้งหมด
||✒️✒ เปิดกัน/ปิดกัน  -เปิด/ปิดป้องกันเตะ
||✒️✒ เปิดกันลิ้ง/ปิดกันลิ้ง
||✒️✒ เปิดเชิญ/ปิดเชิญ
||✒️✒ เปิดกันลิ้ง/ปิดกันลิ้ง
||✒️✒ เปิดกันยก/ปิดกันยก
||✒️✒ เชคกัน  -เชคการตั้งค่าป้องกัน
|| <<<คำสั่งตั้งค่า>>>
||✒️✒ เชคค่า
||✒️✒ เปิดแอด,ปิดแอด
||✒️✒ เปิดออก,ปิดออก
||✒️✒ เปิดเข้า,ปิดเข้า
||✒️✒ เปิดแทค,ปิดแทค
||✒️✒ เปิดทัก,ปิดทัก
||✒️✒ Read「On/Off」
||✒️✒ CheckSticker「On/Off」
|| <<<คำสั่งคิกเกอร์>>>
||✒️✒ คิกเข้า
||✒️✒ คิกออก
||✒️✒ เชคชื่อ  -เชคชื่อบอท
||✒️✒ เชคบอท  -เชคคทบอท
||✒️✒ ล้างห้อง  -ตามนั้น
||✒️✒✒️✒️✒️✒️✒️✒️✒️✒️✒️✒️✒️✒️
|| <<<<<ASUL BOT PY3>>>>>
|| <BY ═हवさູ১さั৩ழণ১ह═ >

"""
    return helpMessage2


def helptexttospeech():
    helpTextToSpeech =   "╔══[ T E X T   T O   S P E E C H ]" + "\n" + \
                         "╠ af : Afrikaans" + "\n" + \
                         "╠ sq : Albanian" + "\n" + \
                         "╠ ar : Arabic" + "\n" + \
                         "╠ hy : Armenian" + "\n" + \
                         "╠ bn : Bengali" + "\n" + \
                         "╠ ca : Catalan" + "\n" + \
                         "╠ zh : Chinese" + "\n" + \
                         "╠ zh-cn : Chinese (Mandarin/China)" + "\n" + \
                         "╠ zh-tw : Chinese (Mandarin/Taiwan)" + "\n" + \
                         "╠ zh-yue : Chinese (Cantonese)" + "\n" + \
                         "╠ hr : Croatian" + "\n" + \
                         "╠ cs : Czech" + "\n" + \
                         "╠ da : Danish" + "\n" + \
                         "╠ nl : Dutch" + "\n" + \
                         "╠ en : English" + "\n" + \
                         "╠ en-au : English (Australia)" + "\n" + \
                         "╠ en-uk : English (United Kingdom)" + "\n" + \
                         "╠ en-us : English (United States)" + "\n" + \
                         "╠ eo : Esperanto" + "\n" + \
                         "╠ fi : Finnish" + "\n" + \
                         "╠ fr : French" + "\n" + \
                         "╠ de : German" + "\n" + \
                         "╠ el : Greek" + "\n" + \
                         "╠ hi : Hindi" + "\n" + \
                         "╠ hu : Hungarian" + "\n" + \
                         "╠ is : Icelandic" + "\n" + \
                         "╠ id : Indonesian" + "\n" + \
                         "╠ it : Italian" + "\n" + \
                         "╠ ja : Japanese" + "\n" + \
                         "╠ km : Khmer (Cambodian)" + "\n" + \
                         "╠ ko : Korean" + "\n" + \
                         "╠ la : Latin" + "\n" + \
                         "╠ lv : Latvian" + "\n" + \
                         "╠ mk : Macedonian" + "\n" + \
                         "╠ no : Norwegian" + "\n" + \
                         "╠ pl : Polish" + "\n" + \
                         "╠ pt : Portuguese" + "\n" + \
                         "╠ ro : Romanian" + "\n" + \
                         "╠ ru : Russian" + "\n" + \
                         "╠ sr : Serbian" + "\n" + \
                         "╠ si : Sinhala" + "\n" + \
                         "╠ sk : Slovak" + "\n" + \
                         "╠ es : Spanish" + "\n" + \
                         "╠ es-es : Spanish (Spain)" + "\n" + \
                         "╠ es-us : Spanish (United States)" + "\n" + \
                         "╠ sw : Swahili" + "\n" + \
                         "╠ sv : Swedish" + "\n" + \
                         "╠ ta : Tamil" + "\n" + \
                         "╠ th : Thai" + "\n" + \
                         "╠ tr : Turkish" + "\n" + \
                         "╠ uk : Ukrainian" + "\n" + \
                         "╠ vi : Vietnamese" + "\n" + \
                         "╠ cy : Welsh" + "\n" + \
                         "╚══[ Jangan Typo ]" + "\n" + "\n\n" + \
                          "Contoh : ˢᴬᵞ-ᴵᴰ ᶠᴱᴺᴰᵞ ᴶᴱᴸᴱˣ"
    return helpTextToSpeech
    
def helptranslate():
    helpTranslate =    "╔══[ T R A N S L A T E ]" + "\n" + \
                       "╠ af : afrikaans" + "\n" + \
                       "╠ sq : albanian" + "\n" + \
                       "╠ am : amharic" + "\n" + \
                       "╠ ar : arabic" + "\n" + \
                       "╠ hy : armenian" + "\n" + \
                       "╠ az : azerbaijani" + "\n" + \
                       "╠ eu : basque" + "\n" + \
                       "╠ be : belarusian" + "\n" + \
                       "╠ bn : bengali" + "\n" + \
                       "╠ bs : bosnian" + "\n" + \
                       "╠ bg : bulgarian" + "\n" + \
                       "╠ ca : catalan" + "\n" + \
                       "╠ ceb : cebuano" + "\n" + \
                       "╠ ny : chichewa" + "\n" + \
                       "╠ zh-cn : chinese (simplified)" + "\n" + \
                       "╠ zh-tw : chinese (traditional)" + "\n" + \
                       "╠ co : corsican" + "\n" + \
                       "╠ hr : croatian" + "\n" + \
                       "╠ cs : czech" + "\n" + \
                       "╠ da : danish" + "\n" + \
                       "╠ nl : dutch" + "\n" + \
                       "╠ en : english" + "\n" + \
                       "╠ eo : esperanto" + "\n" + \
                       "╠ et : estonian" + "\n" + \
                       "╠ tl : filipino" + "\n" + \
                       "╠ fi : finnish" + "\n" + \
                       "╠ fr : french" + "\n" + \
                       "╠ fy : frisian" + "\n" + \
                       "╠ gl : galician" + "\n" + \
                       "╠ ka : georgian" + "\n" + \
                       "╠ de : german" + "\n" + \
                       "╠ el : greek" + "\n" + \
                       "╠ gu : gujarati" + "\n" + \
                       "╠ ht : haitian creole" + "\n" + \
                       "╠ ha : hausa" + "\n" + \
                       "╠ haw : hawaiian" + "\n" + \
                       "╠ iw : hebrew" + "\n" + \
                       "╠ hi : hindi" + "\n" + \
                       "╠ hmn : hmong" + "\n" + \
                       "╠ hu : hungarian" + "\n" + \
                       "╠ is : icelandic" + "\n" + \
                       "╠ ig : igbo" + "\n" + \
                       "╠ id : indonesian" + "\n" + \
                       "╠ ga : irish" + "\n" + \
                       "╠ it : italian" + "\n" + \
                       "╠ ja : japanese" + "\n" + \
                       "╠ jw : javanese" + "\n" + \
                       "╠ kn : kannada" + "\n" + \
                       "╠ kk : kazakh" + "\n" + \
                       "╠ km : khmer" + "\n" + \
                       "╠ ko : korean" + "\n" + \
                       "╠ ku : kurdish (kurmanji)" + "\n" + \
                       "╠ ky : kyrgyz" + "\n" + \
                       "╠ lo : lao" + "\n" + \
                       "╠ la : latin" + "\n" + \
                       "╠ lv : latvian" + "\n" + \
                       "╠ lt : lithuanian" + "\n" + \
                       "╠ lb : luxembourgish" + "\n" + \
                       "╠ mk : macedonian" + "\n" + \
                       "╠ mg : malagasy" + "\n" + \
                       "╠ ms : malay" + "\n" + \
                       "╠ ml : malayalam" + "\n" + \
                       "╠ mt : maltese" + "\n" + \
                       "╠ mi : maori" + "\n" + \
                       "╠ mr : marathi" + "\n" + \
                       "╠ mn : mongolian" + "\n" + \
                       "╠ my : myanmar (burmese)" + "\n" + \
                       "╠ ne : nepali" + "\n" + \
                       "╠ no : norwegian" + "\n" + \
                       "╠ ps : pashto" + "\n" + \
                       "╠ fa : persian" + "\n" + \
                       "╠ pl : polish" + "\n" + \
                       "╠ pt : portuguese" + "\n" + \
                       "╠ pa : punjabi" + "\n" + \
                       "╠ ro : romanian" + "\n" + \
                       "╠ ru : russian" + "\n" + \
                       "╠ sm : samoan" + "\n" + \
                       "╠ gd : scots gaelic" + "\n" + \
                       "╠ sr : serbian" + "\n" + \
                       "╠ st : sesotho" + "\n" + \
                       "╠ sn : shona" + "\n" + \
                       "╠ sd : sindhi" + "\n" + \
                       "╠ si : sinhala" + "\n" + \
                       "╠ sk : slovak" + "\n" + \
                       "╠ sl : slovenian" + "\n" + \
                       "╠ so : somali" + "\n" + \
                       "╠ es : spanish" + "\n" + \
                       "╠ su : sundanese" + "\n" + \
                       "╠ sw : swahili" + "\n" + \
                       "╠ sv : swedish" + "\n" + \
                       "╠ tg : tajik" + "\n" + \
                       "╠ ta : tamil" + "\n" + \
                       "╠ te : telugu" + "\n" + \
                       "╠ th : thai" + "\n" + \
                       "╠ tr : turkish" + "\n" + \
                       "╠ uk : ukrainian" + "\n" + \
                       "╠ ur : urdu" + "\n" + \
                       "╠ uz : uzbek" + "\n" + \
                       "╠ vi : vietnamese" + "\n" + \
                       "╠ cy : welsh" + "\n" + \
                       "╠ xh : xhosa" + "\n" + \
                       "╠ yi : yiddish" + "\n" + \
                       "╠ yo : yoruba" + "\n" + \
                       "╠ zu : zulu" + "\n" + \
                       "╠ fil : Filipino" + "\n" + \
                       "╠ he : Hebrew" + "\n" + \
                       "╚══[ Jangan Typo ]" + "\n" + "\n\n" + \
                         "Contoh : ˢᴬᵞ-ᴵᴰ ᶠᴱᴺᴰᵞ ᴶᴱᴸᴱˣ"
    return helpTranslate
#==============================================================================#
def lineBot(op):
    global AsulLogged
    global ki2
    global user2
    global readAlert
    global lgncall
    global save1
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                line.sendMessage(op.param1, "ระบบตอบรับอัตโนมัติ  ASUL BOT Python3 By ┅═हवさູ১さั৩ழণ১ह═┅ \nปล.ถ้าจะแอดมาถามเรื่องเชลรึขอสคิป ผมไม่สอนนะ ทำไว้เล่นเอง".format(str(line.getContact(op.param1).displayName)))
        if op.type == 5:
            print ("[ 5 ] NOTIFIED BLOCK CONTACT")
            if settings["autoBlock"] == True:
                line.blockContact(op.param1)
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            group = line.getGroup(op.param1)
            if settings["autoJoin"] == True:
                line.acceptGroupInvitation(op.param1)
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                line.leaveRoom(op.param1)
#-------------------------------------------------------------------------------
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        line.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        line.sendMessage(msg.to,"Itu tidak berkomentar")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        line.sendMessage(msg.to,"Done")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        line.sendMessage(msg.to,"Tidak ada dalam daftar hitam")
#-------------------------------------------------------------------------------
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        line.sendMessage(msg.to,"อยุ่ในบัญชีดำแล้ว")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        line.sendMessage(msg.to,"เรียบร้อย")
                        
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        line.sendMessage(msg.to,"เรียบร้อย")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        line.sendMessage(msg.to,"เรียบร้อย")
#-------------------------------------------------------------------------------
        if op.type == 25 or op.type == 26:
            print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
            if msg._from in admin:
                if msg.text in ["Help"]:
                    helpMessage = helpmessage()
                    line.sendMessage(to, str(helpMessage))
                    line.sendContact(to, "u5d777f646c37180c939be97aa5097096")
                elif msg.text in ["คำสั่ง","คส"]:
                    helpMessage2 = helpmessage2()
                    line.sendMessage(to, str(helpMessage2))
                    line.sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/19/20180619_163340.jpg")
                elif msg.text in ["สั่ง1"]:
                    line.sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/19/20180619_140004.png")
                    line.sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/19/20180619_140114.png")
                    line.sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/19/20180619_140151.png")
                elif text.lower() == 'texttospeech':
                    helpTextToSpeech = helptexttospeech()
                    line.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == 'translate':
                    helpTranslate = helptranslate()
                    line.sendMessage(to, str(helpTranslate))
#==============================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    line.sendMessage(to, "██████████████99%Complete")
                    elapsed_time = time.time() - start
                    line.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'ksp':
                    start = time.time()
                    as1.sendMessage(to, "██████████████99%Complete")
                    elapsed_time = time.time() - start
                    as1.sendMessage(to,format(str(elapsed_time)))
                elif msg.text in ["Restart","รีบูต","รบ"]:
                    line.sendMessage(to, "██████████████99%Complete")
                    time.sleep(7)
                    line.sendMessage(to, "Restart เรียบร้อย")
                    restartBot()
                elif text.lower() == 'ออน':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "ASUL Bot ทำงานแล้วเป็นเวลา {}".format(str(runtime)))
                elif text.lower() == 'ข้อมูล':
                    try:
                        arr = []
                        owner = "u5d777f646c37180c939be97aa5097096"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╔══[ ข้อมูลผู้ใช้ ]"
                        ret_ += "\n╠ Line : {}".format(contact.displayName)
                        ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ ข้อมูลบอท ]"
                        ret_ += "\n╠ Version : ASUL 1Kicker"
                        ret_ += "\n╠ Creator : {}".format(creator.displayName)
                        ret_ += "\n╚══[ ASUL Bot Py3 By:┅═हवさູ১さั৩ழণ১ह═┅ ]"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'เชคค่า':
                    try:
                        ret_ = "╔══[ การตั้งค่า ]"
                        if settings["autoAdd"] == True: ret_ += "\n╠⎆ Auto Add ✅"
                        else: ret_ += "\n╠⎆ Auto Add ❌"
                        if settings["autoBlock"] == True: ret_ += "\n╠⎆ Auto Block ✅"
                        else: ret_ += "\n╠⎆ Auto Block ❌"
                        if settings["autoJoin"] == True: ret_ += "\n╠⎆ Auto Join ✅"
                        else: ret_ += "\n╠⎆ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n╠⎆ Auto Leave ✅"
                        else: ret_ += "\n╠⎆ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠⎆ Auto Read ✅"
                        else: ret_ += "\n╠⎆ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n╠⎆ Check Sticker ✅"
                        else: ret_ += "\n╠⎆ Check Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n╠ Detect Mention ✅"
                        else: ret_ += "\n╠⎆ Detect Mention ❌"
                        if settings["Mentionkick"] == True: ret_ += "\n╠⎆ เตะคนแทค ✅"
                        else: ret_ += "\n╠⎆ เตะคนแทค ❌"
                        if settings["checkContact"] == True: ret_ += "\n╠⎆ เชคคท. ✅"
                        else: ret_ += "\n╠⎆ เชคคท. ❌"
                        if settings["Sambutan"] == True: ret_ += "\n╠⎆ ข้อความทักทาย ✅"
                        else: ret_ += "\n╠⎆ ข้อความทักทาย ❌"
                        if settings["Api"] == True: ret_ += "\n╠ ระบบAPI ✅"
                        else: ret_ += "\n╠⎆ ระบบAPI ❌"
                        ret_ += "\n╚══[ การตั้งค่า ]"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                
                elif text.lower() == 'เชคกัน':
                    try:
                        ret_ = "╔══[ การตั้งค่าป้องกัน ]"
                        if settings["protect"] == True: ret_ += "\n╠⎆ บอทกัน ✅"
                        else: ret_ += "\n╠⎆ บอทกัน ❌"
                        if settings["qrprotect"] == True: ret_ += "\n╠⎆ กันลิ้ง ✅"
                        else: ret_ += "\n╠⎆ กันลิ้ง ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n╠⎆ กันเชิญ ✅"
                        else: ret_ += "\n╠⎆ กันเชิญ ❌"
                        if settings["cancelprotect"] == True: ret_ += "\n╠⎆ กันยก ✅"
                        else: ret_ += "\n╠⎆ กันยก ❌"
                        ret_ += "\n╚══[ การตั้งค่าป้องกัน ]"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#-------------------------------------------------------------------------------
                elif text.lower() == 'เปิดกัน':
                    if msg._from in Owner:
                        if settings["protect"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ ระบบป้องกันเปิดอยู่")
                            else:
                                line.sendMessage(msg.to,"➲ เปิดระบบป้องกัน")
                        else:
                            settings["protect"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ เปิดระบบป้องกัน")
                            else:
                                line.sendMessage(msg.to,"➲ ระบบป้องกันเปิดอยู่")
                                
                elif text.lower() == 'ปิดกัน':
                    if msg._from in Owner:
                        if settings["protect"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ ระบบป้องกันปิดอยู่")
                            else:
                                line.sendMessage(msg.to,"➲ ปิดระบบป้องกัน")
                        else:
                            settings["protect"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ ปิดระบบป้องกัน")
                            else:
                                line.sendMessage(msg.to,"➲ ระบบป้องกันปิดอยู่")
#----------------------------------------------------------------------------------------                        
                elif text.lower() == 'เปิดกันลิ้ง':
                    if msg._from in Owner:
                        if settings["qrprotect"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ ระบบกันลิ้งเปิดอยู่")
                            else:
                                line.sendMessage(msg.to,"➲ เปิดระบบกันลิ้ง")
                        else:
                            settings["qrprotect"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ เปิดระบบกันลิ้ง")
                            else:
                                line.sendMessage(msg.to,"➲ ระบบกันลิ้งเปิดอยู่")
                                
                elif text.lower() == 'ปิดกันลิ้ง':
                    if msg._from in Owner:
                        if settings["qrprotect"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ ระบบกันลิ้งปิดอยู่")
                            else:
                                line.sendMessage(msg.to,"➲ ปิดระบบกันลิ้ง")
                        else:
                            settings["qrprotect"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ ปิดระบบกันลิ้ง")
                            else:
                                line.sendMessage(msg.to,"➲ ระบบกันลิ้งปิดอยุ่")
#-------------------------------------------------------------------------------
                elif text.lower() == 'ปิดเชิญ':
                    if msg._from in Owner:
                        if settings["inviteprotect"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ ระบบกันเชิญเปิดอยู่")
                            else:
                                line.sendMessage(msg.to,"➲ เปิดระบบกันเชิญ")
                        else:
                            settings["inviteprotect"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ เปิดระบบกันเชิญ")
                            else:
                                line.sendMessage(msg.to,"➲ ระบบกันเชิญเปิดอยู่")
                                
                elif text.lower() == 'เปิดเชิญ':
                    if msg._from in Owner:
                        if settings["inviteprotect"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ ระบบกันเชิญปิดอยู่")
                            else:
                                line.sendMessage(msg.to,"➲ ปิดระบบกันเชิญ")
                        else:
                            settings["inviteprotect"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ ปิดระบบกันเชิญ")
                            else:
                                line.sendMessage(msg.to,"➲ ระบบกันเชิญปิดอยู่")
#-------------------------------------------------------------------------------
                elif text.lower() == 'เปิดกันยก':
                    if msg._from in Owner:
                        if settings["cancelprotect"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Already On")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Set To On")
                        else:
                            settings["cancelprotect"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Set To On")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Already On")
                                
                elif text.lower() == 'ปิดกันยก':
                    if msg._from in Owner:
                        if settings["cancelprotect"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Already Off")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Set To Off")
                        else:
                            settings["cancelprotect"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Set To Off")
                            else:
                                line.sendMessage(msg.to,"➲ Protection Cancel Invite Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'เปิดหมด':
                    if msg._from in Owner:
                        settings["protect"] = True
                        settings["qrprotect"] = True
                        settings["inviteprotect"] = True
                        settings["cancelprotect"] = True
                        line.sendMessage(msg.to,"➲ เปิดระบบป้องทั้งหมด")
                    else:
                        line.sendMessage(msg.to,"ต้องสั่งโดยผู้สร้างเท่านั้น")
                        		            
                elif text.lower() == 'ปิดหมด':
                    if msg._from in Owner:
                        settings["protect"] = False
                        settings["qrprotect"] = False
                        settings["inviteprotect"] = False
                        settings["cancelprotect"] = False
                        line.sendMessage(msg.to,"➲ ปิดระบบป้องกันทั้งหมด")
                    else:
                        line.sendMessage(msg.to,"ต้องสั่งโดยผู้สร้างเท่านั้น")
#-------------------------------------------------------------------------------
                elif text.lower() == 'เปิดแอด':
                    settings["autoAdd"] = True
                    settings["autoBlock"] = False
                    line.sendMessage(to, "เปิด Auto Add✔️\nปิดAuto Block❌")
                elif text.lower() == 'ปิดแอด':
                    settings["autoAdd"] = False
                    settings["autoBlock"] = True
                    line.sendMessage(to, "ปิด Auto Add❌\nเปิด Auto Block✔️")
                elif text.lower() == 'เปิดเข้า':
                    settings["autoJoin"] = True
                    line.sendMessage(to, "เปิด Auto Join✔️")
                elif text.lower() == 'ปิดเข้า':
                    settings["autoJoin"] = False
                    line.sendMessage(to, "ปิด Auto Join❌")
                elif text.lower() == 'เปิดออก':
                    settings["autoLeave"] = True
                    line.sendMessage(to, "เปิด Auto Leave")
                elif text.lower() == 'ปิดออก':
                    settings["autoLeave"] = False
                    line.sendMessage(to, "ปิด Auto Leave")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    line.sendMessage(to, "เปิด Auto Read✔️")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    line.sendMessage(to, "ปิด Auto Read❌")
                elif text.lower() == 'checksticker on':
                    settings["checkSticker"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan Check Details Sticker")
                elif text.lower() == 'checksticker off':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan Check Details Sticker")
                elif text.lower() == 'เปิดแทค':
                    settings["detectMention"] = True
                    line.sendMessage(to, "เปิดตอบแทค✔️")
                elif text.lower() == 'ปิดแทค':
                    settings["detectMention"] = False
                    line.sendMessage(to, "ปิดตอบแทค❌")
                elif text.lower() == 'เปิดเตะแทค':
                    settings["Mentionkick"] = True
                    line.sendMessage(to, "เปิดเตะคนแทค✔️")
                elif text.lower() == 'ปิดเตะแทค':
                    settings["Mentionkick"] = False
                    line.sendMessage(to, "ปิดเตะคนแทค❌")
                elif text.lower() == 'เปิดพูด':
                    settings["Api"] = True
                    line.sendMessage(to, "เปิดระบบAPI✔️")
                elif text.lower() == 'ปิดพูด':
                    settings["Api"] = False
                    line.sendMessage(to, "ปิดระบบAPI❌")
                elif text.lower() == 'เปิดคท':
                    settings["checkContact"] = True
                    line.sendMessage(to, "เปิดเชคคท.✔️")
                elif text.lower() == 'ปิดคท':
                    settings["checkContact"] = False
                    line.sendMessage(to, "ปิดเชคคท.❌")
#==============================================================================#
                elif msg.text in ["ยก"]:
                   if msg.toType == 2:
                       X = line.getGroup(msg.to)
                       if X.invitee is not None:
                           gInviMids = [contact.mid for contact in X.invitee]
                           line.cancelGroupInvitation(msg.to, gInviMids)
                       else:
                           if settings["lang"] == "JP":
                               line.sendMessage(msg.to,"ไม่มีการเชิญ")
                           else:
                               line.sendMessage(msg.to,"ขออภัยไม่มี")
                   else:
                       if settings["lang"] == "JP":
                           line.sendMessage(msg.to,"ไม่สามารถใช้นอกกลุ่มได้")
                       else:
                           line.sendMessage(msg.to,"ไม่ใช้งานน้อยกว่ากลุ่ม")
#==============================================================================#
                elif msg.text in ["สาวมา","ทักสาว"]:
                     line.sendMessage(msg.to,"สวัสดีครับคนสวย")
                     as1.sendMessage(msg.to,"ชื่อตูนนะครับ")
                     line.sendMessage(msg.to,"อย่าเสือก!!!!")
                     time.sleep(0.2)
                     as1.sendMessage(msg.to,"เก๊าอยากม่อมั่งง่ะ")
                     time.sleep(0.1)
                     as1.sendMessage(msg.to,"😭😭😭")
                     time.sleep(0.2)
                     line.sendMessage(msg.to,"แม่ง วุ่นวายจิงๆ เดะไล่ออกแม่ง")
#==============================================================================#
                elif msg.text in ["Aslogin","ขอลิ้ง","qr"]:
                        if AsulLogged == False:
                            lgncall = msg.to
                            ki2 = ASUL(keepLoggedIn=logincall)
                            AsulLogged = True
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            line. sendMessage(msg.to,"ล็อคอินสำเร็จ Asul พร้อมใช้งานแล้ว"+tm)
                        else:
                            line.sendMessage(msg.to,"Asul ได้ทำการล็อคอินไปแล้ว")
                elif msg.text.lower() == ".":
                        gs = []
                        try:
                            gs = line.getGroup(msg.to).members
                        except:
                            try:
                                gs = line.getRoom(msg.to).contacts
                            except:
                                pass
                        tlist = ""
                        for i in gs:
                            tlist = tlist+i.displayName+" "+i.mid+"\n\n"
                        if AsulLogged == True:
                            try:
                                ki2.sendMessage(user1,tlist)
                            except:
                                ki2.new_post(tlist)
                        else:
                            line.sendMessage(msg.to,"Asul ยังไม่ได้ล็อคอิน")
#==============================================================================#
                elif msg.text in ["Reject","ลบรัน"]:
                    gid = line.getGroupIdsInvited()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    if settings["lang"] == "JP":
                        line.sendMessage(msg.to,"ปฏิเสทคำเชิญเข้ากลุ่มทั้งหมดเรียบร้อย")
                    else:
                        line.sendMessage(msg.to,"ไม่มีคำเชิญเข้าร่วมกลุ่ม")
                elif msg.text in ["Reject1","ลบรัน1"]:
                    gid = ki2.getGroupIdsInvited()
                    for i in gid:
                        ki2.rejectGroupInvitation(i)
                    if settings["lang"] == "JP":
                        ki2.sendMessage(msg.to,"ปฏิเสทค้างเชิญเรียบร้อย")
                    else:
                        ki2.sendMessage(msg.to,"ไม่มีคำเชิญเข้าร่วมกลุ่ม")
            
#==============================================================================#
                elif text.lower() == "เชคชื่อ":
                    line.sendMessage(msg.to,responsename)
                    as1.sendMessage(msg.to,responsename2)
                    
                elif msg.text.lower() == 'เชคบอท':
                    if msg._from in admin:
                        line.sendContact(to, lineMID)
                        as1.sendMessage(msg.to,"1!")
                        time.sleep(0.1)
                        line.sendMessage(msg.to,"ไอ้สัส ของกู")
                        time.sleep(0.2)
                        as1.sendMessage(msg.to,"เออ โทดที ลืม")
                        time.sleep(0.1)
                        line.sendMessage(msg.to,"ไปหมดละ สมงสมอง\n เห้อออ คิกเกอร์กู")
                        time.sleep(0.1)
                        line.sendMessage(msg.to,"1!")
                        as1.sendContact(to, as1MID)
                        as1.sendMessage(msg.to,"อั๊ยยะ สะสะสะสะ")
                        time.sleep(0.1)
                        as1.sendMessage(msg.to,"2!")
                        
                elif text.lower() in ["คิกออก"]:
                  if msg._from in admin:    
                    as1.leaveGroup(msg.to)
               
                elif text.lower() in ["คิกเข้า"]:
                  if msg._from in admin:    
                    G = line.getGroup(msg.to)
                    ginfo = line.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    line.updateGroup(G)
                    invsend = 0
                    Ticket = line.reissueGroupTicket(msg.to)
                    as1.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = line.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    line.updateGroup(G)
#-------------------------------------------------------------------------------
                elif text.lower() == 'ล้างดำ':
                    if msg._from in Owner:
                        settings["blacklist"] = {}
                        line.sendMessage(msg.to,"ลบรายชื่อบัญชีดำทั้งหมดแล้ว")
                        
                elif text.lower() == 'ดำ':
                    if msg._from in Owner:
                        settings["wblacklist"] = True
                        line.sendMessage(msg.to,"Send Contact")
                        
                elif msg.text in ["ขาว"]:
                    if msg._from in Owner:
                        settings["dblacklist"] = True
                        line.sendMessage(msg.to,"Send Contact")
#-------------------------------------------------------------------------------
                elif text.lower() == 'เชคดำ':
                    if msg._from in Owner:
                        if settings["blacklist"] == {}:
                            line.sendMessage(msg.to,"ไม่มีรายชื่อบัญชีดำ")
                        else:
                            line.sendMessage(msg.to,"รายชื่อบัญชีดำ")
                            num=1
                            msgs="══รายการ บัญชีดำ══"
                            for mi_d in settings["blacklist"]:
                                msgs+="\n[%i] %s" % (num, line.getContact(mi_d).displayName)
                                num=(num+1)
                            msgs+="\n══รายการ บัญชีดำ═══\n\nจำนวนคนในบัญชีดำ :  %i" % len(settings["blacklist"])
                            line.sendMessage(msg.to, msgs)
#==============================================================================#
                elif text.lower() == 'ล้างห้อง':
                    if msg._from in Owner:
                        if msg.toType == 2:
                            print ("[ 19 ] KICK ALL MEMBER")
                            _name = msg.text.replace("ล้างห้อง","")
                            gs = line.getGroup(msg.to)
                            gs = as1.getGroup(msg.to)
    #                       line.sendMessage(msg.to,"「 ราชาอสูรมาเยือน 」")
    #                       line.sendMessage(msg.to,"「 ขอต้อนรับสู่ห้องว่าง 」")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                line.sendMessage(msg.to,"ปีกหักอ่ะ")
                            else:
                                for target in targets:
                                    if not target in Bots:
                                        if not target in Owner:
                                            if not target in admin:
                                                try:
                                                    klist=[line,as1]
                                                    kicker=random.choice(klist)
                                                    kicker.kickoutFromGroup(msg.to,[target])
                                                    print (msg.to,[g.mid])
                                                except:
                                                    line.sendMessage(msg.to,"บายยย") 
#==============================================================================#
                elif msg.text in ["ผส.","Creator","ผุ้สร้าง"]:
                     line. sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/18/20180618_215830.jpg")
                     line.sendContact(to,"u5d777f646c37180c939be97aa5097096")
                     line.sendMessage(msg.to,"⬆🌟️นี่แหละผส.เชลAsul.py2-py3🌟")
                     line.sendMessage(msg.to,"หูยยย หล่อชิบหาย คนเหี้ยไรวะเนี่ย")
                elif msg.text in ["แฟน3ผส.","เมีย3ผส."]:
                     me1 = line.getContact("u23063489fe593c3c6ced7447facf7607")
                     line. sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me1.pictureStatus)
                     line.sendContact(to,"u23063489fe593c3c6ced7447facf7607")
                elif msg.text in ["คนใหนปากห้อย","ใครห้อย","ใครปากห้อย"]:
                     line. sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/19/1529403824690.jpg")
#                     line.sendContact(to,"u09d6e6f52a7c6d6f711db71a20a4a5eb")
                     line.sendMessage(msg.to,"☝️คนนี้แหละ เดินสะดุดปากห้อยตัวเองล้มหัวแตก")
                elif msg.text in ["เกบปาก","เก็บปาก"]:
                     line. sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/20/1529223154576.jpg")
                     line.sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/20/1529223156208.jpg")
                     line.sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/20/1529223157811.jpg")
                elif msg.text in ["Me","คท","กุ","เก๊า"]:
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                    line.sendMessage(msg.to,"A ҉s ҉u ҉l ҉ S ҉e ҉l ҉f ҉B ҉o ҉t ҉ P ҉Y ҉3 ҉")
                    line.sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/19/20180619_162547.jpg")
                elif msg.text in ["as1","คิก1"]:
                    as1.sendContact(to,as1MID)
                    as1.sendMessage(msg.to,"ASUL Kicker1")
                elif text.lower() == 'ไอดี':
                    line.sendMessage(msg.to,"[MID]\n" +  lineMID)
                elif text.lower() == 'ชื่อ':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'ตัส':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'ดิส':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'ตัวกุ':
                    line.sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/18/IMG_20180616_205733990.jpg")
                elif text.lower() == 'วีดีโอ':
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'ปก':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("คท "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("ไอดี "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ ไอดี ]"
                        for ls in lists:
                            ret_ += "\n👉" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("ชื่อ "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("ตัส "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("ดิส "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("วีดีโอ "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("ปก "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("copy "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            line.cloneContactProfile(contact)
                            line.sendMessage(msg.to, "กำลังก็อพปี้โปรไฟล์...")
                        except:
                            line.sendMessage(msg.to, "ไม่สามารถก็อพปี้ได้..")
                elif text.lower() == 'กลับร่าง':
                    try:
                        lineProfile.displayName = str(myProfile["displayName"])
                        lineProfile.statusMessage = str(myProfile["statusMessage"])
                        lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                        line.updateProfileAttribute(8, lineProfile.pictureStatus)
                        line.updateProfile(lineProfile)
                        line.sendMessage(msg.to, "กำลังกลับร่างเดิม")
                    except:
                        line.sendMessage(msg.to, "ไม่สามารถกลับร่างเดิมได้")
#==============================================================================#
                elif text.lower() == 'แทคล่องหน':
                    gs = line.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            sendMessageWithMention(to,target)
                elif text.lower() == 'ล่องหน':
                    gs = line.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            line.sendContact(msg.to,target)
                elif text.lower() == 'ไอดีล่องหน':
                    gs = line.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        mc = "ไอดีคนที่ใส่ชื่อล่องหน👇"
                        for mi_d in targets:
                            mc += "\n✒️->" + mi_d
                        line.sendMessage(to,mc)
                elif msg.text in ["เตะล่องหน"]:
                    gs = line.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    line.kickoutFromGroup(to,[target])
                                except:
                                    pass
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Target ditambahkan!")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"Target dihapuskan!")
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Reply Message off")
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                elif text.lower() == 'groupid':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'groupticket':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            line.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'ticket on':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "Berhasil membuka grup qr")
                elif text.lower() == 'ticket off':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "Berhasil menutup grup qr")
                elif text.lower() == 'ginfo':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == 'ceksider':
                                try:
                                    del cctv['point'][receiver]
                                    del cctv['sidermem'][receiver]
                                    del cctv['cyduk'][receiver]
                                except:
                                    pass
                                cctv['point'][receiver] = msg.id
                                cctv['sidermem'][receiver] = ""
                                cctv['cyduk'][receiver]=True
                elif text.lower() == 'offread':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][receiver]=False
                                    line.sendText(receiver, cctv['sidermem'][msg.to])

                elif text.lower() == 'เปิดทัก':
                   if settings["Sambutan"] == True:
                       if settings["lang"] == "JP":
                           line.sendMessage(msg.to,"ข้อความทักทายเปิดอยู่✔️")
                   else:
                       settings["Sambutan"] = True
                       if settings["lang"] == "JP":
                           line.sendMessage(msg.to,"เปิดข้อความทักทาย✔️")

                elif text.lower() == 'ปิดทัก':
                   if settings["Sambutan"] == False:
                       if settings["lang"] == "JP":
                          line.sendMessage(msg.to,"ข้อความทักทายปิดอยู่❌")
                   else: 
                       settings["Sambutan"] = False
                       if settings["lang"] == "JP":
                           line.sendMessage(msg.to,"ปิดข้อความทักทาย❌")

#==============================================================================#          
                elif text.lower() == 'แทค':
                            if msg.toType == 0:
                                sendMention(to, to, "", "")
                            elif msg.toType == 2:
                                group = line.getGroup(to)
                                contact = [mem.mid for mem in group.members]
                                ct1, ct2, ct3, ct4, ct5, jml = [], [], [], [], [], len(contact)
                                if jml <= 100:
                                    mentionMembers(to, contact)
                                elif jml > 100 and jml <= 200: 
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, jml):
                                        ct2 += [contact[b]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                elif jml > 200 and jml <= 300:
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, 199):
                                        ct2 += [contact[b]]
                                    for c in range(200, jml):
                                        ct3 += [contact[c]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                    mentionMembers(to, ct3)
                                elif jml > 300 and jml <= 400:
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, 199):
                                        ct2 += [contact[b]]
                                    for c in range(200, 299):
                                        ct3 += [contact[c]]
                                    for d in range(300, jml):
                                        ct4 += [contact[d]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                    mentionMembers(to, ct3)
                                    mentionMembers(to, ct4)
                                elif jml > 400 and jml <= 500:
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, 199):
                                        ct2 += [contact[b]]
                                    for c in range(200, 299):
                                        ct3 += [contact[c]]
                                    for d in range(300, 399):
                                        ct4 += [contact[d]]
                                    for e in range(400, jml):
                                        ct4 += [contact[e]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                    mentionMembers(to, ct3)
                                    mentionMembers(to, ct4)
                                    mentionMembers(to, ct5)
#===================================================================#
                elif "อัฟชื่อ " in msg.text:
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = line.getProfile()
                        profile.displayName = string
                        line.updateProfile(profile)
                        line.sendMessage(msg.to,"เปลี่ยนชื่อเป็น " + string + "")
#==============================================================================#
                elif msg.text in ["Virus","สังหาร"]:
                    line.sendContact(to, "Virus AsulBot Py3\nเด้งดึ๋งดีมั๊ยจ๊ะ อิอิ',")
#==============================================================================#
                elif text.lower() == 'เปลี่ยนดิส':
                            settings["changePicture"] = True
                            line.sendMessage(to, "กรุณาส่งรูป")
                elif text.lower() == 'เปลี่ยนดิส1':
                            settings["changePicture1"] = True
                            as1.sendMessage(to, "กรุณาส่งรูป")
                elif text.lower() == 'เปลี่ยนรูป':
                            if msg.toType == 2:
                                if to not in settings["changeGroupPicture"]:
                                    settings["changeGroupPicture"].append(to)
                                line.sendMessage(to, "กรุณาส่งรูป")


#==============================================

                elif text.lower() == 'เปิดอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hr + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nเวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                line.sendMessage(msg.to,"Lurking already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            line.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'ปิดอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hr + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        line.sendMessage(msg.to,"Lurking already off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        line.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'lurking reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        line.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        line.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'อ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hr + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nเวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            line.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ รายชื่อคนอ่าน ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ เวลา ]: \n" + readTime
                        try:
                            line.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        line.sendMessage(receiver,"Lurking has not been set.")

                elif text.lower() == 'เปิดเชค':
                    try:
                        del cctv['point'][msg.to]
                        del cctv['sidermem'][msg.to]
                        del cctv['cyduk'][msg.to]
                    except:
                        pass
                    cctv['point'][msg.to] = msg.id
                    cctv['sidermem'][msg.to] = ""
                    cctv['cyduk'][msg.to]=True 
                    settings["Sider"] = True
                    line.sendMessage(msg.to,"เปิดระบบเช็คคนอ่าน✔️")

                elif text.lower() == 'ปิดเชค':
                    if msg.to in cctv['point']:
                       cctv['cyduk'][msg.to]=False
                       settings["Sider"] = False
                       line.sendMessage(msg.to,"ปิดเชคคนอ่าน❌")
                    else:
                        line.sendMessage(msg.to,"ปิดเชคคนอ่าน❌")

#==============================================================================#
                elif msg.text.lower().startswith("say-af "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'af'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
        
                elif msg.text.lower().startswith("say-sq "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sq'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ar "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ar'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-bn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'bn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ca "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ca'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-cn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-cn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-tw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-tw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-yue "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-yue'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cs "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cs'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-da "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'da'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-nl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'nl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-au "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-au'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-eo "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'eo'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-de "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'de'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-el "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'el'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hu "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hu'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-is "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'is'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-id "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-it "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'it'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ja "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-km "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'km'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ko "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ko'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-la "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'la'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-lv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'lv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-mk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'mk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-no "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'no'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pt "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pt'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-do "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ro'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ru "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ru'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-si "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'si'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ta "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ta'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("พูด "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-tr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'tr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-vi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'vi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
#==============================================================================# 
                elif msg.text.lower().startswith("tr-af "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='af')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sq "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sq')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-am "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='am')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ar "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ar')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-az "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='az')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-eu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='eu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-be "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='be')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ca "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ca')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ceb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ceb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ny "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ny')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-cn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-cn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-tw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-co "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='co')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-da "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='da')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-nl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='nl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-en "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-et "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='et')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ka "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ka')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-de "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-el "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='el')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ht "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ht')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ha "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ha')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-haw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='haw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-iw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='iw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hmn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hmn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-is "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='is')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ig "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ig')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-id "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ga "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ga')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-it "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='it')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ja "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-jw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='jw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-km "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='km')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ko "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ko')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ku "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ku')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ky "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ky')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-la "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='la')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ms "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ms')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ml "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ml')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-my "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='my')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ne "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ne')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-no "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='no')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ps "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ps')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ro "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ro')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ru "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ru')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sm "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sm')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-st "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='st')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-si "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='si')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-so "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='so')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-es "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='es')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-su "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='su')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ta "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ta')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-te "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='te')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ur "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ur')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uz "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uz')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-vi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='vi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-xh "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='xh')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fil "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fil')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-he "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='he')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
#==============================================================================#
                elif "Leave " in msg.text:
                    separate = msg.text.split(" ")
                    number = msg.text.replace(separate[0] + " ","")
                    groups = line.getGroupIdsJoined()
                    group = groups[int(number)]
                    for i in group:
                        ginfo = line.getGroup(i).name
                        if ginfo == group:
                            line.leaveGroup(i)
                            line.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))
                elif "ออก " in msg.text:
                    proses = text.split(" ")
                    ng = text.replace(proses[0] + " ","")
                    gid = line.getGroupIdsJoined()
                    for i in gid:
                        h = line.getGroup(i).name
                        if h == ng:
                            line.leaveGroup(i)
                            line.sendMessage(to,"ออกจากกลุ่ม<<< " +h+ " >>>แล้ว✔️")

#==============================================================================#   
                elif "spamtag @" in msg.text.lower():
                   _name = msg.text.replace("spamtag @","")
                   _nametarget = _name.rstrip(' ')
                   gs = line.getGroup(msg.to)
                   for g in gs.members:
                       if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        line.sendMetion(msg)
                        line.sendMention(msg)
                        line.sendMetion(msg)

                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               line.sendMessage(msg.to, teks)
                        else:
                           line.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            line.sendMessage(msg.to, tulisan)
                        else:
                            line.sendMessage(msg.to, "Out Of Range!")

                elif msg.text.lower().startswith("/ "):
                   txt = text.split(" ")
                   jmlh = int(txt[2])
                   teks = text.replace(" "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   line.sendMessage(msg.to, teks)
                        else:
                               line.sendMessage(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               line.sendMessage(msg.to, tulisan)
                         else:
                               line.sendMessage(msg.to, "Out of range! ")

                elif "nuke" in msg.text.lower():
                  if msg.toType == 2:
#                    print  ("ok")
                    _name = msg.text.replace("nuke","")
                    gs = line.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        line.sendMessage(msg.to,"Not found.")
                    else:
                        for target in targets:
                                line.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])


                elif "invitegroupcall" in msg.text.lower():
                            if msg.toType == 2:
                                sep = text.split(" ")
                                strnum = text.replace(sep[0] + " ","")
                                num = int(strnum)
                                line.sendMessage(to, "Berhasil mengundang kedalam telponan group")
                                for var in range(0,num):
                                    group = line.getGroup(to)
                                    members = [mem.mid for mem in group.members]
                                    line.acquireGroupCallRoute(to)
                                    line.inviteIntoGroupCall(to, contactIds=members)

                elif text.lower().startswith("music2 "):
                            try:
                                search = text.lower().replace("music2 ","")
                                r = requests.get("https://farzain.xyz/api/joox.php?apikey=your_api_key&id={}".format(urllib.parse.quote(search))) #untuk api key bisa requests ke web http://www.farzain.xyz/requests.php
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = " Hasil Musik \n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                hasil += "\n\nLink : \n3. M4A : {}".format(str(audio["m4a"]))
                                line.sendImageWithURL(msg.to, str(data["gambar"]))
                                line.sendMessage(msg.to, "Downloading...")
                                line.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                line.sendVideoWithURL(msg.to, str(audio["m4a"]))
                                line.sendMessage(msg.to, "Success Download...")
                            except Exception as error:
                            	line.sendMessage(msg.to, " Result Error \n" + str(error))


                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    line.sendMessage(msg.to, readTime)                 
                elif "screenshotwebsite" in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        line.sendImageWithURL(to, data["result"])
                elif "checkdate" in msg.text.lower():
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    ret_ = "╔══[ D A T E ]"
                    ret_ += "\n╠ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                    ret_ += "\n╠ Age : {}".format(str(data["data"]["usia"]))
                    ret_ += "\n╠ Birthday : {}".format(str(data["data"]["ultah"]))
                    ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                    ret_ += "\n╚══[ Success ]"
                    line.sendMessage(to, str(ret_))
                elif "instagraminfo" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠ Nama : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠ Username : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠ Akun Pribadi : Tidak"
                            ret_ += "\n╠ Total Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            line.sendImageWithURL(to, str(path))
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "Pengguna tidak ditemukan")
                elif "instagrampost" in msg.text.lower():
                    separate = msg.text.split(" ")
                    user = msg.text.replace(separate[0] + " ","")
                    profile = "https://www.instagram.com/" + user
                    with requests.session() as x:
                        x.headers['user-agent'] = 'Mozilla/5.0'
                        end_cursor = ''
                        for count in range(1, 999):
                            print('PAGE: ', count)
                            r = x.get(profile, params={'max_id': end_cursor})
                        
                            data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                            j    = json.loads(data)
                        
                            for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                                if node['is_video']:
                                    page = 'https://www.instagram.com/p/' + node['code']
                                    r = x.get(page)
                                    url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                    print(url)
                                    line.sendVideoWithURL(msg.to,url)
                                else:
                                    print (node['display_src'])
                                    line.sendImageWithURL(msg.to,node['display_src'])
                            end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)
                elif "หารูป" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "ยูทูป." in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html5lib")
                        ret_ = "╔══[ Youtube Result ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ Total {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                elif "searchmusic" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                ret_ = "╔══[ Music ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[4]))
                                ret_ += "\n╚══[ reading Audio ]"
                                line.sendMessage(to, str(ret_))
                                line.sendAudioWithURL(to, song[3])
                        except:
                            line.sendMessage(to, "Musik tidak ditemukan")
                elif "searchlyric" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                songs = song[5]
                                lyric = songs.replace('ti:','Title - ')
                                lyric = lyric.replace('ar:','Artist - ')
                                lyric = lyric.replace('al:','Album - ')
                                removeString = "[1234567890.:]"
                                for char in removeString:
                                    lyric = lyric.replace(char,'')
                                ret_ = "╔══[ Lyric ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[4]))
                                ret_ += "\n╚══[ Finish ]\n{}".format(str(lyric))
                                line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "Lirik tidak ditemukan")
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))

            elif msg.contentType == 13:
                    if settings["checkContact"] == True:
                        try:
                            contact = line.getContact(msg.contentMetadata["mid"])
                            if line != None:
                                cover = line.getProfileCoverURL(msg.contentMetadata["mid"])
                            else:
                                cover = "Tidak dapat masuk di line channel"
                            path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                            try:
                                line.sendImageWithURL(to, str(path))
                            except:
                                pass
                            ret_ = "╔══[ Details Contact ]"
                            ret_ += "\n╠ Nama : {}".format(str(contact.displayName))
                            ret_ += "\n╠ MID : {}".format(str(msg.contentMetadata["mid"]))
                            ret_ += "\n╠ Bio : {}".format(str(contact.statusMessage))
                            ret_ += "\n╠ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                            ret_ += "\n╠ Gambar Cover : {}".format(str(cover))
                            ret_ += "\n╚══[ Finish ]"
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "ไม่สามารถเช็ครายละเอียดคท.นี้")
            
            elif msg.contentType == 1:
                    if settings["changePicture"] == True:
                        path = line.downloadObjectMsg(msg_id)
                        settings["changePicture"] = False
                        line.updateProfilePicture(path)
                        line.sendMessage(to, "เปลี่ยนรูปโปรไฟล์เรียบร้อยแล้ว")
            elif msg.contentType == 1:
                    if settings["changePicture1"] == True:
                        path = as1.downloadObjectMsg(msg_id)
                        settings["changePicture1"] = False
                        as1.updateProfilePicture(path)
                        as1.sendMessage(to, "เปลี่ยนรูปโปรไฟล์เรียบร้อยแล้ว")
                    if msg.toType == 2:
                        if to in settings["changeGroupPicture"]:
                            path = line.downloadObjectMsg(msg_id)
                            settings["changeGroupPicture"].remove(to)
                            line.updateGroupPicture(to, path)
                            line.sendMessage(to, "Berhasil mengubah foto group")
#===============================================================================[asulMID - as1MID]
        if op.type == 19:
            print ("[ 19 ] KICKOUT asul MESSAGE")
            try:
                if op.param3 in lineMID:
                    if op.param2 in as1MID:
                        G = as1.getGroup(op.param1)
                        ginfo = as1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        as1.updateGroup(G)
                        invsend = 0
                        Ticket = as1.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        as1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = as1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        as1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        as1.updateGroup(G)
                    else:
                        G = as1.getGroup(op.param1)
                        ginfo = as1.getGroup(op.param1)
                        as1.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        as1.updateGroup(G)
                        invsend = 0
                        Ticket = as1.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        as1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = as1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        as1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        as1.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[as1MID lineMID]
                if op.param3 in as1MID:
                    if op.param2 in lineMID:
                        G = line.getGroup(op.param1)
#                        ginfo = line.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        as1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        line.updateGroup(G)
                    else:
                        G = line.getGroup(op.param1)
#                        ginfo = line.getGroup(op.param1)
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        as1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        line.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                        
                elif op.param2 not in Bots:
                    if op.param2 in admin:
                        pass
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        random.choice(KAC).sendText(op.param1,"จุกมั้ยล่ะ")
                        
                else:
                    pass
            except:
                pass
#==============================================================================#
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in admin:
                    pass
                elif settings["inviteprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in admin:
                            pass
                        elif settings["cancelprotect"] == True:
                            settings["blacklist"][op.param2] = True
                            random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])	
#-------------------------------------------------------------------------------
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in admin and Bots:
                    pass
                elif settings["qrprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    G = as1.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    as1.updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    line. sendMessage(op.param1,"")
            else:
                line.sendMessage(op.param1,"")

#==============================================================================#
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    line.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
#                        asulc = [" เรียกทำไม ขี้อยู่"," มีไรรึป่าว ","รู้จักกันหรอมาแทค","แทคเอาโล่ง่ะ","แทคบ่อยๆระวังโดนสอยนะคับ"]
#                        reb_ = line.sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/19/20180619_092344.jpg")
                        lists = []
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                              if settings["detectMention"] == True:
                                 line.sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/19/20180619_092344.jpg")
                                 sendMention(receiver, sender, "","\n")

                    if 'MENTION' in msg.contentMetadata.keys() != None:
                      if settings["Mentionkick"] == True:
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                             if mention ['M'] in Bots:
                                line.mentiontag(msg.to,[msg._from])
                                line.sendMessage(msg.to, "บอกแล้ววววว อย่าแทค...")
                                line.kickoutFromGroup(msg.to, [msg._from])
                                break

        if op.type == 17:
           print ("MEMBER JOIN TO GROUP")
           if settings["Sambutan"] == True:
             if op.param2 in lineMID:
                 return
             ginfo = line.getGroup(op.param1)
             contact = line.getContact(op.param2)
#             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             asulb = [" หวัดดี "," ดีจ้าาา "," โย่ววววว "]
             reb_ = random.choice(asulb)
             
#             line.sendImageWithURL(op.param1,image)
             line.sendMessage(op.param1,reb_ + line.getContact(op.param2).displayName + " กลุ่ม " +  str(ginfo.name) + "ยินดีต้อนรับ")
             line.sendImageWithURL(op.param1,"https://www.img.live/images/2018/06/19/20180619_163340.jpg")

        if op.type == 15:
           print ("MEMBER LEAVE TO GROUP")
           if settings["Sambutan"] == True:
             if op.param2 in lineMID:
                 return
             ginfo = line.getGroup(op.param1)
             contact = line.getContact(op.param2)
             asula = [" โชคดีนะ"," ไปซะละ"," บ๊ายบายยย"," ลาก่อย"," จะรีบไปใหนล่ะ"," กลับมาคุยกันก่อน"]
             rea_ = random.choice(asula)
#             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             
             #line.sendImageWithURL(op.param1,image)
             line.sendMessage(op.param1,line.getContact(op.param2).displayName + rea_)
             line.sendImageWithURL(op.param1,"https://www.img.live/images/2018/06/19/20180619_163340.jpg")
             
#==============================================================================#
        if op.type == 26:
            msg = op.message
            if settings["Api"] == True:
                if msg.text in ["คท","Me","me"]:
                            com1 = ["เชคจัง กลัวเค้าไม่รู้ว่ามีเชลง่ะ","คท.ใครล่ะ","เอาคท.ไปรันง่ะ"]
                            com1_ = random.choice(com1)
                            line.sendMessage(msg.to,com1_)
                elif msg.text in ["Help","help","คำสั่ง"]:
                              com2 = ["หัดจำคำสั่งเองมั่ง Helpอยู่ได้","จำคำสั่งไม่ได้ง่ะ"]
                              com2_ = random.choice(com2)
                              line.sendMessage(msg.to,com2_)
                
                elif msg.text in ["บอท"]:
                              line.sendMessage(msg.to,"กือไม่ใช่บอท")
                elif "555" in msg.text.lower():
                              com4 = ["ขำไรกันหว่า","ขำไรยะ","555ขำด้วย","ขำขนาดนี้ อาการหนักนะเรา","5555 ขำด้วย","ขมิบดีๆนะ ขำขนาดนี้ระวังขี้แตก","ขำจนขี้แตกละมั้ง บ้าไปแล้ว!"]
                              com4_ = random.choice(com4)
                              line.sendMessage(msg.to,com4_)
                elif msg.text in ["ดีค่ะ","หวัดดีค่ะ","ดีจ้า"]:
                              com5 = ["ดีคับ คนสวย","ดีจ้ะ ชื่อไรคับ","หวัดดีจ้าาา"]
                              com5_ = random.choice(com5)
                              line.sendMessage(msg.to,com5_)
                elif msg.text in ["ดีคับ","หวัดดีคับ","ดีครับ","หวัดดีครับ"]:
                              com6 = ["หวัดดี ไอ่ทิด","หวัดดีบักหำ","ไหว้พระเถอะลูก"]
                              com6_ = random.choice(com6)
                              line.sendMessage(msg.to,com6_)
                elif "มอนิ่ง" in msg.text.lower():
                              com7 = ["มอร์นิ่ง ฝันดีนะ555","เช้าละหรอ","มอนิ่งๆ","กี่โมงละเนี่ย เช้าละหรอ"]
                              com7_ = random.choice(com7)
                              line.sendMessage(msg.to,com7_)
                elif "มอๆ" in msg.text.lower():
                              com17 = ["มอร์นิ่ง ฝันดีนะ555","เช้าละหรอ","มอนิ่งๆ","กี่โมงละเนี่ย เช้าละหรอ"]
                              com17_ = random.choice(com17)
                              line.sendMessage(msg.to,com17_)
                elif msg.text in ["น่าน"]:
                              com8 = ["น่านไกล ไม่ไปหรอก","ไปทำไมน่าน","น่าน เป็นจังหวัดทางภาคเหนือ555"]
                              com8_ = random.choice(com8)
                              line.sendMessage(msg.to,com8_)
                elif msg.text in ["กำ","กำหำ"]:
                              com9 = ["กำหำใคร","หื่นจังจะกำแต่หำ","กำหำแล้วรูดๆๆ55"]
                              com9_ = random.choice(com9)
                              line.sendMessage(msg.to,com9_)
                elif msg.text in [".อยู่ไหม","อยู่ไหม"]:
                              com10 = ["แป๊บ ขี้อยู่","อยู่วี่5555","ไม่อยู่มั้ง","อยู่ป่าวหว่า"]
                              com10_ = random.choice(com10)
                              line.sendMessage(msg.to,com10_)
                elif msg.text in ["ไปใหน","ไปไหน"]:
                              com11 = ["ไปใหนก็ได้ โตแล้ว","จะไปด้วยง่ะ","ไปเรื่อยๆ","ไปให้แมวถาม555"]
                              com11_ = random.choice(com11)
                              line.sendMessage(msg.to,com11_)
                elif msg.text in ["คับ"]:
                              com12 = ["แน่ใจหรอว่าคับ หำนิดเดียว55","ไม่คับหรอกมั้ง อิอิ"]
                              com12_ = random.choice(com12)
                              line.sendMessage(msg.to,com12_)
                elif msg.text in ["ค่ะ","คะ","จ้ะ"]:
                              com13 = ["พูดเพราะจัง จีบได้มะ","พูดเพราะจัง มาเป็นเมียเราเถอะ"]
                              com13_ = random.choice(com13)
                              line.sendMessage(msg.to,com13_)
                elif "บิน" in msg.text.lower():
                              com14 = ["บินดิ จะตีให้ปีกหัก","บินขึ้นง่ะ หนักพุง555","บินทมายยยย","ระวังปีกหักนะ"]
                              com14_ = random.choice(com14)
                              line.sendMessage(msg.to,com14_)
                elif "หือ" in msg.text.lower():
                              com15 = ["หือกับพี่ระวังโดนปี้นะ","หืออะไร ใหนใครกล้าหือ","อย่าหือ เดะกะบาลลั่น"]
                              com15_ = random.choice(com15)
                              line.sendMessage(msg.to,com15_)
                elif msg.text in ["ห๊ะ"]:
                              line.sendMessage(msg.to,"ห๊ะอะไร หัดตั้งใจฟังดิ")
                elif "เหนื่อย" in msg.text.lower():
                              line.sendMessage(msg.to,"หากเหนื่อยนัก ขอจงหยุดพักซะก่อน.....")
                elif "ร้อน" in msg.text.lower():
                              line.sendMessage(msg.to,"ร้อนก็ไปอาบน้ำ เดะพี่ถูหลังให้ หุหุ")
                elif msg.text in ["Sp","Speed","speed"]:
                              line.sendMessage(msg.to,"กำลังเช็คความเร็ว....")
                              line.sendMessage(msg.to,"0.024965118408203")
                elif msg.text in ["หำ"]:
                              line.sendMessage(msg.to,"ก็หำอ่ะดิ นึกว่าสากกะเบือง่ะ")
                elif msg.text in ["แอด","@"]:
                              line.sendMessage(msg.to,"เลดี้แอ่นเยสตะแม่ง ขอเชิญพบกับแอดมิน ณ บัดนี้")
                              time.sleep(0.1)
                              line.sendMessage(msg.to,"Siriv10:groupcreator")
                              time.sleep(0.1)
                              line.sendMessage(msg.to,"นี่ไงแอดมิน🔝")
                elif msg.text in ["รอง","รองแอด","@@"]:
                              line.sendMessage(msg.to,"กำลังเช็ครองแอดมิน...")
                              line.sendMessage(msg.to,"Siriv10:予備作成者")
                elif "ควย" in msg.text.lower():
                              com16 = ["เงี่ยนง่ะ เรียหาควย","หือออ ควยใคร"]
                              com16_ = random.choice(com16)
                              line.sendMessage(msg.to,com16_)
                

#==============================================================================#
        if op.type == 26:
            msg = op.message
            if msg.text in ["คนใหนปากห้อย","ใครห้อย","ใครปากห้อย"]:
               line. sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/19/1529403824690.jpg")
#               line.sendContact(to,"u09d6e6f52a7c6d6f711db71a20a4a5eb")
               line.sendMessage(msg.to,"เดินสะดุดปากตัวเองล้ม คือคนนี้เลย☝️")
            elif "ตุน" in msg.text.lower():
                         line.sendMessage(msg.to,"ตุนอะไร ชื่อตูน ตูน เดะกัดใส้แตก")
                         line.sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/18/20180618_225618.jpg")
            elif msg.text in ["ตูน","ตาตูน","พี่ตูน","เจ้ตุ๊ด","เจ๊ตุ๊ด"]:
                          com3 = ["เรียกทำไม","คิดถึงง่ะ รอก่อนนะ ไม่ว่าง","ตูนใหน?"]
                          com3_ = random.choice(com3)
                          line.sendMessage(msg.to,com3_)
                          line.sendImageWithURL(msg.to,"https://www.img.live/images/2018/06/18/20180618_225618.jpg")
             
#==============================================================================#
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if cctv['cyduk'][op.param1]==True:
                    if op.param1 in cctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in cctv['sidermem'][op.param1]:
                            pass
                        else:
                            cctv['sidermem'][op.param1] += "\nâ¢ " + Name
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    mentionMembers(op.param1,[op.param2])
                                else:
                                    mentionMembers(op.param1,[op.param2])
                            else:
                                mentionMembers(op.param1,[op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass


        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)





