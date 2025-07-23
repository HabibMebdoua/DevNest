from django.shortcuts import render,redirect
from .telegram_conf import send_telegram_message
from django.contrib.auth.decorators import login_required
from .forms import OrderProjectForm
from django.contrib import messages



@login_required
def order_project(request):
    form = OrderProjectForm()
    if request.method == 'POST':
        form = OrderProjectForm(request.POST)
        if form.is_valid():

            # Getting data from the form
            data = form.cleaned_data
            project_title = data.get('title')
            project_desc = data.get('description')
            project_type = data.get('type')
            project_owner = request.user

            message = (
            "📬 *طلب مشروع جديد!*\n\n"
            f"*العنوان:* {project_title}\n"
            f"*الوصف:* {project_desc}\n"
            f"*النوع:* {project_type}\n\n"
            f"*من:* {project_owner.username}\n"
            f"*الهاتف:* {getattr(project_owner, 'phone_number', 'غير متوفر')}\n"
            f"*الإيميل:* {project_owner.email}"
            )

            send_telegram_message(message) #Sending the message to the admin

            order = form.save(commit=False)
            order.owner = request.user
            order.save()
            messages.success(request, ' تم إرسال طلب المشروع بنجاح! قم بتفقد لوحة التحكم')
            return redirect('index')
        else:
            messages.error(request, 'حدث خطأ أثناء إرسال طلب المشروع. يرجى المحاولة مرة أخرى.')

    context = {
        'form': form
    }
    return render(request, 'projects/order_project.html', context)