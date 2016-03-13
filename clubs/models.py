from django.db import models


class Manager(models.Model):
    # club = models.ForeignKey(Club)
    name = models.CharField(primary_key=True, max_length=30)
    # height = models.IntegerField(default=170)
    # date_of_birth =  models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.name



# Create your models here.
class Club(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    city = models.CharField( max_length=30)
    arena = models.CharField( max_length=30)
    manager = models.ForeignKey(Manager)

    def __str__(self):
        return self.name
    #
    # def get_players(self):
    #     players = Player.objects.filter(club=self)
    #     return players


class Player(models.Model):
    club = models.ForeignKey(Club,related_name='players')
    number = models.IntegerField(default=170)
    name = models.CharField(primary_key=True, max_length=30)
    position = models.CharField(max_length=30)
    height = models.IntegerField(default=170)
    age =  models.IntegerField(default=170)

    previous_clubs = models.ManyToManyField(Club, through='PreviousClubs',related_name='playerspreviousclubs')

    def __str__(self):
        return self.name

    # def get_previous_clubs(self):
    #     previous_clubs = (PreviousClubs.objects.filter(player=self))
    #     return previous_clubs


#
class PreviousClubs(models.Model):
    player = models.ForeignKey(Player)
    club = models.ForeignKey(Club)

    def __str__(self):
        return self.player.name