from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Blog(models.Model):
    category = models.ManyToManyField(Category,  related_name="category")
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='blog/static/images/')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
      return f'{self.title}'

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# filter contains
# >>> blog = Blog.objects.filter(id__contains='django orm')
# >>> print(blog.query)
# SELECT "blog_blog"."id", "blog_blog"."title", "blog_blog"."image", "blog_blog"."body", "blog_blog"."created", "blog_blog"."updated" FROM "blog_blog" WHERE "blog_blog"."id" LIKE %django orm% ESCAPE '\'

# filter icontains

#blog1 = Blog.objects.filter(id__incontains='django orm')
#print(blog1.query)
#SELECT "blog_blog"."id", "blog_blog"."title", "blog_blog"."image", "blog_blog"."body", "blog_blog"."created", "blog_blog"."updated" FROM "blog_blog" WHERE "blog_blog"."id" LIKE %django orm% ESCAPE '\'


# filter objects.all

# >>> from blog.models import Blog
# >>> blog = Blog.objects.all()
# >>> print(blog.query)
# SELECT "blog_blog"."id", "blog_blog"."title", "blog_blog"."image", "blog_blog"."body", "blog_blog"."created", "blog_blog"."updated" FROM "blog_blog"

# filter id=10

# SELECT "blog_blog"."id", "blog_blog"."title", "blog_blog"."image", "blog_blog"."body", "blog_blog"."created", "blog_blog"."updated" FROM "blog_blog"
# >>> blog1 = Blog.objects.filter(id=5)
# >>> print(blog1.query)
# SELECT "blog_blog"."id", "blog_blog"."title", "blog_blog"."image", "blog_blog"."body", "blog_blog"."created", "blog_blog"."updated" FROM "blog_blog" WHERE "blog_blog"."id" = 5


# filter id__lessther

# >>> blog2 = Blog.objects.filter(id__lt=3)
# >>> print(blog2.query)
# SELECT "blog_blog"."id", "blog_blog"."title", "blog_blog"."image", "blog_blog"."body", "blog_blog"."created", "blog_blog"."updated" FROM "blog_blog" WHERE "blog_blog"."id" < 3