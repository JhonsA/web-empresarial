from django import template
from pages.models import Page

register = template.Library()

# Agreagamos un decorador que implementa la funcionalidad
# Tranformamos lo que es una funcion normal en una tag simple (register.simple_tag) y lo registramos en la libreria de
# templates (register = templrate.Library())
@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages