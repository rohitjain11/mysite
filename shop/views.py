from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models import User, Product


#register 
def register(request):
    if request.method == 'POST':
        name = request.POST["name"]
        username = request.POST["username"]
        num = request.POST["num"]
        email = request.POST["email"]
        pword = request.POST["pword"]

        info = User(name=name,username=username,num=num,pword=pword,email=email)
        info.save()
        return redirect('login')

    else:
        if request.session.has_key('user'):
            return redirect('product_list')
        else:
            return render(request, 'register.html')

#login
def login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        pword = request.POST["pword"]
        try:
            info = User.objects.get(email=email, pword=pword)
        except:
            return render(request, 'login.html',{"msg":"invalid"})
        if info is not None:
            dd = {'name':info.name,'id':info.id}
            request.session['user'] = dd
            return redirect('product_list')

    else:
        if request.session.has_key('user'):
            return redirect('product_list')
        else:
            return render(request, 'login.html')



# show product list
def product_list(request):
    if request.session.has_key('user'):
        dd = request.session['user']
        ol = Product.objects.all()

        return render(request, 'product_list.html', {"dd" : dd,'ol':ol })

    else:
        return redirect('login')


def product_details(request, id):
    if request.session.has_key('user'):
        dd = request.session['user']
        ol = Product.objects.get(id=id)
        return render(request, 'product_details.html',{"dd" : dd,'ol':ol })

    else:
        return redirect('login')

def logout(request):
    if request.session.has_key('user'):
        del request.session['user']
    return redirect('login')
