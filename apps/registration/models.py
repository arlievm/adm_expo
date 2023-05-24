from django.db import models


user_status = [
  [
    "Партнер",
    "Партнер"
  ],
  [
    "Участник",
    "Участник"
  ]
]


class Application(models.Model):
    
    class Meta:
        db_table = 'application'
        verbose_name = 'ПРЕДВАРИТЕЛЬНАЯ ЗАЯВКА'
        verbose_name_plural = 'ПРЕДВАРИТЕЛЬНАЯ ЗАЯВКА'
        
    name_organic = models.CharField(verbose_name="Название организации", max_length=128)
    surname = models.CharField(verbose_name="Фамилия", max_length=16)
    name = models.CharField(verbose_name="Имя", max_length=16)
    email = models.EmailField(verbose_name="E-mail", max_length=32)
    number = models.CharField(verbose_name="Телефон", max_length=16)
    user_status = models.CharField(verbose_name="Выберите направление", max_length=100, default=None, choices=user_status, blank=True, null=True)
    data = models.BooleanField(verbose_name="Я согласен на обработку моих персональных данных", default=False)
    
    def __str__(self):
        return self.name



class Registration(models,Models):

    class Meta:
      db_table = "registration"
      verbose_name = _("Registration")
      verbose_name_plural = _("Registration")
    
    name = models.CharField(verbose_name="Имя", max_length=32)
    surname = models.CharField(verbose_name="Фамилия", max_length=32)
    patronymic = models.CharField(verbose_name="Отчество", max_length=16,blank=True, null=True)
    email = models.EmailField(verbose_name="E-mail", max_length=32)
    city = models.CharField(verbose_name="Страна", max_length=16)
    dateofbirth = models.CharField(verbose_name="Страна", max_length=16)
    image_id_one = models.ImageField(verbose_name="Загрузите паспорт с лицевой стороны",max_length=16,blank=True,null=True)
    image_id_two = models.ImageField(verbose_name="Загрузите паспорт с обратной стороны",max_length=16,blank=True,null=True)
    photo_id = models.ImageField(verbose_name="Сделайте селфи с паспортом",max_length=16,blank=True,null=True)
    number = models.CharField(verbose_name="Телефон", max_length=16)
    whatsapp = models.CharField(verbose_name="WhatsApp", max_length=16)
    email = models.EmailField(verbose_name="Электронная почта", max_length=32)
    password_one = models.CharField(verbose_name="Придумайте пароль",max_length=36)
    password_two = models.CharField(verbose_name="Подтвердите пароль",max_length=36)
    interested = models.BooleanField(verbose_name="Я заинтересован в",max_length=36)
    hit_one = models.BooleanField(verbose_name="Посещение на HIT EXPO",max_length=36)
    hit_two = models.BooleanField(verbose_name="Участие на HIT EXPO",max_length=36)
    searching = models.BooleanField(verbose_name="Поиске проектов",max_length=36)
    other_one = models.BooleanField(verbose_name="Другое",max_length=36)
    event = models.BooleanField(verbose_name="Как вы узнали о мероприятие",max_length=36)
    insta = models.BooleanField(verbose_name="Инстаграм",max_length=36)
    radio = models.BooleanField(verbose_name="ТВ, Радио",max_length=36)
    news = models.BooleanField(verbose_name="Новостные порталы",max_length=36)
    other_two = models.BooleanField(verbose_name="Другое",max_length=36)

    def __str__(self):
        return self.name
    