from jira import JIRA
import json
Host="https://hrybottest777.atlassian.net"
Login="igosheva_olesya@mail.ru"
Pas="Theneighbourhood1204"
AssName=""
Nazv="Название задачи"
Desc="Описание"
Prior='High/Medium/Low'
Status="In Progres/Done"
IssueID="HRY-6"

def Make_Issue(Host, Login, Password, AssName, Nazv, Descr, Prior,NomProec):
    auth_jira = JIRA(Host, basic_auth=(Login,Password))
    projects = auth_jira.projects()
    new_issue = auth_jira.create_issue(assignee={'name': AssName}, project=projects[NomProec], summary=Nazv, description=Descr, issuetype={'id': '10002'})

def Make_Done(Host, Login, Password, IssueID, Status):
    auth_jira = JIRA(Host, basic_auth=(Login,Password))
    isq=auth_jira.issue(IssueID)
    auth_jira.transition_issue(isq, transition=Status)

def Up_Prior(Host, Login, Password, Prior, IssueID):
    auth_jira = JIRA(Host, basic_auth=(Login,Password))
    isq=auth_jira.issue(IssueID)
    isq.update(priority={"name" : Prior})

def List_Issue(Host, Login, Password):
    auth_jira = JIRA(Host, basic_auth=(Login,Pas))
    Colect=auth_jira.search_issues('')
    print(Colect[0])
    Zad=[]
    Zad.append(Colect[0])
    Zad.append(auth_jira.issue(Colect[0]).fields.summary)
    Zad.append(auth_jira.issue(Colect[0]).fields.description)
    Zad.append(auth_jira.issue(Colect[0]).fields.priority)
    Zad.append(auth_jira.issue(Colect[0]).fields.assignee)
    Zad.append(auth_jira.issue(Colect[0]).fields.status)
    return Zad
def Issue_Status(Host, Login, Password, IssueID):
    auth_jira = JIRA(Host, basic_auth=(Login,Pas))
    return auth_jira.issue(IssueID).fields.status
