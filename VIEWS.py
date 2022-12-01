CLASS BASE VIEWS

listview,detailview,templateview,createview,formview

class items(ListView):
    model=modelname
    template_name="temp.html"
    context_object_name='name'

class item1(detailview):
    model=modelname
    template_name="temp.html"
    context_object_name='name'
    

fuunction based views-
 def functionname(request):
     return response("value")