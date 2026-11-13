from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q




def create_garn(request):
    if request.method == "POST":
        data = request.POST
        Ganr.objects.create(
            name = data['name']
        )
        return redirect('add_film')
    return render(request, 'add_ganr.html')


def create_film(request):
    if request.method == "POST":
        data = request.POST
        Film.objects.create(
            name = data['name'],
            caption = data['caption'],
            photo = request.FILES['photo'],
            ganr_id = Ganr.objects.get(id=data['ganr_id'])
        )
        return redirect('add_film')
    ganrrr = Ganr.objects.all()
    return render(request, 'add_film.html', {'ganr':ganrrr})



def create_comment(request):
    if request.method == "POST":
        data = request.POST
        Comment.objects.create(
            author = data['author'],

            text = data['text'],
            film_id = Film.objects.get(id = data['film_id'])
        )
        return redirect('show_comments')
    films = Film.objects.all()
    return render(request, 'add_comment.html', {'films': films})




def show_comments(request):
    query = request.GET.get('q', '')
    comments = Comment.objects.all()
    if query:
        comments = comments.filter(text__icontains=query)
    return render(request, 'comments.html', {'comments': comments, 'query': query})


def show_ganr(request):
    query = request.GET.get('q', '').strip()
    ganr = Ganr.objects.all()
    if query:
        ganr = ganr.filter(name__icontains=query)
    return render(request, 'ganr.html', {'ganr': ganr, 'query': query})



def show_films(request):
    query = request.GET.get('q')
    films = Film.objects.all()
    if query:
        films = films.filter(
            name__icontains=query
            )
    return render(request, 'films.html', {'films': films, 'query': query})


def detail_film(request, id):
    item = Film.objects.get(id=id)
    return render(request, 'detail_film.html', {'i': item})


def delete_film(request, id):
    if request.method == 'POST':
        item = Film.objects.get(id=id)
        item.delete()
        return redirect('show_films')

    return redirect('show_films')


def detail_comment(request, id):
    item = Comment.objects.get(id=id)
    return render(request, 'detail_comment.html', {'item': item})


def delete_comment(request, id):
    if request.method == 'POST':
        item = Comment.objects.get(id=id)
        item.delete()
        return redirect('show_comments')

    return redirect('show_comments')


def detail_ganr(request, id):
    item = Ganr.objects.get(id=id)
    return render(request, 'detail_ganr.html', {'item': item})


def delete_ganr(request, id):
    if request.method == 'POST':
        item = Ganr.objects.get(id=id)
        item.delete()
        return redirect('show_ganr')

    return redirect('show_ganr')



