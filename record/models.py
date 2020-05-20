from django.conf import settings
from django.db import models
from django.utils import timezone
from account.models import User



class Resident(models.Model):
    full_name     = models.CharField(verbose_name="名前",max_length=128)
    kana_full_name= models.CharField(verbose_name="ふりがな",max_length=128)
    DEPARTMENT_CHOICES = (#(保存する値,表示)
        ("1","1階"),
        ("2","2階"),
        ("3","3階"),
        ("4","4階"),
        ("5","5階"),
        ("6","6階"),
    )
    department      = models.CharField(
        verbose_name="部署",
        default="1",
        max_length=128,
        choices=DEPARTMENT_CHOICES,
    )
    birthday        = models.DateField(
        verbose_name="生年月日"
    )
    UNIT_CHOICES    = (
        ('E','東'),
        ('W','西'),
    )
    unit            = models.CharField(
        verbose_name="ユニット",
        default='E',
        max_length=1,
        choices=UNIT_CHOICES,
    )
    room            = models.IntegerField(
        verbose_name="部屋番号",
    )
    def register(self):
        self.save()
    def __str__(self):
        return self.full_name



class Staff(User):
    kana_first_name= models.CharField(verbose_name="姓（かな）",max_length=128)
    kana_last_name= models.CharField(verbose_name="名（かな）",max_length=128)
    DEPARTMENT_CHOICES = (#(保存する値,表示)
        ("1","1階"),
        ("2","2階"),
        ("3","3階"),
        ("4","4階"),
        ("5","5階"),
        ("6","6階"),
    )
    department = models.CharField(
        verbose_name="部署",
        default="1",
        max_length=128,
        choices=DEPARTMENT_CHOICES,
    )
    CHOICE_OCCUPATION=(
        ("CS","介護職"),
        ("NS","看護師"),
        ("Dr","医師"),
        ("PT","理学療法士"),
        ("OT","作業療法士"),
        ("ST","言語聴覚士"),
    )
    occupation=models.CharField(
        verbose_name="職種",
        choices=CHOICE_OCCUPATION,
        max_length=128,
        default="CS",
    )
    READING_SUPPORT_NECESSITY=(
        (0,"不要"),
        (1,"必要"),
    )
    reading_comprehension=models.IntegerField(
        verbose_name="日本語サポートの必要性",
        choices=READING_SUPPORT_NECESSITY,
        default=1
    )


class Record(models.Model):
    resident        = models.ForeignKey(
        Resident,
        verbose_name="利用者",
        on_delete=models.CASCADE,
        null=True,
    )
    staff           = models.ForeignKey(
        Staff,
        verbose_name="職員",
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    date            = models.DateField(
        verbose_name="日付",
        default=timezone.now,
    )
    time            = models.TimeField(
        verbose_name="時刻",
        default="00:00"
    )
    notice          = models.CharField(
        verbose_name="特記事項",
        max_length=8000,
        blank=True, null=True
    )
    translated_notice= models.CharField(
        verbose_name="変換結果",
        max_length=8000,
        blank=True, null=True
    )
    written_date    = models.DateTimeField(
        blank=True, null=True
    )
    department      = models.CharField(
        verbose_name="部署",
        max_length=128,
    )
    unit            = models.CharField(
        verbose_name="ユニット",
        max_length=128,
    )
    isTranslated    = models.BooleanField(
        verbose_name="変換済みかどうか",
        default=False,
    )
    def register(self):
        self.written_date=timezone.now()
        self.department=self.resident.department
        self.unit=self.resident.unit
        self.save()







class Meal_record(Record):
    KIND_CHOICES   = (
        ('朝食','朝食'),
        ('昼食','昼食'),
        ('夕食','夕食'),
    )
    form1           = models.CharField(
        verbose_name="種類",
        choices=KIND_CHOICES,
        max_length=16,
        default='BF'
        
    )
    FOOD_CHOICES=tuple([(x,x)for x in range(0,11)])
    form2           = models.IntegerField(
        verbose_name="主食量",
        default=10,
        choices=FOOD_CHOICES,
    )
    form3           = models.IntegerField(
        verbose_name="副食量",
        default=10,
        choices=FOOD_CHOICES,
    )
    def __str__(self):
        return "食事記録"






