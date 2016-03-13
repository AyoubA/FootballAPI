from django.contrib.auth.models import User, Group
from rest_framework import serializers
from clubs.models import Club, Manager, Player, PreviousClubs


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')


class PreviousClubsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PreviousClubs
        fields = ('url', 'id', 'club', 'player')



class PlayerSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Player
        fields = ('url', 'number', 'name', 'position', 'height', 'age', 'club','previous_clubs')





class ClubSerializer(serializers.HyperlinkedModelSerializer):
    # players = PlayerSerializer(
    #     source='get_players',
    #     read_only=True
    # )

    players= serializers.StringRelatedField(many=True)

    class Meta:
        model = Club

        fields = ('url', 'name', 'city', 'arena', 'manager', 'players')






class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ('url', 'name')







