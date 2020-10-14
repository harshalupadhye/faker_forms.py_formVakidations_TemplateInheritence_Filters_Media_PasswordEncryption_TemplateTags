from django import template
register=template.Library()

def cut(value,args):
    """
    this is to cut args from value 
    """
    return value.replace(args,' ')
    register.filter('cut',cut)