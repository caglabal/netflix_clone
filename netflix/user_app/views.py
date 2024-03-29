from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


#*register sayfası
def register_page(request):

    if request.user.is_authenticated:   #kullanıcı girişliyse
        return redirect('page-select-profile')

    context = {}
    context["registerForm"] = UserForm

    if request.method == 'POST':
        form = UserForm(request.POST)
        #form geçerli mi değil mi
        if form.is_valid():
            #veritabanına kaydet
            form.save()
            #logine yönlendir
            return redirect('page-index')
        else:
            #hata ver
            print("FORM HATASI", form.errors)
            # return redirect('page-register')
            context["errorForm"] = form.errors
            return render(request,"register.html",context)
    else:   
        #get ise sayfayı hazırlasın
        return render(request,"register.html",context)
    

#*login sayfası
def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('sifre')

        if username and password:
            #böyle bir kullanıcı var mı
            user = authenticate(request, username = username, password = password)

            if user is None:
                #böyle bir user yoksa
                return redirect('page-login')
            else:
                #login et
                login(request,user)
                #anasayfaya yönlendir
                return redirect('page-select-profile')
        else:
            #inputlar boş
            return redirect('page-login')

    else:
        return render(request,"login.html")
    

@login_required(login_url="page-login")   #eğer giirşli değilse page-logine yönlendirilcek.
def select_profile(request):

    context = {}
    context["form"] = ProfileForm

    if request.method == 'POST':
        new_profile = ProfileForm(request.POST,request.FILES)

        if new_profile.is_valid():
            #veritabanına kaydet
            new_profile = new_profile.save()
            #requestteki user hesabının alt hesabı olarak ekle
            request.user.profile.add(new_profile)  #manytomany kendine özel fonksiyonları var add:ekleme,remove:çıkarır,all:forEach
            return redirect('page-select-profile')

        else:
            #hata ver
            print("form hatası: ",new_profile.errors)
            return redirect('page-select-profile')

    else:
        #güncelleme formu
        profileUpdateForms = {}  #obje olusturduk
        for profile in request.user.profile.all():  #bütün profilleri getir. 
            profileUpdateForms[profile.id] = ProfileForm(instance=profile)  #bu instance ile profile içeriğini bana getir demek.

            context['UpdateForms'] = profileUpdateForms.items()  #update formu bana obje olarak getir context ile bunu frontende göndermeye çalılyoruz.


        return render(request,"profile.html",context)
    
@login_required(login_url="page-login")  #girişli değilse update yapamaz.
def updateProfile(request,profileId):
    
    if request.method == 'POST':
        instance = NetflixProfile.objects.filter(id = profileId).first() #profile id si id ye eşit olanları netflixprofile modelinden getir.

        if instance is None:
            return redirect('page-select-profile')

        profile = ProfileForm(request.POST,request.FILES, instance=instance)  #istek yapıcaz post ile o yüzden equest.post vs yapmalıyız.Foto eklenecek ondan dolayı fıles
        #profil ekleme modal yapımı getirmesi için. instance fonksiyonu insatnce değişkeni 

        if profile.is_valid():
            #veritabanına kaydet
            profile = profile.save()
            return redirect('page-select-profile')

        else:
            pass
        return redirect('page-select-profile')

    else:
        return redirect('page-select-profile')
    

#delete profile
@login_required(login_url="page-login")  #girişli değilse delete yapamaz.
def delete_profile(request,profileId):

    instance = NetflixProfile.objects.filter(id = profileId).first()

    if instance is None:
        return redirect('page-select-profile')
    else:
        instance.delete()
        return redirect('page-select-profile')
    

#dashbord html için görüntüleme fonksyonu
def load_dashboard(request):

    return render(request,"dashboard.html")