from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255)
    tab_target = models.CharField(max_length=255, blank=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    is_visible = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    positions = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['positions', 'title', 'time_created']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Dishes(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1000, blank=True)
    photo = models.FileField(default='/static/main_app/img/no_photo.jpg', blank=True)
    price = models.FloatField(default=0)
    special = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    menu = models.ManyToManyField(Menu)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Блюда"
        verbose_name_plural ="Блюдо"


class Sale(models.Model):
    title = models.CharField(max_length=255, default=" ")
    content = models.TextField(max_length=1000,  null=True)
    price = models.FloatField(default=0,  null=True)
    is_work = models.BooleanField(default=False,  null=True)
    date_created = models.DateField(auto_now_add=True,  null=True)
    date_start = models.DateField(auto_now=True, null=True)
    date_stop = models.DateField(auto_now=True,  null=True)

    class Meta:
        verbose_name = "Акції"
        verbose_name_plural = "Акція"


class Status(models.Model):
    title = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title


class Clients(models.Model):
    name = models.CharField(max_length=255, verbose_name='Імья')
    e_mail = models.EmailField( verbose_name='пошта')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    date = models.DateField(verbose_name='Дата прибуття')
    time = models.TimeField(verbose_name='Час Прибуття')
    message = models.TextField(max_length=1500, verbose_name='Повідомлення', null=True)
    count_of_people = models.SmallIntegerField(verbose_name='Кількість людей')
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, default=1, verbose_name='Статус замовлення')

    def __str__(self):
        return self.name

    class Meta:
         ordering = ['date', 'time']
         verbose_name = 'Клиєнт'
         verbose_name_plural = 'Клиєнти'


#заложена на будущее
class Galery(models.Model):
    image = models.FileField()
    text = models.CharField(max_length=255, default=' ')
    is_visible = models.BooleanField(default=False)


class Events(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.CharField(max_length=255, verbose_name='Опис')
    price = models.SmallIntegerField(default=100, verbose_name='Ціна')
    image = models.FileField(default='media/default_events.jpg', verbose_name='Фото')
    date_start = models.DateField(auto_now=True)
    date_stop = models.DateField()
    is_visible = models.BooleanField(default=False, verbose_name='Активне чи ні')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_start']
        verbose_name = "Подія"
        verbose_name_plural = 'Події'


class Chief(models.Model):
    title = models.CharField(max_length=255, verbose_name='ПІБ')
    position = models.CharField(max_length=255, verbose_name='Посада')
    content = models.TextField(max_length=1000, verbose_name='Опис')
    photo = models.FileField(null=True)
    is_visible = models.BooleanField(default=True, verbose_name='Видимість')
    date_start = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', 'date_start']
        verbose_name = "Повар"
        verbose_name_plural = 'Повари'











