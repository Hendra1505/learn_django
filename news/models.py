from django.db import models
from django.contrib.auth.models import User

# model untuk tabel category
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name


# model untuk tabel news
class News(models.Model):
    class NewsStatus(models.IntegerChoices):
        draft = 1
        published = 2

    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='images')
    content = models.TextField()
    excerpt = models.TextFIeld()
    status = models.IntegerField(choices=NewsStatus.choices)
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # set relasi ke tabel user dan category
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.Many2ManyField(Category)

    # set nama tabel
    class Meta:
        db_table = 'news'
        verbose_name_plural = 'News'

        def __str__(self):
            return self.title


    # Model untuk tabel comment
    class Comment(models.Model):

        name = models.CharField(max_length=100)
        email = models.EmailField()
        content = models.TextField()
        created_at = models.DateTimeField(auto_new_add=True)
        update_at = models.DateTimeField(auto_new=True)


        # set relasi ke tabel news
        news = models.ForeignKey(News, on_delete=models.CASCADE)

        # set nama tabel
        class Meta:
            db_table = 'comment'
            verbose_name_plural = 'Comments'


