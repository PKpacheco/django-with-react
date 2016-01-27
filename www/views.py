import os

from django.shortcuts import render, HttpResponse
from django.conf import settings

from react.render import render_component

def home(request):
	rendered = render_component(
		os.path.join(os.getcwd(), 'www', 'static', 'www', 'index.jsx'),
        {},
        to_static_markup=True,
    )

	return HttpResponse(rendered)
