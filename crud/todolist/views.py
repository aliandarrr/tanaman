from urllib import request
from django.shortcuts import render, redirect
import psycopg2
from todolist import models
#def create(req):
#    if req.POST:
#        respon = req.POST['nama']
#        print(respon)
    #def create(req):
    #if req.POST:
        #print = ...
        #nama = req.POST['nama']
        #id = req.POST['nama']
        #email = req.POST['email']
        #password = req.POST['password']
        #print(respon)
        #print(nama)
        #print(email)
        #print(password)
        #connection = psycopg2.connect(host="localhost",database="database",user="postgres",password="postgres")
        #cursor = connection.cursor()
        #query = f"insert into public.todolist (nama) values ('{respon}')"
        #query = f"insert into public.email (nama,email) values ('{nama}','{email}')"  #insert #teks
        #query = f"insert into public.datauser (nama,email,password) values ('{nama}','{email}','{password}')"
        #query = f"select * from public.todolist where id =('{respon}')" #select #angka
        #query = f"select * from public.email where nama=('{nama}') and email=('{email}')"
        #query = f"update public.todolist set nama=('{respon}') where id = 5" #update #teks
        #query = f"update public.email set nama=('{nama}'), email=('{email}') where id = 1" #isi namanya angka email baru
        #query = f"delete from public.todolist where id =('{respon}')" #delete #angka
        #query = f"update public.email set nama = ('{nama}') where email = ('{email}')" #ganti nama
        #query = f"update public.email set email = ('{email}') where nama = ('{nama}')" #ganti email
        #query = f"delete from public.email where id =('{respon}')" #delete #angka
        #query = f"delete from public.email where nama =('{nama}')" #bisa
        #query = f"delete from public.email where email =('{email}')" #bisa
        #query = f"delete from public.email where email =('{email}') and nama=('{nama}') "


        #cursor.execute(query)
        #result = cursor.fetchone() #select
        #print(result) #select

        #connection.commit()

        #cursor.close()
        #connection.close()
    #return render(req, 'index.html')

def login(request):
        if request.POST:
            respon = models.login(request.POST)
            models.login.save()
        return render (request, 'login.html')

def Home(request):
    return render(request, 'Home.html')
def galeri(request):
    return render(request, 'galeri.html')
def Contact(request):
    return render(request, 'Contact.html')

def About(request):
    if request.POST and request.FILES['images']:
        nama = request.POST['nama']
        nama_latin = request.POST['nama_latin']
        cara_perawatan = request.POST['detail']
        jenis_tanaman = request.POST['jenis_tanaman']
        images = request.FILES['images']
        jumlah = request.POST['jumlah']
        models.bunga.objects.create(nama=nama, nama_latin=nama_latin, images=images, cara_perawatan= cara_perawatan, jenis_tanaman=jenis_tanaman, jumlah=jumlah)
        print("berhasil memasukkan data")   
    return render(request, 'About.html')

def Tanaman_Hias(request):
    return render(request, 'Tanaman_Hias.html')
def TanamanBuah(request):
    return render(request, 'TanamanBuah.html')
def TanamanSayur(request):
    return render(request, 'TanamanSayur.html')
def lainlain(request):
    return render(request, 'lainlain.html')

def Tanaman_Hias(request):
    data=models.bunga.objects.filter(jenis_tanaman=1)
    return render(request,'Tanaman_Hias.html',{'data':data})

def TanamanBuah(request):
    data=models.bunga.objects.filter(jenis_tanaman=2)
    return render(request,'TanamanBuah.html',{'data':data})
def TanamanSayur(request):
    data=models.bunga.objects.filter(jenis_tanaman=3)
    return render(request,'TanamanSayur.html',{'data':data})
def lainlain(request):
    data=models.bunga.objects.filter(jenis_tanaman=4)
    return render(request,'lainlain.html',{'data':data})

def edit(request,id):
    data = models.bunga.objects.filter(id=id).first()
    if request.method == "POST":
        nama = request.POST['nama']
        nama_latin = request.POST['nama_latin']
        cara_perawatan = request.POST['cara_perawatan']
        jenis_tanaman = request.POST['jenis_tanaman']
        jumlah = request.POST['jumlah']
        models.bunga.objects.filter(id=id).update(nama=nama, nama_latin=nama_latin, images=data.images, cara_perawatan= cara_perawatan, jenis_tanaman=jenis_tanaman, jumlah=jumlah)
        print("berhasil update data")   

    return render (request,"edit.html" ,{
        "data": data
    })

def hapus(request, id):
    data = models.bunga.objects.filter(id=id).delete()
    return redirect ("/Tanaman_Hias")

def Home(request):
    data = models.bunga.objects.all().order_by('jumlah').reverse()[:3]
    return render (request, 'Home.html', {'data':data})

