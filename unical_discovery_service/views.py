from django.shortcuts import render

from . models import Entity


def unical_spid_ds(request):
    """
    an example of working DS call
    /role/idp.ds?entityID=https%3A%2F%2Fsatosa.testunical.it%2FSaml2%2Fmetadata&return=https%3A%2F%2Fsatosa.testunical.it%2FSaml2%2Fdisco
    """
    template = "unical_ds_index.html"

    caller_entityid = request.GET.get('entityID')
    caller_disco = request.GET.get('return')

    d = {'caller_entityid': caller_entityid,
         'caller_disco': caller_disco,
         'unical_id': Entity.objects.get(name='unicalid'),
         'spid_entities': Entity.objects.filter(type__name="SPID",
                                                is_active=True)
         }

    # print(d.items())
    return render(request, template, context=d)
