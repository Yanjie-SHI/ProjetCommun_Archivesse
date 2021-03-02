# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Utilisateur(models.Model):
    u_id = models.AutoField(db_column='U_Id', primary_key=True)  # Field name made lowercase.
    u_nom = models.CharField(db_column='U_Nom', max_length=64, blank=True, null=True)  # Field name made lowercase.
    u_prénom = models.CharField(db_column='U_Prénom', max_length=64, blank=True,
                                null=True)  # Field name made lowercase.
    u_mail = models.CharField(db_column='U_Mail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    u_mdp = models.CharField(db_column='U_Mdp', max_length=32, blank=True, null=True)  # Field name made lowercase.
    u_pseudo = models.CharField(db_column='U_Pseudo', max_length=128, blank=True,
                                null=True)  # Field name made lowercase.
    u_pays = models.CharField(db_column='U_Pays', max_length=64, blank=True, null=True)  # Field name made lowercase.
    u_cp = models.IntegerField(db_column='U_CP', blank=True, null=True)  # Field name made lowercase.
    u_ville = models.CharField(db_column='U_Ville', max_length=64, blank=True, null=True)  # Field name made lowercase.
    u_adresse = models.CharField(db_column='U_Adresse', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Utilisateur'


class Archive(models.Model):
    a_coderéférence = models.CharField(db_column='A_CodeRéférence', primary_key=True,
                                       max_length=32)  # Field name made lowercase.
    a_titre = models.CharField(db_column='A_Titre', max_length=128, blank=True, null=True)  # Field name made lowercase.
    a_type = models.CharField(db_column='A_Type', max_length=16, blank=True, null=True)  # Field name made lowercase.
    a_producteur = models.CharField(db_column='A_Producteur', max_length=64, blank=True,
                                    null=True)  # Field name made lowercase.
    a_uploader_id = models.IntegerField(db_column='A_Uploader_Id', blank=True, null=True)  # Field name made lowercase.
    a_musée_id = models.IntegerField(db_column='A_Musée_id', blank=True, null=True)  # Field name made lowercase.
    a_état = models.CharField(db_column='A_État', max_length=1, blank=True, null=True)  # Field name made lowercase.
    a_canbedownload = models.CharField(db_column='A_canBeDownload', max_length=1, blank=True,
                                       null=True)  # Field name made lowercase.
    a_description = models.CharField(db_column='A_description', max_length=2000, blank=True,
                                     null=True)  # Field name made lowercase.
    a_routetélécharger = models.CharField(db_column='A_routeTélécharger', max_length=500, blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Archive'


class Museum(models.Model):
    m_id = models.IntegerField(db_column='M_ID', primary_key=True)  # Field name made lowercase.
    m_nom = models.CharField(db_column='M_Nom', max_length=32, blank=True, null=True)  # Field name made lowercase.
    m_ville = models.CharField(db_column='M_Ville', max_length=32, blank=True, null=True)  # Field name made lowercase.
    m_cp = models.IntegerField(db_column='M_CP', blank=True, null=True)  # Field name made lowercase.
    m_adresse = models.CharField(db_column='M_Adresse', max_length=500, blank=True,
                                 null=True)  # Field name made lowercase.
    m_tel = models.IntegerField(db_column='M_Tel', blank=True, null=True)  # Field name made lowercase.
    m_mail = models.CharField(db_column='M_Mail', max_length=64, blank=True, null=True)  # Field name made lowercase.
    m_nbdocumentlimit = models.IntegerField(db_column='M_nbDocumentLimit', blank=True,
                                            null=True)  # Field name made lowercase.
    m_nbvideolimit = models.IntegerField(db_column='M_nbVideoLimit', blank=True,
                                         null=True)  # Field name made lowercase.
    m_tempsouvert = models.CharField(db_column='M_TempsOuvert', max_length=64, blank=True,
                                     null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Museum'


class Reservation(models.Model):
    r_id = models.IntegerField(db_column='R_Id', primary_key=True)  # Field name made lowercase.
    r_date = models.DateField(db_column='R_Date', blank=True, null=True)  # Field name made lowercase.
    r_musée_id = models.IntegerField(db_column='R_Musée_id', blank=True, null=True)  # Field name made lowercase.
    r_donneur_id = models.IntegerField(db_column='R_Donneur_id', blank=True, null=True)  # Field name made lowercase.
    r_demandeur_id = models.IntegerField(db_column='R_Demandeur_id', blank=True,
                                         null=True)  # Field name made lowercase.
    r_nbdemanddocument = models.IntegerField(db_column='R_nbDemandDocument', blank=True,
                                             null=True)  # Field name made lowercase.
    r_nbdemandvideo = models.IntegerField(db_column='R_nbDemandVideo', blank=True,
                                          null=True)  # Field name made lowercase.
    r_étatdocument = models.IntegerField(db_column='R_ÉtatDocument', blank=True,
                                         null=True)  # Field name made lowercase.
    r_étatvideo = models.IntegerField(db_column='R_ÉtatVideo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reservation'
