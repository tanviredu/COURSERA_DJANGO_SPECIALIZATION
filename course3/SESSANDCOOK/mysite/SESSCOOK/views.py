from django.shortcuts import render
from django.http      import HttpResponse



## setting the cookie in the browser
def cookie(request):
    ## this is in the client side
    ## in the browser

    print("[+] the cookies are : ")
    print(request.COOKIES);
    #return HttpResponse(request.COOKIES)
    #fetching the cookie
    # if there give it otherwise set None
    oldval = request.COOKIES.get('zap',None)
    resp   = HttpResponse("Cookie : "+str(oldval))
    ##return resp
    if oldval:
        resp.set_cookie('zap',100) # untill the browser close
    else:
        resp.set_cookie('zap',42)  ## untill the browser close

    resp.set_cookie("Tanvir",4000,max_age=100000)
    return HttpResponse(request.COOKIES)




## setting session in the Browser

def sessfun(request):
    ## this is the server side data
    ## temporary store
    ## get the num visit or get 0 then +1
    num_visit = request.session.get('num_visit',0)+1
    ## storing the session in the sess variable
    request.session['num_visit'] = num_visit
    if num_visit >= 4:
        del(request.session['num_visit'])
    return HttpResponse('view_count = '+str(num_visit))