import os
import csv
from refreshbooks import api

url = ''
token = ''


def main_program():
    api_caller = api.TokenClient(url, token)
    # get all the clients from our account
    all_clients = list_all(api_caller.client.list, 'client')
    client_name_list = []
    credit_list = []
    dict_test = {"Organization": "Balance"}
    
    #loop through each client
    for client in all_clients: 
	   client_credit = client.credit
	   credit_list.append(client_credit)
	   client_name = client.organization
	   client_name_list.append(client_name)
    
    #print client_name_list
    #print credit_list
    
    for client in all_clients:
    	client_name = client.organization
    	client_credit = client.credit
    	dict_test[client_name]=client_credit
    
    print dict_test
    
    #writer= csv.writer(open('dict.csv', 'wb'))
    #for key, value in dict_test(): 
    #	writer.writerow([key, value])

def list_all(command, entity):
    page = 1
    per_page = 100
    last_page = False

    while last_page is False:
        try:
            response = command(page=str(page), per_page=str(per_page))
            entities = getattr(response, pluralize(entity))
            for item in getattr(entities, entity):
                yield item
            last_page = entities.attrib['page'] == entities.attrib['pages']
        finally:
            page += 1


def pluralize(entity):
    return entity + 's'


main_program()
