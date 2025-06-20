from django.http import HttpResponse

def alamat_view(request):
    return HttpResponse("Alamat: Jl. al muhajirin No. 9, cibolang kaler")

def telepon_view(request):
    return HttpResponse("Telepon: +62 821-3879-2075")
