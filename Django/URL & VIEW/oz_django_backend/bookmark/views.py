from django.shortcuts import render

from bookmark.models import Bookmark


def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    bookmarks = Bookmark.objects.all()

    return render(
        request,
'bookmark_list.html', {
            'bookmark_list': bookmarks
        })