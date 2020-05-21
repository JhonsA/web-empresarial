from .models import Link

# Procesador de contexto, para extender el contexto y poder utilizar esta funcion donde se requiera
# Se inscribe en setting.py, TEMPLATES, context_procesors
def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx