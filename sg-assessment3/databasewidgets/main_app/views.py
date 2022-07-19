
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from main_app.models import *
from django.views.generic.edit import IndexView, CreateView, DeleteView
from django.urls import reverse
reverse('main_app_myview', args=())

# Single page Django app


# The index is the root homepage

# def index(request):
#     return HttpResponse("Hello, world. You're at the widgets index.")


# def index(request):
#     return render(request, 'index.html')


# List of all widgets
def widgets_index(request):
    Widgets = Widget.objects.all()
    return render(request, 'index.html', {'Widgets': Widgets})

# or


def IndexView(request):
    form = WidgetsForm()
    if request.method == 'POST':
        form = WidgetsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("""please enter in correct value, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    return render(request, 'index.html', {'form': form})


# alternative...


# def all_widgets(request):
#     return render(request, 'index.html', {
#         'widgets': Widget.objects.all()
#     })


# Details for each widget
# def widgets_detail(request, widget_id):
#     Widget = Widget.objects.get(id=widget_id)
#     # instantiate WidgetsForm to be rendered in the template
#     widgets_form = WidgetsForm()
#     return render(request, 'index', {
#         # context
#         'Widget': Widget, 'widgets_form': widgets_form
#     })


# def widget_detail(request, pk):
#     return render(request, 'index.html', {
#         'widget': get_object_or_404(Widget, pk=id)
#     })


# CREATE
# class WidgetCreate(CreateView):
#     model = Widget
#     fields = ['name', 'breed', 'description', 'age']


# # ...

# review from class lessons:
# def cats_detail(request, cat_id):
#     cat = Cat.objects.get(id=cat_id)
#     # instantiate FeedingForm to be rendered in the template
#     feeding_form = FeedingForm()
#     return render(request, 'cats/detail.html', {
#         # include the cat and feeding_form in the context
#         'cat': cat, 'feeding_form': feeding_form
#     })v


# ...
# NOTE This function broke the app
# Now even when I remove it it remains in renderers.py

def add_widget(request, widget_id):
    # create a ModelForm instance using the data in request.POST
    form = WidgetsForm(request.POST)
    # validate the form
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.widget_id = widget_id
        new_widget.save()
    return redirect('index', widget_id=widget_id)


# DELETE
# class WidgetDelete(DeleteView):
#     model = Widget
#     success_url = ''


# .............

# Attempt #4 to clear
# Error NoReverseMatch at /
# Reverse for 'add_widget' not found. 'add_widget' is not a valid view function or pattern name.

def index(request):
    widget = Widget.objects.all()
    return render(request, 'index.html', {'widget': widget})


def create(request):
    create = WidgetsForm()
    if request.method == 'POST':
        create = WidgetsForm(request.POST, request.FILES)
        if create.is_valid():
            create.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
        # else:
        #     return render(request, 'widget/create_form.html', {'create_form': create})


def update_widget(request, widget_id):
    widget_id = int(widget_id)
    try:
        widget_del = Widget.objects.get(id=widget_id)
    except Widget.DoesNotExist:
        return redirect('index')
    widget_form = WidgetsForm(request.POST or None, instance=widget_del)
    if widget_form.is_valid():
        widget_form.save()
        return redirect('index')
    return render(request, 'widget/create_form.html', {'create_form': widget_form})


def delete_widget(request, widget_id):
    widget_id = int(widget_id)
    try:
        widget_del = Widget.objects.get(id=widget_id)
    except Widget.DoesNotExist:
        return redirect('index')
    widget_del.delete()
    return redirect('index')


def delete_widget_all(request):
    Widget.objects.all().delete()
    return redirect('index')
