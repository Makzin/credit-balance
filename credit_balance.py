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
    dict_test = {}
    path = os.path.expanduser('~/Desktop/'+url+'_credit_report/')

    ensure_dir(path)

    #loop through each client
    for client in all_clients:
        dict_test[client.organization]=client.credit

    #print dict_test


    with open(ensure_file(url + '_credit_report.csv'),'wb') as f:
        w = csv.writer(f)
        w.writerow(["Disclaimer - this will only print off credits in the base currency of the account!"])
        w.writerow(["ORGANIZATION", "BALANCE"])        
        w.writerows(dict_test.items())

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

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
    os.chdir(d)

def ensure_file(f):
    tag = 1
    while os.path.isfile(f):
      f = "%s_credit_report #%s.csv" % (url, str(tag))
      tag = tag + 1
    return f


main_program()

