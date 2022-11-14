from django.db import models


class Visitor(models.Model):
    """
    Create Table "Visitors database(Postgresql)"
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=True, null=False)
    last_name = models.CharField(max_length=150, blank=True, null=False)
    email = models.CharField(max_length=200, blank=True, null=False)
    create_at = models.DateTimeField(auto_created=True)

    def __repr__(self):
        return f'<Visitor {self.first_name} {self.last_name}>'
