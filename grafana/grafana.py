# encoding: utf-8
import requests

from operator import itemgetter








####################################
####################################



def grafana():
		
	payload_data = {
	  "from": "1590940800000",
	  "to": "1593532799999",
	  "queries": [{
	    "refId": "A",
	    "intervalMs": 7200000,
	    "maxDataPoints": 400,
	    "datasourceId": 41,
	    "rawSql": "select\r\ns.users AS \"Сотрудник\",\r\ncount(case WHEN date_part('month',s.timecreated)= date_part('month',current_timestamp - interval '15 DAY') THEN s.action_id ELSE NULL end)::integer AS \"Текущий месяц\"\r\nfrom\r\n(SELECT\r\nchangegroup.id AS action_id, \r\nchangegroup.issueid AS request, \r\njiraissue.issuenum AS requestNum, \r\napp_user.lower_user_name AS users, \r\nchangegroup.created AS timecreated, \r\nchangeitem.OLDSTRING AS old, \r\nchangeitem.NEWSTRING AS new\r\nFROM changegroup, changeitem, jiraissue, app_user\r\nWHERE changegroup.id = changeitem.groupid\r\nAND jiraissue.id = changegroup.issueid\r\nand changegroup.author = app_user.user_key\r\nAND app_user.lower_user_name IN(\r\n'a.elinek',\r\n'ya.prilukov',\r\n'i.samochornov',\r\n'l.zhaleeva',\r\n'a.nurgaliev',\r\n'v.bocharov',\r\n'e.firyulina',\r\n'v.kumanovsky',\r\n'a.silin',\r\n'a.ochirov',\r\n'n.zonberg',\r\n'e.kalistratov',\r\n'chernova.i',\r\n's.avdeev',\r\n'd.chikanov',\r\n'vl.kardyukov',\r\n'e.kirillova',\r\n'ar.nurgaliev',\r\n'a.kinshin',\r\n'm.shirling',\r\n'fomenko.s'\r\n)\r\nAND (\r\nchangeitem.NEWSTRING = 'Решено'\r\nAND changeitem.OLDSTRING IS NOT NULL\r\nor changeitem.NEWSTRING = 'Отдана в разработку'\r\nor changeitem.NEWSTRING = 'отдана на согласование'\r\nor changeitem.NEWSTRING = 'Назначена в работу 2 линии'\r\n)\r\nAND changegroup.created BETWEEN current_timestamp::date - interval '31 DAY' AND (current_timestamp + interval '1 DAY')::date)s\r\ngroup by s.users;",
	    "format": "table"
	  }]
	}
	url = 'https://grafana.cdek.ru/api/tsdb/query'
	headers = {
		}
	r = requests.post(url, json=payload_data, headers=headers, timeout = 10)
	table = r.json()
	
	# print(table)
	results = sorted(table['results']['A']['tables'][0]['rows'], key=itemgetter(1), reverse=True) 
	i = 1
	for user in results:

		print(i, user[0], user[1])
		i +=1
		
	return r.json()
	
	

grafana()
