from rest_framework.response import Response
from rest_framework import views
from .models import GameState


class SaveGameView(views.APIView):
    def post(self, request, **kwargs):
        key = request.DATA['key']
        game_state, created = GameState.objects.get_or_create(key=key)
        game_state.pos_x = request.DATA['x']
        game_state.pos_y = request.DATA['y']
        game_state.pos_z = request.DATA['z']
        game_state.save()
        return Response(data={'response': 'OK'}, status=200)


class LoadGameView(views.APIView):
    def get(self, request, **kwargs):
        try:
            game_save = GameState.objects.get(key=request.GET['key'])
            return Response('%s|%s|%s' % (game_save.pos_x, game_save.pos_y, game_save.pos_z), status=200)
        except GameState.DoesNotExist:
            return Response(data={'message': 'no save game present'}, status=400)
