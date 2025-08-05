from django.shortcuts import render, redirect
import requests

def index(request):
    query = request.GET.get('query','')
    page = int(request.GET.get('page',1))
    
    api_url = f"https://yts.mx/api/v2/list_movies.json"
    params = {
        'page': page,
        'query_term': query
    }
    
    try:
        response = requests.get(api_url, params=params)
        data = response.json()
        movies = data['data']['movies'] if data['data']['movie_count'] > 0 else []
    except Exception as e:
        movies = []
        print("Error fetching movies:", e)
        
    context = {
        'movies': movies,
        'query':query,
        'page':page
    }
    return render(request, 'main/index.html', context)

def movie(request, movie_id):
    url = f"https://yts.mx/api/v2/movie_details.json?movie_id={movie_id}&with_images=true&with_cast=true"
    response = requests.get(url)#, params=params)
    data = response.json()
    movie = data['data'].get('movie')
    # if not movie:
    #     return redirect('landing')
    context = {'movie':movie}
    return render(request, 'main/movie.html', context)

