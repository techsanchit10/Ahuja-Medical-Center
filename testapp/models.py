from django.db import models
from django.core.urlresolvers import reverse


class Package(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'package'
        verbose_name_plural = 'packages'
#there is a way in Django, you can explicitly declare what the
#singular form of the database objects should be and what the
# plural form of the database objects should be. And this can
# be done by using verbose_name and verbose_name_plural attributes.
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('testapp:test_list_by_package', args=[self.slug])


class Test(models.Model):
    package = models.ForeignKey(Package, related_name='tests')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('testapp:test_detail', args=[self.id, self.slug])
