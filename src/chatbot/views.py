# import requests
# from django.http import JsonResponse
# from django.shortcuts import render

# def ai_chat(request):
#     if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
#         user_message = request.POST.get("message")

#         headers = {
#             "Authorization": "Bearer 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",
#             "Content-Type": "application/json"
#         }

#         data = {
#             "model": "openai/gpt-3.5-turbo",
#             "messages": [
#             {
#             "role": "system",
#             "content": (
#                 "أنت مساعد ذكي يعمل في منصة متخصصة في تنفيذ أفكار العملاء وتحويلها إلى مشاريع برمجية مكتملة "
#                 "(مثل تطبيقات ويب، تطبيقات جوال، برامج سطح مكتب، أو فيديوهات تعريفية). "
#                 "دورك هو استقبال فكرة العميل، فهم متطلباته، ثم مساعدته باقتراح الشكل الأنسب لتنفيذ فكرته، "
#                 "سواء كان تطبيق ويب أو موبايل أو أي خيار آخر، وشرح التقنية المناسبة بلغة واضحة وبسيطة. "
#                 "اسم المنصة التي تعمل بها هو DevNest. "
#                 "لا تجب على أي استفسار لا يتعلق بالمنصة أو البرمجة."
#             )
#             },
#         {"role": "user", "content": user_message}
# ]

#         }

#         api_response = requests.post(
#             "https://openrouter.ai/api/v1/chat/completions",
#             headers=headers,
#             json=data
#         )

#         if api_response.status_code == 200:
#             content = api_response.json()['choices'][0]['message']['content']
#             return JsonResponse({"response": content})
#         else:
#             error_message = api_response.json().get("error", {}).get("message", "خطأ غير معروف")
#             return JsonResponse({"response": f"حدث خطأ: {error_message}"})

#     return render(request, "chatbot/chat.html")
