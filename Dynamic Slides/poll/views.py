from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from poll.models import Form
from django.urls import reverse_lazy

@method_decorator(login_required, name='dispatch')
class AboutView(TemplateView):
	template_name='index.html'



# class Publisher(ListView):
# 	model=Form   #model ka naam
# 	template_name='form_list.html'  #file ka naam or model ka naam same hote hai
#
#
# 	def get_queryset(self):  #object jo return karega
#
# 		return Form.objects.all()
# #niche wala method not working solved by harshit sir
# 	# def get_context_data(self, **kwargs):
# 	# 	context=super().get_context_data(**kwargs)
# 	# 	return context
# 	#*args == bahut sare argument pass karne ho uske liye hote hai
# 	#**kwargs == pass the dictionary
# class Author(CreateView):
# 	model=Form
# 	fields=['email', 'password']
# 	success_url = reverse_lazy('view')
#
# class Author2(UpdateView):
# 	model=Form
# 	fields=['email', 'password']
# 	success_url = reverse_lazy('view')
#
# class Author3(DeleteView):
# 	model=Form
# 	success_url= reverse_lazy('view')