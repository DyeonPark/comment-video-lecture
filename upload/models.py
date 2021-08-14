from django.db import models

#교수자가 업로드하는 모델
class Document(models.Model):
	title = models.CharField(max_length=200)
	videoFile = models.FileField(upload_to='%Y-%m-%d-%H-%M-%S')
	docFile = models.FileField(upload_to='%Y-%m-%d-%H-%M-%S')
	dateTimeOfUpload = models.DateTimeField(auto_now=True)


# class ImageCapture(models.Model):
# 	img_id = models.AutoField(primary_key=True)
# 	helper_id = models.ForeignKey(Helper, on_delete=models.CASCADE)
# 	imgfile = models.ImageField(upload_to="capture_FA")
#
# 	def create(self):
# 		self.imgfile.path = self.helper_id.doc_id.docFile.path + "\\capture_FA\\" + self.imgfile.name
# 		#
