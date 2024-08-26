from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models, forms


class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.InFlow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflows.view_inflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset


class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.InFlow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflows.add_inflow'


class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.InFlow
    template_name = 'inflow_detail.html'
    permission_required = 'inflows.view_inflow'
