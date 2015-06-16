from django.shortcuts import render

from search import get_snippets


def home(request):
    query = request.POST.get('query', '')
    snippets = get_snippets(query)
    return render(
        request, 'home.html',
        {
            'query': query,
            'snippets': snippets,
        }
    )
