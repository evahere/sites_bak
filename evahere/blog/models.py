from django.db import models
# from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# class Article(models.Model):
#     article_id = models.AutoField(primary_key=True)
#     # 文章标题
#     title = models.TextField()
#     #文章摘要
#     brief_content = models.TextField()
#     #文章主要内容
#     content = models.TextField()
#     #文章发布日期
#     publish_date = models.DateTimeField(auto_now=True)
#
#     # content = UEditorField(verbose_name='文章内容')
#
#
#
#
#     # def get_brief_content(self):
#     #     return (self.content[0:3]+'...')
#
#     def __str__(self):
#         return self.title


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章主要内容
    # content = RichTextField(config_name='my_config')
    content = RichTextUploadingField(config_name='my_config')

    # 文章发布日期
    publish_date = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    views = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title