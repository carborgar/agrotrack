from django.views.generic import ListView

from .models import Field
from .models import Product
from .models import Task


class FieldListView(ListView):
    model = Field
    template_name = "fields/field_list.html"
    context_object_name = "fields"

    def get_queryset(self):
        return Field.objects.all()


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()

        field_ids = self.request.GET.getlist('field')
        type_filters = self.request.GET.getlist('type')
        status_filters = self.request.GET.getlist('status')
        product_ids = self.request.GET.getlist('products')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')

        if field_ids:
            queryset = queryset.filter(field__id__in=field_ids)
        if type_filters:
            queryset = queryset.filter(type__in=type_filters)
        if product_ids:
            queryset = queryset.filter(products__id__in=product_ids)
        if date_from:
            queryset = queryset.filter(date__gte=date_from)  # Filtra por fecha desde
        if date_to:
            queryset = queryset.filter(date__lte=date_to)

        # Filtrado por múltiples estados
        if status_filters:
            queryset = [task for task in queryset if task.status() in status_filters]

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = Field.objects.all()
        context['products'] = Product.objects.all()
        context['type_choices'] = Task.TYPE_CHOICES
        context['status_choices'] = Task.STATUS_CHOICES
        context['selected_fields'] = self.request.GET.getlist('field')
        context['selected_types'] = self.request.GET.getlist('type')
        context['selected_statuses'] = self.request.GET.getlist('status')
        context['selected_products'] = self.request.GET.getlist('products')
        context['date_from'] = self.request.GET.get('date_from')
        context['date_to'] = self.request.GET.get('date_to')
        return context
