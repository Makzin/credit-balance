import os
import csv
from refreshbooks import api

url = 'jitterbeast.freshbooks.com'
token = 'cf103a226b294dea127de9ceb4fc7394'


def main_program():
    api_caller = api.TokenClient(url, token)
    # get all the clients from our account
    all_clients = list_all(api_caller.client.list, 'client')
    dict_test = {}
        
    #loop through each client and add them and their balance to the dictionary    
    for client in all_clients:
    	dict_test[client.organization]=client.credit
    
    print dict_test

    #fieldnames = {'Organization': 'Balance'}
    #with open('credit_balance.csv', 'wb') as f: 
    #    writer = csv.DictWriter(f, delimiter=':', fieldnames=fieldnames)
    #    writer.writerows(dict_test)
    #    for row in dict_test: 
    #            writer.writerow(row)

    #test_file = open('test2.csv','w')
    #csvwriter = csv.DictWriter(test_file, delimiter=':', fieldnames=fieldnames)
    #csvwriter.writerow(dict((fn, fn) for fn in fieldnames))
    #for row in dict_test: 
     #   csvwriter.writerow(row)
    #test_file.close()
    

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