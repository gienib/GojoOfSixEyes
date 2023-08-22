from django.db import models

'''class Folder(models.Model):
    name = models.CharField(max_length=256)
    path = models.CharField(max_length=256)

    # class Meta:
    #     ordering = ['name', 'path']

    def __str__(self):
        return self.name'''

class File(models.Model):
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=512)
    comments = models.CharField(max_length=512, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    # class Meta:
    #     ordering = ['title, url']
    
    def __str__(self):
        return self.title