# -*- coding: utf-8 -*-
import json
import time
import base64

from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import F
from django.contrib.auth.decorators import login_required

from core import resource
from core.jsonresponse import create_response
import nav
import models
from resource import models as resource_models
from util import string_util
from business.project.b_project_repository import BProjectRepository

FIRST_NAV = 'project'

class StaredProject(resource.Resource):
	app = 'project'
	resource = 'stared_project'

	@login_required
	def api_put(request):
		project_id = request.POST['id']
		b_project = BProjectRepository.get().get_project_by_id(project_id)
		b_project.star_by_user(request.user)

		response = create_response(200)
		return response.get_response()


	@login_required
	def api_delete(request):
		project_id = request.POST['id']
		b_project = BProjectRepository.get().get_project_by_id(project_id)
		b_project.unstar_by_user(request.user)

		response = create_response(200)
		return response.get_response()