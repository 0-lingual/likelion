from django.shortcuts import render

# Create your views here.
def lotto(request):
    import random

    lotto_number = list()
    for _ in range(7):
        number = random.randint(1,45)
        lotto_number.append(number)

    return render(request, 'lotto.html', {'lotto_number' : lotto_number})