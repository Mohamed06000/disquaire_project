from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Artist, Contact, Booking
from django.shortcuts import render

def index(request):
    # request albums
    albums = Album.objects.filter(available=True).order_by('-create_at')[:12]
    # then format the request.
    # note that we don't use album['name'] anymore but album.name
    # because it's now an attribute.
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))

    context = {
        'albums': albums
    }

    return render(request, 'store/index.html', context)


def listing(request):
    albums = Album.objects.filter(available=True)
    context = {
        'albums': albums
    }

    return render(request, 'store/listing.html', context)


def detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    artists = [artist.name for artist in album.artists.all()]
    artists_name = " ".join(artists)
    context = {
        'album_title': album.title,
        'artists_name': artists_name,
        'album_id': album.id,
        'thumbnail': album.picture
    }

    return render(request, 'store/detail.html', context)


def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains=query)  # contains sert a rechercher une partie d'un mot et icontains pour eviter la casse

        if not albums.exists():
            albums = Album.objects.filter(artists__name__icontains=query)

    title = "Résultats pour la requête %s" % query
    context = {
        'albums': albums,
        'title': title
    }

    return render(request, 'store/search.html', context)
