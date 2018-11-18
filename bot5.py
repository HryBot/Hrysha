import tamtam
import json
import re
import jiraa
import MySQLdb
import random


Host="https://hrybottest777.atlassian.net"
Login="igosheva_olesya@mail.ru"
Pas="Theneighbourhood1204"
mem_Naz={}
mem_Desc={}
mem_Ass={}
mem_Prior={}
mem_KLZad={}
mem_Status={}
dictAdding = {}
dictChanging = {}
xx = 0
xxx = 0
token = 'hJyWCYn2kX6MeM6ieE5MTw3M4Jj2RuLmPJ6jdben1OQ'
path = "./Utils/savedMessages.json"

def Nazv_Proect():
    Ot=[]
    Ot.append('Кака назвать проект?')
    Ot.append('Как ты хочешь назвать проект?')
    Ot.append('Назови проект!')
    Ot.append('А больше ничего не хочешь? Ну ладно. Назови его')
    Ot.append('Nazovi proekt')
    i=random.randint(0,len(Ot)-1)
    return Ot[i]

def Desc_Proect():
    Ot=[]
    Ot.append('Опиши свой проект')
    Ot.append('Расскажи мне о своем проекте 🙂')
    Ot.append('И шо будет в твоем проекте? Давай поподробнее')
    Ot.append('О чем твой проект?')
    Ot.append('Расскажи в двух словах, что за задача')
    i=random.randint(0,len(Ot)-1)
    return Ot[i]

def Ispol():
    Ot=[]
    Ot.append('Кто будет заниматься этой задачей')
    Ot.append('Кто будет решать эту задачу')
    Ot.append('Выбери исполнителя этой чудесной задачи')
    Ot.append('Выбери исполнителя этого поручения')
    i=random.randint(0,len(Ot)-1)
    return Ot[i]+". Назови его логин"

def Priorit():
    Ot=[]
    Ot.append('Какой приоритет у задачи')
    Ot.append('Скажи приоритет твоей задачи')
    Ot.append('Насколько быстро надо сделать поручение')
    i=random.randint(0,len(Ot)-1)
    return Ot[i]

def IssueID():
    Ot=[]
    Ot.append('Какой ID у задачи')
    Ot.append('Скажи какой ID у твоей задачи')
    i=random.randint(0,len(Ot)-1)
    return Ot[i]

def StatusIssue():
    Ot=[]
    Ot.append('Какой статус у задачи')
    Ot.append('Скажи какой статус у твоей задачи')
    i=random.randint(0,len(Ot)-1)
    return Ot[i]

def SQLL():
      conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="bot")
      sql = "SELECT * FROM User"
      cur = conn.cursor(MySQLdb.cursors.DictCursor)
      cur.execute(sql)
      data = cur.fetchall()
      print(data)
      conn.commit()
      cur.close()
def AuthCheck(TamTam):
      conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="bot123")
      sql = "SELECT * FROM Users WHERE  TamTamID="+str(TamTam)
      cur = conn.cursor(MySQLdb.cursors.DictCursor)
      cur.execute(sql)
      data = cur.fetchall()
      cur.close()
      if cur.rownumber>0:
          return 1
      else:
          return 0

def BDLogin(TamTam, Login, Password):
      conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="bot123")
      sql = "SELECT * FROM Users WHERE JiraLogin='"+str(Login)+"' AND JiraPassword='"+str(Password)+"'"
      print(sql)
      cur = conn.cursor(MySQLdb.cursors.DictCursor)
      cur.execute(sql)
      data = cur.fetchall()
      cur.close()
      if cur.rownumber>0:
          sql1 = "update users set TamTamID='"+str(TamTam)+"' where UserID='" + str(data[0]['UserID'])+"'"
          cur1 = conn.cursor(MySQLdb.cursors.DictCursor)
          cur1.execute(sql1)
          conn.commit()
          cur1.close()
          return 1
      else:
          return 0
def tokk(token):
    tamtammain = tamtam.TamTam(token)
    return tamtammain

def changeStatus(SENDER_ID, TEXT_FROM_MESS1, step):
    if step == "0":
        dictChanging.update({str(SENDER_ID): []})
        dictChanging[str(SENDER_ID)].append(TEXT_FROM_MESS1)
        tokk(token).send_pers((str(SENDER_ID)), StatusIssue())
        """Status"""
    with open("./Utils/queue.json", 'r') as function:
        if step == "1":
            dictChanging[str(SENDER_ID)].append(TEXT_FROM_MESS1)
            jiraa.Make_Done(Host, Login, Pas, dictChanging[str(SENDER_ID)][0], dictChanging[str(SENDER_ID)][1])
            dictChanging.pop(str(SENDER_ID), None)
            funcFile = json.loads(function.read())
            funcFile.pop(str(SENDER_ID), None)
            open("./Utils/queue.json", 'w').write(json.dumps(funcFile))
            tokk(token).send_pers((str(SENDER_ID)), "Статус изменен")
        else:
            funcFile = json.loads(function.read())
            step = str(int(step) + 1)
            funcFile[str(SENDER_ID)] = "changeStatus" + step
            open("./Utils/queue.json", 'w').write(json.dumps(funcFile))
    return

def Delitee(SENDER_ID, TEXT_FROM_MESS1, step):
    if step == "0":
        dictChanging.update({str(SENDER_ID): []})
        dictChanging[str(SENDER_ID)].append(TEXT_FROM_MESS1)
        tokk(token).send_pers((str(SENDER_ID)), StatusIssue())
        """Status"""
    with open("./Utils/queue.json", 'r') as function:
        if step == "1":
            dictChanging[str(SENDER_ID)].append(TEXT_FROM_MESS1)
            jiraa.Issue_Del(Host, Login, Pas, dictChanging[str(SENDER_ID)][0], dictChanging[str(SENDER_ID)][1])
            dictChanging.pop(str(SENDER_ID), None)
            funcFile = json.loads(function.read())
            funcFile.pop(str(SENDER_ID), None)
            open("./Utils/queue.json", 'w').write(json.dumps(funcFile))
            tokk(token).send_pers((str(SENDER_ID)), "Удалено")
        else:
            funcFile = json.loads(function.read())
            step = str(int(step) + 1)
            funcFile[str(SENDER_ID)] = "Delitee" + step
            open("./Utils/queue.json", 'w').write(json.dumps(funcFile))
    return

def adding(SENDER_ID, TEXT_FROM_MESS1, step):
    if step == "0":
        dictAdding.update({str(SENDER_ID): []})
        print(dictAdding)
        dictAdding[str(SENDER_ID)].append(TEXT_FROM_MESS1)
        tokk(token).send_pers((str(SENDER_ID)), Desc_Proect())
        """Desc"""
    elif step == "1":
        dictAdding[str(SENDER_ID)].append(TEXT_FROM_MESS1)
        tokk(token).send_pers((str(SENDER_ID)), Ispol())
        # код, который добавляет куда-то работника
        """AssName"""
    elif step == "2":
        dictAdding[str(SENDER_ID)].append(TEXT_FROM_MESS1)
        tokk(token).send_pers((str(SENDER_ID)), Priorit())
        # код, который добавляет куда-то приоритет
        """Prior"""
    with open("./Utils/queue.json", 'r') as function:
        if step == "3":
            dictAdding[str(SENDER_ID)].append(TEXT_FROM_MESS1)
            jiraa.Make_Issue(Host,Login,Pas,dictAdding[str(SENDER_ID)][2], dictAdding[str(SENDER_ID)][0], dictAdding[str(SENDER_ID)][1], dictAdding[str(SENDER_ID)][3])
            dictAdding.pop(str(SENDER_ID), None)
            funcFile = json.loads(function.read())
            funcFile.pop(str(SENDER_ID), None)
            open("./Utils/queue.json", 'w').write(json.dumps(funcFile))

            tokk(token).send_pers((str(SENDER_ID)), "Добавлено")
        else:
            funcFile = json.loads(function.read())
            step = str(int(step) + 1)
            funcFile[str(SENDER_ID)] = "adding" + step
            open("./Utils/queue.json", 'w').write(json.dumps(funcFile))
    return

botID = tokk(token).get_me()['user_id']
def main(xx):
    while True:
        GET_CHATS_ALL = tokk(token).get_chats(1)
        LAST_CHAT_ID = GET_CHATS_ALL[0][0]['chat_id']
        LAST_TIME_EVENT = GET_CHATS_ALL[1]
        LAST_SENDER_ID = tokk(token).get_messages(LAST_CHAT_ID)[0]['sender']['user_id']
        xxx = LAST_SENDER_ID

        if LAST_TIME_EVENT != xx and xxx != botID:
            TEXT_FROM_MESS1 = tokk(token).get_messages(LAST_CHAT_ID)[0]['message']['text']
            SENDER_ID = tokk(token).get_messages(LAST_CHAT_ID)[0]['sender']['user_id']
            CHAT_ID = tokk(token).get_chat(LAST_CHAT_ID)['chat_id']

            with open("./Utils/queue.json",'r') as function:
                funcFile = json.loads(function.read())
                isExist = False
                for users in funcFile:
                    if str(SENDER_ID) == str(users):
                        if re.search("\D*", funcFile[str(SENDER_ID)]).group(0) == "adding":
                            print(re.search("\d+",funcFile[str(SENDER_ID)]).group(0))
                            adding(SENDER_ID, TEXT_FROM_MESS1, re.search("\d+",funcFile[str(SENDER_ID)]).group(0))
                        elif re.search("\D*", funcFile[str(SENDER_ID)]).group(0) == "changeStatus":
                            print(re.search("\d+", funcFile[str(SENDER_ID)]).group(0))
                            changeStatus(SENDER_ID, TEXT_FROM_MESS1, re.search("\d+", funcFile[str(SENDER_ID)]).group(0))

            splitedText = re.split(" ", TEXT_FROM_MESS1)
            splitedTextlogin = re.split(", ", TEXT_FROM_MESS1)

            if AuthCheck(SENDER_ID)==1:

                if (TEXT_FROM_MESS1 == "Добавить"):
                    funcFile.update({SENDER_ID:"adding0"})
                    open("./Utils/queue.json", 'w').write(json.dumps(funcFile))
                    tokk(token).send_pers((str(SENDER_ID)), Nazv_Proect())
                elif (TEXT_FROM_MESS1 == "Изменить статус"):
                    funcFile.update({SENDER_ID: "changeStatus0"})
                    open("./Utils/queue.json", 'w').write(json.dumps(funcFile))
                    tokk(token).send_pers((str(SENDER_ID)), IssueID())

                elif (TEXT_FROM_MESS1 == "Удалить"):
                    funcFile.update({SENDER_ID: "Delitee0"})
                    open("./Utils/queue.json", 'w').write(json.dumps(funcFile))
                    tokk(token).send_pers((str(SENDER_ID)), IssueID())
                elif (TEXT_FROM_MESS1 == "Редактировать приоритет"):
                    funcFile.update({SENDER_ID: "adding2"})
                    open("./Utils/queue.json", 'w').write(json.dumps(funcFile))
                    tokk(token).send_pers((str(SENDER_ID)), 'Вы завершили что-то там')
                elif (TEXT_FROM_MESS1 == "список"):
                    funcFile.update({SENDER_ID: "adding4"})
                    open("./Utils/queue.json", 'w').write(json.dumps(funcFile))
                    tokk(token).send_pers((str(SENDER_ID)), 'Вы завершили что-то там')
                elif (TEXT_FROM_MESS1 == "статус задания"):
                    funcFile.update({SENDER_ID: "adding3"})
                    open("./Utils/queue.json", 'w').write(json.dumps(funcFile))
                    tokk(token).send_pers((str(SENDER_ID)), 'Вы завершили что-то там')
                elif (TEXT_FROM_MESS1 == "5 последних заданий"):
                    funcFile.update({SENDER_ID: "adding4"})
                    open("./Utils/queue.json", 'w').write(json.dumps(funcFile))
                    tokk(token).send_pers((str(SENDER_ID)), 'Вы завершили что-то там')
                elif (TEXT_FROM_MESS1 == "Команду" or TEXT_FROM_MESS1 == "команду"):
                    tokk(token).send_pers((str(SENDER_ID)), "Что вы хотите сделать?")
                elif (splitedText[0] == "Сохрани" and splitedText[1] == 'идею'):
                    with open(path, 'r') as f:
                        data = json.loads(f.read())
                        isExist = False

                        for chats in data['data']['chat_id']:
                            if str(CHAT_ID) in chats:
                                isExist = True
                        if (isExist):
                            for chats in data['data']['chat_id']:
                                if str(CHAT_ID) in chats:
                                    for senders in data['data']['chat_id'][chats]["sender_id"]:
                                        if str(SENDER_ID) in senders:
                                            data['data']['chat_id'][str(CHAT_ID)]["sender_id"][str(SENDER_ID)]["messages"].append(TEXT_FROM_MESS1[13:])
                                            open(path, 'w').write(json.dumps(data))
                                            tokk(token).send_pers((str(SENDER_ID)), "Идея добавлена")
                                        else:
                                            data['data']['chat_id'][str(CHAT_ID)]["sender_id"].update({str(SENDER_ID): {"messages": []}})
                                            data['data']['chat_id'][str(CHAT_ID)]["sender_id"][str(SENDER_ID)]["messages"].append(TEXT_FROM_MESS1[13:])
                                            open(path, 'w').write(json.dumps(data))
                                            tokk(token).send_pers((str(SENDER_ID)), "Идея добавлена")
                        else:
                            data['data']['chat_id'].update({str(CHAT_ID): {"sender_id": {str(SENDER_ID): {"messages": []}}}})
                            data['data']['chat_id'][str(CHAT_ID)]["sender_id"][str(SENDER_ID)]["messages"].append(TEXT_FROM_MESS1[13:])
                            open(path, 'w').write(json.dumps(data))
                            tokk(token).send_pers((str(SENDER_ID)), "Идея добавлена")

                elif (TEXT_FROM_MESS1 == "Мои идеи"):
                    with open(path, 'r') as f:
                        data = json.loads(f.read())
                        isExist = False
                        for chats in data['data']['chat_id']:
                            if str(CHAT_ID) == chats:
                                for senders in data['data']['chat_id'][chats]["sender_id"]:
                                    if str(SENDER_ID) == senders:
                                        for messages in data['data']['chat_id'][chats]["sender_id"][senders]["messages"]:
                                            tokk(token).send_pers((str(SENDER_ID)), messages)
                                            isExist = True
                        if isExist == False:
                            tokk(token).send_pers((str(SENDER_ID)), "Нет сообщений")
            elif len(splitedTextlogin)==2:
                Logi=BDLogin(SENDER_ID,splitedTextlogin[0],splitedTextlogin[1])
                if Logi==1:
                         tokk(token).send_pers((str(SENDER_ID)), 'Вы успешно вошли')
                else:
                         tokk(token).send_pers((str(SENDER_ID)), 'Неверный логин или пароль')
            else:
                     tokk(token).send_pers((str(SENDER_ID)), 'Вы не авторизованный пользователь, напишите Логин и пароль через запятую')

if __name__ == '__main__':
    main(xx)
