from django.http import HttpResponse

def ccmsMission(request):
    return HttpResponse("CCMS Mission View")


def ccmsVision(request):

    return HttpResponse("CCMS Vision View")

def ccmsObjectives(request):
    return HttpResponse("CCMS Objectives View")