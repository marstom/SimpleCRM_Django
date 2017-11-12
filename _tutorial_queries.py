from mycrm.models import *

def get_companies_report_text():
    companies = Company.objects.all()
    text = ''

    for company in companies:
        text+='------------------------------------\n'
        text+=('Company: {}\n'.format(company))
        text+='contacts:\n'
        for client in company.businesscard_set.all():
            text += ('\t* {}\t{}\ttel:{}\n'.format(client, client.last_name, client.phone))
        text+='Company details:\n'
        for order in company.order_set.all():
            text += ('\t*{}\tValue:{} Euro\n'.format(order, order.value))
        text += '------------------------------------\n\n'

    return text

