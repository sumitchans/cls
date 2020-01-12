import datetime
import requests

from django.conf import settings
from rest_framework.exceptions import APIException

from .models import UserClass, User
from .serializers import *


def get_user(params, request):
    """
    Function to return user
    :param params:
    :param request:
    :return:
    """
    try:
        user = User.objects.get(username=params['username'], is_active=True)
        return user
    except Exception as ex:
        raise APIException(str(ex))


def user_login(params, request):
    """
    Function to user login
    :param params:
    :param request:
    :return:
    """
    user = get_user(params, request)
    auth = (settings.OAUTH_CLIENT_ID, settings.OAUTH_CLIENT_SECRET)
    login_data = {'username': user.username, 'password': params['password'], 'grant_type': 'password'}
    response = requests.post(settings.BASE_URL + '/o/token/', data=login_data, auth=auth)
    return response


def user_logout(request):
    """
        Logs out the user
        Params: access_token to be rendered invalid
    """
    try:
        data = dict()
        data['client_id'] = settings.OAUTH_CLIENT_ID
        data['client_secret'] = settings.OAUTH_CLIENT_SECRET
        data['token'] = request.META["HTTP_AUTHORIZATION"].split("Bearer ")[1]
        resp = requests.post(settings.BASE_URL + '/o/revoke_token/', data=data)
        return resp
    except Exception as ex:
        raise APIException(str(ex))


def get_user_class(request):
    """
    method to get user class
    :param request:
    :return:
    """
    try:
        user_class = UserClass.objects.filter(user_id=request.user)
        serializer = UserClassSerializer(user_class, many=True)
        return serializer.data
    except Exception as ex:
        raise APIException(str(ex))
