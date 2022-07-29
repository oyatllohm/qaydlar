from django.shortcuts import render
from django.views import View
# Create your views here.
from django.views.generic import DeleteView ,DetailView ,UpdateView
from .models import Qaydlar
from django.urls import reverse_lazy
class Homview(View):
    def get(self,request):
        qayd = Qaydlar.objects.all()
        # q= Qaydlar.objects.delete(qayd)
        
        context={
            'qayd':qayd
        }
        
        return render(request=request, template_name='index.html',context=context)



class Formsview(View):
    def get(self,request):
        
      
        return render(request=request, template_name='forms.html')

    def post (self,request):
        
        qayd = request.POST.get('qayd')
        vaqt = request.POST.get('vaqt')
        maqsad = request.POST.get('maqsad')
        muhum = request.POST.get('muhum')
       
        Qaydlar.objects.create(
            qayd_name=qayd,
            reg_Time = vaqt,
            maqsad=maqsad,
            muhim=muhum,
        )
        
        return render(request=request, template_name='forms.html')

# class DDeleteView(View):
#     # model = Qaydlar
#     # template_name = 'delit.html'
    
    
#     def get(self,request):
#         return render(request,'delit.html')
class DDetailview(DeleteView ):
    
    model = Qaydlar
    template_name: str = "delit.html"
    context_object_name:str = 'q'
    success_url = reverse_lazy('home')
    
    
class UUpdateView(UpdateView):
    model = Qaydlar
    template_name = 'edit.html'
    fields = ['qayd_name','reg_Time','maqsad','muhim']
    context_object_name:str = 't'
    success_url = reverse_lazy('home')