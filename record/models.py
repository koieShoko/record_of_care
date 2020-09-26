from django.conf import settings
from django.db import models
from django.utils import timezone
from account.models import User



class Resident(models.Model):
    full_name          = models.CharField(
        verbose_name   = "名前",
        max_length     = 128)
    kana_full_name     = models.CharField(verbose_name="ふりがな",max_length=128)
    DEPARTMENT_CHOICES = (#(保存する値,表示)
        ("1","1階"),
        ("2","2階"),
        ("3","3階"),
        ("4","4階"),
        ("5","5階"),
        ("6","6階"),
    )
    birthday         = models.DateField(
        verbose_name ="生年月日"
    )
    department       = models.CharField(
        verbose_name ="部署",
        default      = "1",
        max_length   = 128,
        choices      = DEPARTMENT_CHOICES,
    )
    UNIT_CHOICES     = (
        ('東','東'),
        ('西','西'),
    )
    unit             = models.CharField(
        verbose_name = "ユニット",
        default      = '東',
        max_length   = 1,
        choices      = UNIT_CHOICES,
    )
    room             = models.IntegerField(
        verbose_name = "部屋番号",
    )
    is_leaving       = models.BooleanField(
        verbose_name = '退所済',
        default      = False,
    )
    def register(self):
        self.save()
    def __str__(self):
        return self.full_name







class Category_form0(models.Model):
    category_name = models.CharField(
        verbose_name = "カテゴリ名",
        default = '',
        max_length = 50,
    )
    form1_name = models.CharField(
        verbose_name = "情報1の項目名",
        default = '',
        blank = True,
        max_length = 50,
    )
    form2_name = models.CharField(
        verbose_name = "情報2の項目名",
        default = '',
        blank = True,
        max_length = 50,
    )
    form3_name = models.CharField(
        verbose_name = "情報3の項目名",
        default = '',
        max_length = 50,
        blank = True,
    )
    def __str__(self):
        return self.category_name



class Category_form1(models.Model):
    category_name= models.CharField(
        verbose_name = "カテゴリ名",
        default = '',
        max_length = 50,
    )
    parent = models.ForeignKey(
        Category_form0,
        verbose_name   = "親カテゴリ",
        on_delete      = models.CASCADE,
        blank          = True, 
        null           = True
    )
    label = models.CharField(
        verbose_name = "項目名(あとから自動入力)",
        default = '',
        blank=True,
        null = True,
        max_length = 50,
    )
    def save(self):
        self.label = self.parent.form1_name
        super(Category_form1, self).save()
    def __str__(self):
        return self.category_name

class Category_form2(models.Model):
    category_name= models.CharField(
        verbose_name = "カテゴリ名",
        default = '',
        max_length = 50,
    )
    parent = models.ForeignKey(
        Category_form0,
        verbose_name   = "親カテゴリ",
        on_delete      = models.CASCADE,
        blank          = True, 
        null           = True
    )
    def __str__(self):
        return self.category_name

class Category_form3(models.Model):
    category_name= models.CharField(
        verbose_name = "カテゴリ名",
        default = '',
        max_length = 50,
    )
    parent = models.ForeignKey(
        Category_form0,
        verbose_name   = "親カテゴリ",
        on_delete      = models.CASCADE,
        blank          = True, 
        null           = True,
    )
    def __str__(self):
        return self.category_name











class Staff(User):
    full_name          = models.CharField(
        verbose_name   = "名前",
        max_length     = 128)
    kana_full_name     = models.CharField(verbose_name="ふりがな",max_length=128)
    DEPARTMENT_CHOICES = (#(保存する値,表示)
        ("1","1階"),
        ("2","2階"),
        ("3","3階"),
        ("4","4階"),
        ("5","5階"),
        ("6","6階"),
    )
    department         = models.CharField(
        verbose_name   = "部署",
        default        = "1",
        max_length     = 128,
        choices        = DEPARTMENT_CHOICES,
    )
    is_leaving         = models.BooleanField(
        verbose_name   = '退所済かどうか',
        default        = False,
    )
    CHOICE_OCCUPATION  = (
        ("CS","介護職"),
        ("NS","看護師"),
        ("Dr","医師"),
        ("PT","理学療法士"),
        ("OT","作業療法士"),
        ("ST","言語聴覚士"),
    )
    occupation         = models.CharField(
        verbose_name   = "職種",
        choices        = CHOICE_OCCUPATION,
        max_length     = 128,
        default        = "CS",
    )
    reading_support    = models.BooleanField(
        verbose_name   = "日本語サポート",
        default        = False,
    )
    def __str__(self):
        return self.full_name   

class Record(models.Model):
    resident           = models.ForeignKey(
        Resident,
        verbose_name   = "利用者",
        on_delete      = models.CASCADE,
        null           = True,
    )
    room               = models.IntegerField(
        verbose_name   = "利用者の部屋番号",
        default        = 0,
    )
    staff              = models.ForeignKey(
        Staff,
        verbose_name   = "職員",
        on_delete      = models.CASCADE,
        blank          = True, 
        null           = True
    )
    date               = models.DateField(
        verbose_name   = "日付",
        default        = timezone.now,
    )
    time               = models.TimeField(
        verbose_name   = "時刻",
        default        = "07:00"
    )
    notice             = models.CharField(
        verbose_name   = "特記事項",
        max_length     = 8000,
        default        = "",
        blank          = True
    )
    translated_notice  = models.CharField(
        verbose_name   = "変換結果",
        max_length     = 8000,
        default        = "",
        blank          = True,
    )
    ruby_translated_notice = models.CharField(
        verbose_name   = "変換結果",
        max_length     = 8000,
        default        = "",
        blank          = True,
        null           = True,
    )
    written_date       = models.DateTimeField(
        blank          = True, 
        null           = True
    )
    department         = models.CharField(
        verbose_name   = "部署",
        max_length     = 128,
    )
    unit               = models.CharField(
        verbose_name   = "ユニット",
        max_length     = 128,
    )
    isTranslated       = models.BooleanField(
        verbose_name   = "変換済みかどうか",
        default        = False,
    )
    CHOICE_KIND        = (
        ("食事", "食事"),
        ("入浴", "入浴"),
        ("生活", "生活"),
        ("医療", "医療"),
        ("夜間", "夜間"),
        ("リハビリ", "リハビリ"),
        ("家族連絡", "家族連絡"),
        ("事故", "事故"),
        ("その他", "その他"),
    )
    form0              = models.ForeignKey(
        Category_form0,
        verbose_name   = "親カテゴリ",
        on_delete      = models.CASCADE,
    )
    form1              = models.ForeignKey(
        Category_form1,
        verbose_name   = "情報1",
        on_delete      = models.CASCADE,
        blank          = True, 
        null           = True
    )
    form2              = models.ForeignKey(
        Category_form2,
        verbose_name   = "情報2",
        on_delete      = models.CASCADE,
        blank          = True, 
        null           = True
    )
    form3              = models.ForeignKey(
        Category_form3,
        verbose_name   = "情報3",
        on_delete      = models.CASCADE,
        blank          = True, 
        null           = True
    )
    def register(self):
        self.written_date  = timezone.now()
        self.department    = self.resident.department
        self.room          = self.resident.room
        self.unit          = self.resident.unit
        self.save()
    def __str__(self):
        return self.form0.category_name

