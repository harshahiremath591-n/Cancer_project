from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .utils import predict_cancer_type
from .models import CancerPrediction

def home(request):
    if request.method == 'POST' and request.FILES.get('scan'):
        scan_file = request.FILES['scan']
        fs = FileSystemStorage()
        filename = fs.save(scan_file.name, scan_file)
        file_path = fs.path(filename)

        # The AI processing happens here
        label, score = predict_cancer_type(file_path)

        # Saving to your MySQL Database
        CancerPrediction.objects.create(image=filename, result=label, confidence=score)

        return render(request, 'home.html', {
            'result': label, 
            'score': score, 
            'url': fs.url(filename)
        })
    return render(request, 'home.html')