from upload.models import Document
from onlineclass.models import Helper, ImageCapture
from django.http import HttpResponse
from django.template import loader


def execute_commentor(request, doc_id):
    template = loader.get_template('onlineclass/commentor.html')

    doc = Document.objects.get(id=doc_id)
    helper = Helper.objects.get(doc_id=doc_id)
    imgfile = ImageCapture.objects.get(helper_id=helper.helper_id)

    context = {
        "doc": doc,
        "helper": helper,
        "imgfile": imgfile
    }
    return HttpResponse(template.render(context, request))
