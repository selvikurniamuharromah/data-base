from pickle import TRUE
from django.db import models

# Create your models here.
class STAF(models.Model):
    NIP = models.CharField(max_length=50)
    NAMA = models.CharField(max_length=40)
    TTL = models.CharField(max_length=40)
    PHOTO = models.CharField(max_length=40)
    EMAIL = models.CharField(max_length=40)
    UNIT = models.CharField(max_length=40)
    ALAMAT = models.CharField(max_length=40)

    def __str__(self):
        return self.NIP

class MAHASISWA(models.Model):
    NIM = models.CharField(max_length=50)
    NAMA = models.CharField(max_length=40)
    TTL = models.CharField(max_length=40)
    PHOTO = models.CharField(max_length=40)
    EMAIL = models.CharField(max_length=40)
    FAKULTAS = models.CharField(max_length=40)
    PRODI = models.CharField(max_length=40)

    def __str__(self):
        return self.NIP


class DOSEN(models.Model):
    NIP = models.CharField(max_length=50)
    NAMA = models.CharField(max_length=40)
    TTL = models.CharField(max_length=40)
    PHOTO = models.CharField(max_length=40)
    EMAIL = models.CharField(max_length=40)
    FAKULTAS = models.CharField(max_length=40)
    PRODI = models.CharField(max_length=40)
    ALAMAT = models.CharField(max_length=40)
    STAF_id = models.ForeignKey(STAF, on_delete=models.CASCADE, null=True)
    MAHASISWA_id = models.ForeignKey(MAHASISWA, on_delete=models.CASCADE, null=True)
    STAF_id = models.ForeignKey(
    STAF,
    on_delete=models.DO_NOTHING,
    related_name='re_STAF_id',  # Here
    db_column='STAF_id',
    null=True
)

    MAHASISWA_id = models.ForeignKey(
    MAHASISWA,
    on_delete=models.DO_NOTHING,
    related_name='re_MAHASISWA_id',  # Here
    db_column='MAHASISWA_id',
    null=True
)

    def __str__(self):
        return self.NIP