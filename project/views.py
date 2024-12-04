from django.shortcuts import render
from django.views.generic import TemplateView
from project.models import Project
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from manager.models import Customer, Salesman, TechnicalLead

# Create your views here.
class Home(TemplateView):
    model = Project
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        project_list = Project.objects.filter(status="active")
        customer_list = Customer.objects.all()
        salesman_list = Salesman.objects.all()
        technicallead_list = TechnicalLead.objects.all()

        context['projects'] = project_list
        context['customers'] = customer_list
        context['salesmen'] = salesman_list
        context['technicalleads'] = technicallead_list

        return context

@csrf_exempt
def ajax_get_project(request):
    project_id = request.GET.get('project_id')
    try:
        project = Project.objects.get(id=project_id)
        project_data = {
            'id': project.id,
            'project_name': project.project_name,
            'customer_id': project.customer.id,
            'site': project.site,
            'salesman_id': project.salesman.id,
            'technical_lead_id': project.technical_lead.id,
            'start_date': project.start_date.strftime('%Y-%m-%d'),
            'end_date': project.end_date.strftime('%Y-%m-%d')
        }
        return JsonResponse({'success': True, 'project': project_data})
    except Project.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Project not found.'})
    
@csrf_exempt
def ajax_update_project(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        try:
            project = Project.objects.get(id=project_id)

            # Update project details
            project.project_name = request.POST.get('project_name')
            project.customer_id = request.POST.get('customer')
            project.site = request.POST.get('site')
            project.salesman_id = request.POST.get('salesman')
            project.technical_lead_id = request.POST.get('techLead')
            project.start_date = request.POST.get('start_date')
            project.end_date = request.POST.get('end_date')

            # Handle file update
            if 'file' in request.FILES:
                project.file = request.FILES['file']

            # Save the updated project
            project.save()

            return JsonResponse({'success': True, 'message': 'Project updated successfully!'})
        except Project.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Project not found.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
@csrf_exempt
def ajax_update_status_project(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        try:
            project = Project.objects.get(id=project_id)
            project.status = 'archived'
            project.save()
            return JsonResponse({'success': True})
        except Project.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Project not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


@csrf_exempt
def ajax_create_project(request):
    if request.method == 'POST':
        obj = Project(
            project_name=request.POST.get('project_name'),
            customer_id=request.POST.get('customer'),
            salesman_id=request.POST.get('salesman'),
            technical_lead_id=request.POST.get('techLead'),
            site=request.POST.get('site'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date'),
            file = request.FILES.get('file'),
        )

        obj.save()

        return JsonResponse({'success': True})

