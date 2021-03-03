from django.db import models


class Users(models.Model):
    u_id = models.AutoField(db_column='u_id', primary_key=True, help_text="使用者的id（由系统随机生成）")
    u_mail = models.CharField(db_column='u_mail', max_length=100, unique=True, blank=False, null=False,
                              help_text="使用者的邮箱")
    u_first_name = models.CharField(db_column='u_first_name', max_length=64, blank=True, null=True, help_text="使用者的姓")
    u_last_name = models.CharField(db_column='u_last_name', max_length=64, blank=True, null=True, help_text="使用者的名")
    u_username = models.CharField(db_column='u_username', max_length=128, blank=True, null=True,
                                  help_text="使用者的用户名(名首字母大写+姓全大写,例子：Yanjie SHI)")
    u_password = models.CharField(db_column='u_password', max_length=32, blank=True, null=True, help_text="使用者的密码")
    u_nation = models.CharField(db_column='u_nation', max_length=64, blank=True, null=True, help_text="使用者的所在国家")
    u_city = models.CharField(db_column='u_city', max_length=64, blank=True, null=True, help_text="使用者的所在城市")
    u_address = models.CharField(db_column='u_address', max_length=500, blank=True, null=True, help_text="使用者的住址")
    u_post_code = models.IntegerField(db_column='u_post_code', blank=True, null=True, help_text="使用者的邮编")

    class Meta:
        managed = True
        db_table = 'Users'


class Museum(models.Model):
    m_id = models.IntegerField(db_column='m_id', primary_key=True, help_text="文献馆ID")
    m_name = models.CharField(db_column='m_name', max_length=32, blank=False, null=False, help_text="文献馆的名字")
    m_city = models.CharField(db_column='m_city', max_length=32, blank=False, null=False, help_text="文献馆所在的城市")
    m_address = models.CharField(db_column='m_address', max_length=500, blank=False, null=False, help_text="文献馆所在的地址")
    m_post_code = models.IntegerField(db_column='m_post_code', blank=True, null=True, help_text="文献馆所在的地址的邮编")
    m_tel = models.IntegerField(db_column='m_tel', blank=True, null=True, help_text="文献馆的联系电话")
    m_mail = models.CharField(db_column='m_mail', max_length=100, blank=True, null=True, help_text="文献馆的联系邮箱")
    m_document_limit = models.IntegerField(db_column='m_document_limit', blank=True, null=True,
                                           help_text="文献馆每个人一次能查看的文字档案数量")
    m_video_limit = models.IntegerField(db_column='m_video_limit', blank=True, null=True,
                                        help_text="文献馆每个人一次能查看的视频档案数量")

    class Meta:
        managed = True
        db_table = 'Museum'


class Archive(models.Model):
    a_code_reference = models.CharField(db_column='a_code_reference', primary_key=True, max_length=32, help_text="文献编号")
    a_title = models.CharField(db_column='a_title', max_length=200, blank=False, null=False, help_text="文献标题")
    a_type = models.IntegerField(db_column='a_type', blank=False, null=False,
                                 help_text="文献类型(1:Document physique 2:Document numérisé 3:Audio-visuelle(三选一)")
    a_author = models.CharField(db_column='a_author', max_length=100, blank=False, null=False)
    a_description = models.CharField(db_column='a_description', max_length=2000, blank=True, null=True)

    a_museum = models.ForeignKey(Museum, db_index=True, on_delete=models.DO_NOTHING, help_text="用于获取文献馆的地址: 地址+邮编+城市")

    class Meta:
        managed = True
        db_table = 'Archive'


class Reservation(models.Model):
    r_id = models.IntegerField(db_column='r_id', primary_key=True, help_text="预约号码(随机生成的一个13位的数字，不能重复)")
    r_date_start = models.DateField(db_column='r_date_start', blank=False, null=False, help_text="本次预约的时间起始日期")
    r_date_end = models.DateField(db_column='r_date_end', blank=False, null=False, help_text="本次预约的时间结束日期")
    r_museum = models.ForeignKey(Museum, db_index=True, on_delete=models.DO_NOTHING, help_text="关联获取该馆可预约数，计算剩余可用预约数")
    r_creator = models.ForeignKey(Users, db_index=True, on_delete=models.DO_NOTHING, help_text="创建预约的用户")

    class Meta:
        managed = True
        db_table = 'Reservation'


'''
预约-用户-文献关系：一个预约可以有多个人参与，一个人可以预约多本文献，预约总文献数控制着多少人和多少文献
'''


class Res_Dem_Arch(models.Model):
    r_id = models.ForeignKey(Reservation, db_index=True, on_delete=models.DO_NOTHING, help_text="预约号")
    u_id = models.ForeignKey(Users, db_index=True, on_delete=models.DO_NOTHING, help_text="预约的用户编号")
    a_code_reference = models.ForeignKey(Archive, db_index=True, on_delete=models.DO_NOTHING, help_text="文献编号")

    class Meta:
        managed = True
        db_table = 'Res_Dem_Arch'
