from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, View, UpdateView
from.models import *
from .forms import *
from django_summernote.widgets import SummernoteWidget


class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = "main/article_detail.html"


class ArticleCreate(View):
    def get(self, request):
        form = ArticleCreateForm()
        return render(request, "main/form_view.html", {'form':form})

    def post(self, request):
        form = ArticleCreateForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            id = article.id
            return redirect('detail', pk=id)
        return render(request, "main/form_view.html", {'form': form})


# class UpdateArcticle(View):
#     def get(self, request, id):
#         article = Article.objects.get(id=id)
#         form = ArticleCreateForm(instance=article)
#         return render(request, "main/form_view.html", {'form':form})
#
#     def post(self, request, id):
#         form = ArticleCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             article = form.save()
#             id = article.id
#             return redirect('detail', pk=id)
#         return render(request, "main/form_view.html", {'form': form})

class UpdateArcticle(UpdateView):
    model = Article
    fields = ['text', 'docfile']
    template_name = 'main/form_view.html'
    form_class = ArticleCreateForm

    def get_form(self):
        pk = self.kwargs["pk"]
        form = super(UpdateArcticle, self).get_form(self.form_class)
        form.fields['text'].widget = SummernoteWidget()
        return form

    def get_success_url(self):
        return reverse('detail', args=[self.kwargs['pk']])
