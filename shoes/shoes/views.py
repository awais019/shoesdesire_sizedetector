from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UploadedImage
from .utils import get_foot_size
from django.core.files.storage import default_storage


@csrf_exempt
def foot_size_api(request):
    if request.method == 'POST' and request.FILES.get('image', None):
        image_file = request.FILES['image']

        # Save the file temporarily
        file_name = default_storage.save(image_file.name, image_file)
        file_path = default_storage.path(file_name)

        print('File saved to', file_path)

        try:
            length, width = get_foot_size(file_path)
            default_storage.delete(file_name)  # Clean up the file

            return JsonResponse({
                'foot_length_in': length / 25.4,
                'foot_width_inc': width / 25.4
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request'}, status=400)
