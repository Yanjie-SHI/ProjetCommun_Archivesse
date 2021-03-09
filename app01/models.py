from django.db import models


class Users(models.Model):
    id = models.AutoField(db_column='u_id', primary_key=True, help_text="使用者的id（由系统随机生成）")
    mail = models.CharField(db_column='u_mailaddress', max_length=100, unique=True, blank=False, null=False,
                            help_text="使用者的邮箱")
    first_name = models.CharField(db_column='u_firstname', max_length=64, blank=True, null=True, help_text="使用者的姓")
    last_name = models.CharField(db_column='u_lastname', max_length=64, blank=True, null=True, help_text="使用者的名")
    username = models.CharField(db_column='u_username', max_length=128, blank=True, null=True,
                                help_text="使用者的用户名(名首字母大写+姓全大写,例子：Yanjie SHI)")
    password = models.CharField(db_column='u_password', max_length=32, blank=True, null=True, help_text="使用者的密码")
    gender = models.IntegerField(db_column='u_sex', blank=True, null=True, help_text="使用者的性别(1:male 2:female)")
    nation = models.CharField(db_column='u_country', max_length=64, blank=True, null=True, help_text="使用者的所在国家")
    city = models.CharField(db_column='u_city', max_length=64, blank=True, null=True, help_text="使用者的所在城市")
    address = models.CharField(db_column='u_address', max_length=500, blank=True, null=True, help_text="使用者的住址")
    post_code = models.IntegerField(db_column='u_zipcode', blank=True, null=True, help_text="使用者的邮编")

    class Meta:
        managed = True
        db_table = 'Users'


class Museum(models.Model):
    id = models.AutoField(db_column='m_id', primary_key=True, help_text="文献馆ID")
    name = models.CharField(db_column='m_name', max_length=200, blank=False, null=False, help_text="文献馆的名字")
    city = models.CharField(db_column='m_city', max_length=32, blank=False, null=False, help_text="文献馆所在的城市")
    address = models.CharField(db_column='m_address', max_length=500, blank=False, null=False, help_text="文献馆所在的地址")
    post_code = models.IntegerField(db_column='m_zipcode', blank=True, null=True, help_text="文献馆所在的地址的邮编")
    tel = models.CharField(db_column='m_tel', max_length=20, blank=True, null=True, help_text="文献馆的联系电话")
    mail = models.CharField(db_column='m_mail', max_length=100, blank=True, null=True, help_text="文献馆的联系邮箱")
    document_limit = models.IntegerField(db_column='m_nbdocumentlimit', blank=True, null=True,
                                         help_text="文献馆每个人一次能查看的文字档案数量")
    video_limit = models.IntegerField(db_column='m_nbvideolimit', blank=True, null=True,
                                      help_text="文献馆每个人一次能查看的视频档案数量")

    class Meta:
        managed = True
        db_table = 'Museum'


class Archive(models.Model):
    id = models.CharField(db_column='a_id', primary_key=True, max_length=32, help_text="文献编号")
    title = models.CharField(db_column='a_title', max_length=200, blank=False, null=False, help_text="文献标题")
    type = models.IntegerField(db_column='a_type', blank=False, null=False,
                               help_text="文献类型(1:Document physique 2:Document numérisé 3:Audio-visuelle(三选一)")
    folio = models.IntegerField(db_column="a_folio", blank=True, null=True, help_text="文献的页数(有些馆藏的文献只有部分页)")
    language = models.CharField(db_column="a_language", max_length=100, blank=False, null=False, help_text="文献的语言")
    author = models.CharField(db_column='a_author', max_length=200, blank=False, null=False)
    description = models.CharField(db_column='a_description', max_length=2000, blank=True, null=True)

    museum = models.ForeignKey(Museum, db_index=True, on_delete=models.DO_NOTHING, help_text="用于获取文献馆的地址: 地址+邮编+城市")

    class Meta:
        managed = True
        db_table = 'Archive'


class Reservation(models.Model):
    id = models.AutoField(db_column='r_id', primary_key=True, help_text="预约号码(随机生成的一个13位的数字，不能重复)")
    expire_date = models.DateField(db_column='r_enddate', blank=False, null=False, help_text="本次预约的时间结束日期")
    status = models.IntegerField(db_column='r_status', blank=False, null=False,
                                 help_text="本次预约的状态 0:Pas encore aller; 1:suis allé")
    sent_flag = models.IntegerField(db_column='r_providerhassent', blank=False, null=False,
                                    help_text="提供者是否已把需求者要求的文献照片发送给需求者 0否1是")
    received_flag = models.IntegerField(db_column='r_demanderhasreceived', blank=False, null=False,
                                        help_text="需求者是否已确认收到提供者发送的文献 0否1是")

    museum = models.ForeignKey(Museum, db_index=True, on_delete=models.DO_NOTHING, help_text="关联获取该馆可预约数，计算剩余可用预约数")
    creator = models.ForeignKey(Users, db_index=True, on_delete=models.DO_NOTHING, help_text="创建预约的用户")

    class Meta:
        managed = True
        db_table = 'Reservation'


'''
预约-用户-文献关系：一个预约可以有多个人参与，一个人可以预约多本文献，预约总文献数控制着多少人和多少文献
'''


class Res_Dem_Arch(models.Model):
    rad_id = models.AutoField(db_column="rad_id", primary_key=True, help_text="自增长id")
    reservation = models.ForeignKey(Reservation, db_index=True, on_delete=models.DO_NOTHING, help_text="预约号")
    resv_user = models.ForeignKey(Users, db_index=True, on_delete=models.DO_NOTHING, help_text="预约的用户编号")
    archive = models.ForeignKey(Archive, db_index=True, on_delete=models.DO_NOTHING, help_text="文献编号")

    class Meta:
        managed = True
        db_table = 'Res_Dem_Arch'


class Notification(models.Model):
    id = models.AutoField(db_column="n_id", primary_key=True, help_text="通知id")
    category = models.IntegerField(db_column="n_category", blank=False, null=False,
                                   help_text="通知分类：0 = Admin,1= Reservation,2 = Demande")
    title = models.CharField(db_column="n_title", max_length=200, blank=False, null=False, help_text="通知标题")
    content = models.CharField(db_column="n_content", max_length=2000, blank=False, null=False, help_text="通知内容")
    status = models.IntegerField(db_column="n_status", blank=False, null=False, help_text="通知状态 0未读1已读")
    receiver = models.ForeignKey(Users, db_index=True, on_delete=models.DO_NOTHING, help_text="通知接收人")

    class Meta:
        managed = True
        db_table = 'Notification'


class Demand(models.Model):
    id = models.AutoField(db_column="d_id", primary_key=True, help_text="需求id")
    create_date = models.DateField(db_column="d_date", blank=False, null=False, help_text="需求创建日期")
    status = models.IntegerField(db_column="d_status", blank=False, null=False, help_text="需求状态 0未完成1已完成")
    demander = models.ForeignKey(Users, db_index=True, on_delete=models.DO_NOTHING, help_text="需求发布的人")
    archive = models.ForeignKey(Archive, db_index=True, on_delete=models.DO_NOTHING, help_text="该需求关联的文献id")

    class Meta:
        managed = True
        db_table = 'Demand'


class Favorites(models.Model):
    id = models.AutoField(db_column="f_id", primary_key=True, help_text="收藏id")
    user = models.ForeignKey(Users, db_index=True, on_delete=models.DO_NOTHING, help_text="收藏者id")
    archive = models.ForeignKey(Archive, db_index=True, on_delete=models.DO_NOTHING, help_text="被收藏的文献id")

    class Meta:
        managed = True
        db_table = 'Favorite'
