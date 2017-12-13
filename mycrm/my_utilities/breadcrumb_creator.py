'''
Class using for create generic breadcrumbs
'''

class BreadcrumbCreator:

    def __init__(self):
        self.pages_list=[]

    def append_page(self, name, url):
        page = self._breadcrumb_creator(name, url)
        self.pages_list.append(page)

    def append_active_page(self, name):
        active_page = '<li class="breadcrumb-item active">{name}</li>'.format(name=name)
        self.pages_list.append(active_page)


    def get_pages(self):
        return ''.join(self.pages_list)

    def _breadcrumb_creator(self, name, url):
        link = '<li class="breadcrumb-item"><a href="{url}">{name}</a></li>'.format(name=name, url=url)
        result = link
        return result

if __name__ == '__main__':
    bc = BreadcrumbCreator()
    bc.append_page('asdf', 'goog')
    bc.append_page('qwer', 'goog')
    bc.append_page('2345', 'goog')
    bc.append_active_page('thisislastpage')
    print(bc.get_pages())