from django.http.response import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import Note
from .serializers import NoteSerializer

# Create your views here.
def createNote(request):
    if request.method == 'POST':
        print(request.method)
        instance = Note(
            title=request.POST.get('title', ''),
            content=request.POST.get('content', ''),
            image_ids=request.POST.get('image_ids', ''),
        )
        print(request.POST)
        print(instance)
        instance.save()

        return JsonResponse({})

def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True, context={'short': True})

    return JsonResponse(serializer.data, safe=False)

def getNote(request):
    id = request.GET.get('id', None)
    try:
        instance = Note.objects.get(id=id)
    except Note.DoesNotExist:
        return HttpResponseNotFound()
    serializer = NoteSerializer(instance)
    return JsonResponse(serializer.data, safe=False)
