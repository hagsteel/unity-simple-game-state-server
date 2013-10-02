from django.db import models


class GameState(models.Model):
    key = models.CharField(max_length=30)
    pos_x = models.FloatField(null=True)
    pos_y = models.FloatField(null=True)
    pos_z = models.FloatField(null=True)

    def __unicode__(self):
        return 'x:%s - y:%s - z:%s' % (self.pos_x, self.pos_y, self.pos_z)
