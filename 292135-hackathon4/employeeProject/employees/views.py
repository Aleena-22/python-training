from django.shortcuts import render
import random

def employee_form(request):
    if request.method == "GET":
        return render(request, 'employees/form.html')

# View for calculating Net Salary
def calculate_net_salary(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gross_salary = float(request.POST.get('gross_salary'))
        tax = float(request.POST.get('tax')) / 100
        bonus = float(request.POST.get('bonus')) / 100
        
        # using formula to find the net salary 
        net_salary = gross_salary - (gross_salary * tax) + (gross_salary * bonus)
        
        return render(request, 'employees/resultPage.html', {
            'name': name,
            'net_salary': net_salary
        })

# View for jumbling a word
def jumble_word(request):
    if request.method == "POST":
        word = request.POST.get('word')
        word_list = list(word)
        random.shuffle(word_list)
        jumbled_word = ''.join(word_list)
        return render(request, 'employees/jumbleWord.html', {'jumbled_word': jumbled_word})

    return render(request, 'employees/jumbleWord.html')
