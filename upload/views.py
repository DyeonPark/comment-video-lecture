import os
from upload.models import Document
from onlineclass.models import Helper, ImageCapture
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from upload.cmt_1_preprocess import execute_preprocess
from upload.cmt_2_mix import execute_mix


def upload_files(request):
    if request.user.groups.exists():
        # 사용자 그룹 받아오기
        group = request.user.groups.all()[0].name

        # 교수자 그룹에 포함될 경우 렌더링
        if group == "professor_group":

            # 폼을 제출했을 경우 (POST) 그 외 (GET)
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

                # commenter 서비스 실행
                execute_preprocess(path)
                execute_mix(path)

                helper = Helper.objects.create(
                    doc_id=document,
                    helper_audio=path + "mix\\mix.mp3",
                    helper_txt=path + "txt\\0001.txt",
                    helper_csv=path + "transform_timeline_result.csv"
                )

                img_list = os.listdir(path + "capture_FA\\")
                img_list.sort()
                print(img_list)

                for img in img_list:
                    ImageCapture.objects.create(
                        helper_id=helper,
                        img_file=path + "capture_FA\\" + img
                    )

            documents = Document.objects.all()
            return render(request, "upload/upload_file.html", context={
                "files": documents
            })

        # 학생 그룹에 포함될 경우 렌더링
        elif group == "student_group":

            template = loader.get_template('upload/view_file.html')
            documents = Document.objects.all()
            context = {
                "files": documents
            }
            return HttpResponse(template.render(context, request))
