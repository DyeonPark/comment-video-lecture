from upload.models import Document
from django.shortcuts import render
from upload.cmt_1_preprocess import execute_preprocess
from upload.cmt_2_mix import execute_mix

def upload_files(request):
    if request.method == "POST":

        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        videoFile = request.FILES["videoFile"]
        docFile = request.FILES["docFile"]

        document = Document.objects.create(
                title=fileTitle,
                videoFile=videoFile,
                docFile=docFile,
        )

        # 파일 저장경로(path) 불러오기
        path = document.docFile.path
        print("document.docFile.path: ", path)
        path = path[:-15]

        # commentor 서비스 실행
        execute_preprocess(path)
        execute_mix(path)

    documents = Document.objects.all()

    return render(request, "upload/upload_file.html", context={
        "files": documents
    })
