# accounts/context_processors.py
from .models import Author

def author_info(request):
    if request.user.is_authenticated:
        try:
            author = Author.objects.get(user=request.user)
            return {'author': author}
        except Author.DoesNotExist:
            return {}
    return {}
