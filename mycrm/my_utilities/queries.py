from mycrm.models import *
from textwrap import wrap

def get_companies_report_text():
    companies = Company.objects.all()
    lines = []
    lines.append('~~~~~~~~~~~~~~~~~~~~~~SUMMARY~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    for company in companies:
        lines.append('------------------------------------')
        lines.append('Company: {}'.format(company))
        lines.append('contacts:')
        for client in company.businesscard_set.all():
            lines.append('      * {}      {}      tel:{}'.format(client, client.last_name, client.phone))
        lines.append('Company details:')
        for order in company.order_set.all():
            lines.append('      *{}      Value:{} Euro'.format(order, order.value))
        lines.append('------------------------------------')
        lines.append('')

    return lines

