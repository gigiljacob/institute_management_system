from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            'page': 'blog'
        })
        return context
