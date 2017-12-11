'''

Queries examples
only for testing purposes

python manage.py shell < _tutorial_queries.py

'''



def get_companies_report_text():
    from mycrm import models
    companies = models.Company.objects.all()
    text = ''

    for company in companies:
        text += '------------------------------------\n'
        text += ('Company: {}\n'.format(company))
        text += 'contacts:\n'
        for client in company.businesscard_set.all():
            text += ('\t* {}\t{}\ttel:{}\n'.format(client, client.last_name, client.phone))
        text += 'Company details:\n'
        for order in company.order_set.all():
            text += ('\t*{}\tValue:{} Euro\n'.format(order, order.value))
        text += '------------------------------------\n\n'

    return text


def sorting_queries1():
    from mycrm import models
    from django.db.models.functions import Coalesce

    firmaA = models.Company.objects.get(pk=1)

    print('____________________order__________________________')
    #all comments related with company 1
    commentsA = firmaA.comment_set.all()
    # commentsA = firmaA.comment_set.filter(title='This is and example')
    # commentsA.order_by('date')
    ordered = commentsA.order_by(Coalesce('date', 'pk').desc())
    for comment in ordered:
        print(comment.title, '\t', comment.date)

    print('______________________________________________')


def count_elements():
    from mycrm import models
    print('______________________________________________')
    firmaA = models.Company.objects.get(pk=2)
    com = firmaA.comment_set.count()
    print(com)
    print('______________________________________________')

# sorting_queries1()
count_elements()
