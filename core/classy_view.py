from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.forms import PostAddModelForm


class PostAddView(LoginRequiredMixin, CreateView):
    form_class = PostAddModelForm
    template_name = 'post_add.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            post = form.save(commit=False)
            profile = request.user.profile
            post.profile = profile
            post.save()

            return redirect('main')
        else:
            return self.form_invalid(form)

