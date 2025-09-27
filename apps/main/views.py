from django.shortcuts import render, redirect
from .forms import ConsultingForm
from .models import SaveDb

# Create your views here.
def main(request):
    context = {}
    return render(template_name="main.html", context=context, request=request)


def get_consult(request):
    if request.method == 'POST':
        # Если форма была отправлена, создаем экземпляр формы с этими данными
        form = ConsultingForm(request.POST)
        if form.is_valid():
            # Данные валидны, можно их обработать
            # Например, отправить на почту, сохранить в БД и т.д.
            buyer_name = form.cleaned_data['buyer_name']
            phone_number = form.cleaned_data['phone_number']
            description = form.cleaned_data['description']

            # Создаем объект и сохраняем
            new_record = SaveDb(buyer_name=buyer_name, phone_number=phone_number, description=description)
            new_record.save()  # Сохраняем в БД


            # После успешной обработки перенаправляем пользователя (на страницу "спасибо" или главную)
            return redirect('success_page')
    else:
        # Если это GET запрос, просто показываем пустую форму
        form = ConsultingForm()

    # Рендерим шаблон с формой (пустой или с ошибками)
    return render(request, "consultingform.html", {'form': form})