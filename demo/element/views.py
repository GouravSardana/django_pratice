from django.shortcuts import render
from django.views.generic import TemplateView
from element.models import Slider, Features, Banner, FirstFeature


class About(TemplateView):
	template_name='element/index.html'
	# model=Slider, Features
	model=Features, Banner, FirstFeature
	def get(self,request,*args,**kwargs):
		features=Features.objects.all()
		slider=Slider.objects.all();
		banner=Banner.objects.all();
		firstFeature=FirstFeature.objects.all();
		print(slider);
		return render(request,'element/index.html',{'f':features,'slider':slider, 'b':banner, 'ff':firstFeature})
	# def get_queryset(self):  #object jo return karega
	# 	print(Features.objects.all())
	# 	return Features.objects.all()


class About1(TemplateView):
	template_name='element/left-sidebar.html'
class About2(TemplateView):
	template_name='element/right-sidebar.html'
class About3(TemplateView):
	template_name='element/no-sidebar.html'

