from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from servicecall.models import ServiceCall
from project.models import Project
from product.models import Product
from manager.models import TechnicalLead
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date

# Create your views here.
class ServiceCallView(TemplateView):
    model = ServiceCall
    template_name = "service_call.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        techlead_list = TechnicalLead.objects.all()
        project_list = Project.objects.filter(status="active")
        product_list = Product.objects.all()
        maintenance_calls = ServiceCall.objects.all()
    
        # Data for pie chart
        chart_data = {
            'labels': ['Pending', 'In Progress', 'Done'],
            'data': [
                maintenance_calls.filter(status='pending').count(),
                maintenance_calls.filter(status='in_progress').count(),
                maintenance_calls.filter(status='done').count(),
            ]
        }
        context['techleads'] = techlead_list
        context['projects'] = project_list
        context['products'] = product_list
        context['maintenance_calls'] = maintenance_calls
        context['chart_data'] = chart_data

        return context
    
@csrf_exempt
def ajax_create_service_call(request):
    if request.method == 'POST':
        project_id = request.POST.get('project')
        product = request.POST.get('product')
        techLead = request.POST.get('techLead')
        problem_description = request.POST.get('problem_description')
        category = request.POST.get('category')
        status = request.POST.get('status')
        solution_description = request.POST.get('solution_description')

        # Fetch the project and create a new ServiceCall
        project = Project.objects.get(id=project_id)
        closing_date = date.today() if status == 'done' else None

        service_call = ServiceCall.objects.create(
            project=project,
            product_id=product,
            description=problem_description,
            category=category,
            status=status,
            solution_description=solution_description,
            opening_date=date.today(),
            closing_date=closing_date,  # Set closing date if status is 'done'
            technical_lead_id=techLead
        )

        # Update the chart data by fetching current service calls
        maintenance_calls = ServiceCall.objects.all()

        updated_chart_data = {
            'labels': ['Pending', 'In Progress', 'Done'],
            'data': [
                maintenance_calls.filter(status='pending').count(),
                maintenance_calls.filter(status='in_progress').count(),
                maintenance_calls.filter(status='done').count(),
            ]
        }

        # Return the response data as JSON to update the table
        return JsonResponse({
            'success': True,
            'project_name': project.project_name,
            'call_number': service_call.id,
            'description': service_call.description,
            'category': service_call.category,
            'tech_lead': service_call.technical_lead.first_name,  # Add logic to pull tech lead if needed
            'solution_description': service_call.solution_description,
            'status': service_call.status,
            'chart_data': updated_chart_data  # Chart data for updating the chart dynamically
        })
    
    return JsonResponse({'success': False}, status=400)