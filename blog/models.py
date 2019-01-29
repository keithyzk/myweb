from django.db import models

# Create your models here.
class Ariticle(models.Model):
    title = models.CharField(max_length=32, default='title')
    content = models.TextField(null=True)

class mysql_list(models.Model):
    ip = models.GenericIPAddressField()
    typeTu = (
        (1, '主库'),
        (2, '从库')
    )
    mysqltype = models.SmallIntegerField('数据库类型', choices=typeTu)
    username = models.CharField('帐号', default='', max_length=64)
    password = models.CharField('密码', default='', max_length=64)
    port = models.IntegerField('端口号', default=3306)
    master_ip = models.GenericIPAddressField(default='', null=True, blank=True)
    master_port = models.IntegerField('主库端口号', null=True, blank=True)

class mysql_user_list(models.Model):
    id = models.IntegerField(primary_key=True)
    db_id = models.ForeignKey(mysql_list)
    userlist = models.TextField('用户列表',blank=True,null=True)


    def __unicode__(self):
        return self.title