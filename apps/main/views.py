from django.shortcuts import render, redirect
from .forms import ConsultingForm, CalculatingProjectForm
from .models import SaveDbConsulting, SaveDbCalculating


def main(request):
    context = {}
    return render(request, "main.html", context)


def calculate_prj(request):
    if request.method == "POST":
        form = CalculatingProjectForm(request.POST)
        if form.is_valid():
            buyer_name = form.cleaned_data["buyer_name"]
            phone_number = form.cleaned_data["phone_number"]
            room_type = form.cleaned_data["room_type"]
            company_name = form.cleaned_data["company_name"]

            # Сохраняем данные в сессии для страницы успеха
            request.session['calculation_data'] = {
                'buyer_name': buyer_name,
                'phone_number': phone_number,
                'room_type': room_type,
                'company_name': company_name,
            }

            # Создаем объект и сохраняем его
            new_record = SaveDbCalculating(
                buyer_name=buyer_name,
                phone_number=phone_number,
                room_type=room_type,
                company_name=company_name
            )
            new_record.save()

            # Перенаправляем на страницу успеха
            return redirect('main:success_calculation')  # Исправлено имя URL
    else:
        form = CalculatingProjectForm()

    return render(request, "calculate_project.html", {'form': form})


def get_consult(request):
    if request.method == 'POST':
        form = ConsultingForm(request.POST)
        if form.is_valid():
            buyer_name = form.cleaned_data['buyer_name']
            phone_number = form.cleaned_data['phone_number']
            description = form.cleaned_data['description']

            # Сохраняем данные в сессии для страницы успеха
            request.session['consultation_data'] = {
                'buyer_name': buyer_name,
                'phone_number': phone_number,
                'description': description,
            }

            # Создаем объект и сохраняем
            new_record = SaveDbConsulting(
                buyer_name=buyer_name,
                phone_number=phone_number,
                description=description
            )
            new_record.save()

            # Перенаправляем на страницу успеха
            return redirect('main:success_consultation')  # Исправлено имя URL
    else:
        form = ConsultingForm()

    return render(request, "consultingform.html", {'form': form})


def success_consultation(request):
    # Получаем данные из сессии
    consultation_data = request.session.get('consultation_data', {})

    context = {
        'request_data': {
            'buyer_name': consultation_data.get('buyer_name', 'Client'),
            'phone_number': consultation_data.get('phone_number', ''),
            'description': consultation_data.get('description', ''),
        }
    }

    # Очищаем сессию после использования
    if 'consultation_data' in request.session:
        del request.session['consultation_data']

    return render(request, 'success_consultation.html', context)


def success_calculation(request):
    # Получаем данные из сессии
    calculation_data = request.session.get('calculation_data', {})

    context = {
        'request_data': {
            'buyer_name': calculation_data.get('buyer_name', 'Client'),
            'phone_number': calculation_data.get('phone_number', ''),
            'room_type': calculation_data.get('room_type', ''),
            'company_name': calculation_data.get('company_name', ''),
            'room_area': calculation_data.get('room_area', '')
        }
    }

    # Очищаем сессию после использования
    if 'calculation_data' in request.session:
        del request.session['calculation_data']

    return render(request, 'success_calculation.html', context)