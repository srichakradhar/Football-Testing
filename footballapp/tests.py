from django.test import TestCase
from django.http import HttpRequest
from django.test import Client
from django.urls import reverse

from . import views
from .models import Team, Players, AdminProfile, Mappings
from difflib import SequenceMatcher
import json
from django.contrib.auth.hashers import check_password, make_password

# Put your code here.
# Write unit test cases to get maximum coverage.