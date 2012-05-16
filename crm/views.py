from django.shortcuts import render
from forms import ChildForm
from models import Child

def test(request):
    if request.method == "GET":
        try:
            print "trying"
            child_id = request.GET['id']
            print "1"
            child = Child.objects.get(id=child_id)
            print "2"
            form = ChildForm(instance=child)
            print "still trying"
        except Exception as e:
            print e
            child_id = None
            form = ChildForm()
            print "failed"

    else:
        form = ChildForm(request.POST)
        if form.is_valid():
            form.save()



    return render(request, 'test.html', {'form': form})






    pass
