from django.http  import HttpResponse
from django.shortcuts import redirect


def unauth_user(view_func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
          return view_func(request,*args,**kwargs)
    return wrapper


def allowed_user(allowed_roles=[]):
    def decorater(view_func):
        def wrapper(request,*args,**kwargs):
                group = None
                if request.user.groups.exists():
                    # a=request.user.groups.all()
                    # print(a)
                    group = request.user.groups.all()[0].name

                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse('You are not authorized to view this page')  #make a error 404 page with link back to home
        return wrapper
    return decorater

#AdminLvl0------->mother bank admin
#AdminLvl1--------->mini bank admin
#no role--------->general page home