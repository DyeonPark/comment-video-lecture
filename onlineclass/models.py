from django.db import models
from upload.models import Document


# 최종 Commentor 서비스를 위한 모델
class Helper(models.Model):
	helper_id = models.AutoField(primary_key=True)
	doc_id = models.ForeignKey(Document, on_delete=models.CASCADE)
	helper_audio = models.FilePathField() #FileField(upload_to="%Y-%m-%d-%H-%M-%S\\helper")
	helper_txt = models.FilePathField() #FileField(upload_to="%Y-%m-%d-%H-%M-%S\\helper")
	helper_csv = models.FilePathField() #FileField(upload_to="%Y-%m-%d-%H-%M-%S\\helper")


# 최종 Commentor 서비스를 위해 필요한 이미지를 저장하는 모델
class ImageCapture(models.Model):
	img_id = models.AutoField(primary_key=True)
	helper_id = models.ForeignKey(Helper, on_delete=models.CASCADE)
	img_file = models.FilePathField() #ImageField(upload_to="%Y-%m-%d-%H-%M-%S\\helper\\capture_img")

	# def create(self):
	# 	self.imgfile.path = self.helper_id.doc_id.docFile.path + "\\capture_FA\\" + self.imgfile.name
	# 	#
