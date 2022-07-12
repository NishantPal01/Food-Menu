from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ItemForm
from food.models import Items
from .models import Items
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.

# def index(request):
#     items = Items.objects.all()
    
#     # template = loader.get_template('')
#     context = {
#         'items':items,
#     }

#     # return HttpResponse(template.render(context,request))
#     return render(request, 'food/index.html', context)


class IndexClassView(ListView):
    model = Items;
    template_name = 'food/index.html'
    context_object_name = 'items'


def food(request):
    return HttpResponse('<h3> welcome to my food menu </h3>')


# def details(request, item_id):
#     item_list = Items.objects.get(pk=item_id)
#     context = {
#         'item_list':item_list
#     }
#     return render(request, 'food/detail.html', context)

class DetailViewItem(DetailView):
    model = Items
    template_name = 'food/detail.html'
    

def create_form(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request,'food/item_form.html',{'form':form})

class CreateItem(CreateView):
    model = Items;
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'food/item_form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def update(request, id):
    item = Items.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')


    return render(request,'food/item_form.html',{'form':form,'item':item})

def delete_item(request, id):
    item = Items.objects.get(id=id)
    

    if request.method == 'POST':
        item.delete()
        return redirect('index')

    return render(request,'food/delete-form.html',{'item':item})

