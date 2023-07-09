# Create your models here.
from django.db import models
from django.db import utils
from django.contrib.auth.models import User
import datetime

article = 'A'
news = 'N'
POSTTYPE = [(article, 'Статья'),
            (news, 'Новость')]


# Модель, содержащая объекты всех авторов.
class Author(models.Model):
    # Имеет следующие поля:
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)         # - cвязь «один к одному» с встроенной моделью пользователей User;
    _author_rating = models.IntegerField(default=0, db_column='author_rating') # - рейтинг пользователя.Ниже будет дано описание того, как этот рейтинг можно посчитать.

    @property
    def update_rating(self):
        return self._author_rating

    @update_rating.setter
    def author_rating(self):
        # Рейтинг состоит из следующего:
        # - суммарный рейтинг каждой статьи автора умножается на 3;
        post_rating_sum = sum(Post.objects.filter(post_author=self.author_user).values('post_rating')) * 3
        # - суммарный рейтинг всех комментариев автора;
        comments_author_rating_sum = sum(Comment.objects.filter(comment_author=self.author_user).values('comment_rating'))
        # - суммарный рейтинг всех комментариев к статьям автора.
        comments_post_rating_sum = 0

        self._author_rating = post_rating_sum + comments_author_rating_sum + comments_post_rating_sum

    # # Создайте пользователя и сохраните его в базе данных
    # user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')
    # # Обновите поля и сохраните их снова
    # user.first_name = 'John'
    # user.last_name = 'Citizen'
    # user.save()

class Category(models.Model):
    # Категории новостей / статей — темы, которые они отражают(спорт, политика, образование и т.д.).
    # Имеет единственное поле (должно быть уникальным (в определении поля необходимо написать параметр unique = True)):
    category_name = models.CharField(max_length=50, unique=True)  # - название категории.


# Эта модель должна содержать в себе статьи и новости, которые создают пользователи. Каждый объект может иметь одну или несколько категорий.
class Post(models.Model):
    # Модель должна включать следующие поля:
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)          # - связь «один ко многим» с моделью Author;
    post_type = models.CharField(max_length=2, choices=POSTTYPE, default='N')  # - поле с выбором — «статья» или «новость»;
    post_date = models.DateTimeField(auto_now_add=datetime.datetime.now())     # - автоматически добавляемая дата и время создания;
    post_category = models.ManyToManyField(Category, through='PostCategory')   # - связь «многие ко многим» с моделью Category(с дополнительной моделью PostCategory);
    post_title = models.CharField(max_length=124)                              # - заголовок статьи / новости;
    post_text = models.TextField()                                             # - текст статьи / новости;
    post_rating = models.IntegerField()                                        # - рейтинг статьи / новости.

    # - Метод like() увеличивает рейтинг на единицу.
    def like(self):
        return self.post_rating + 1

    # - Метод dislike() уменьшает рейтинг на единицу.
    def dislike(self):
        return self.post_rating - 1

    # - Метод preview(), который возвращает начало статьи (предварительный просмотр) длиной 124 символа и добавляет многоточие в конце.
    def preview(self):
        return str(self.post_text)[0:125] + '...'

# Промежуточная модель для связи «многие ко многим»:
class PostCategory(models.Model):
    # - связь «один ко многим» с моделью Post;
    post_connection = models.ForeignKey(Post, on_delete=models.CASCADE)
    # - связь «один ко многим» с моделью Category.
    category_connection = models.ForeignKey(Category, on_delete=models.CASCADE)


# Под каждой новостью/статьёй можно оставлять комментарии, поэтому необходимо организовать их способ хранения тоже.
class Comment(models.Model):
    # Модель будет иметь следующие поля:
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE) # - связь «один ко многим» с моделью Post;
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE) # - связь «один ко многим» со встроенной моделью User (комментарии может оставить любой пользователь, необязательно автор);
    comment_text = models.TextField()                                # - текст комментария;
    comment_datetime = models.DateTimeField(auto_now_add=datetime.datetime.now()) # - дата и время создания комментария;
    comment_rating = models.IntegerField()                           # - рейтинг комментария

    # - Метод like() увеличивает рейтинг на единицу.
    def like(self):
        return int(self.comment_rating) + 1

    # - Метод dislike() уменьшает рейтинг на единицу.
    def dislike(self):
        return int(self.comment_rating) - 1


