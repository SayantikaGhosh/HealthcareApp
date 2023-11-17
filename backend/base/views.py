from django.shortcuts import render
from .models import Food, Consume
# from django.utils.timezone import timedelta
import datetime

def landing(request):
    return render(request, 'base/root.html')
    

def home(request):
     food_name = Food.objects.all()
     context = {'food_name':food_name}
     return render(request,'base/home.html',context)


def calorie_cal(request):
        if request.method == 'POST':
            weight = request.POST['weight']
            height = request.POST['height']
            age = request.POST['age']
            gender = request.POST['gender']
            # print("weight: ",weight)
            # print("height: ",height)
            # print("age: ",age)
            # print("gender: ",gender)
            if gender == 'male':
                result = 66.47 + (13.75 * int(weight)) + (5.003 * int(height)) - (6.755 * int(age))
                # print(result,"######################")
                return render(request,'base/calorie_cal.html',{'result':result})
            if gender == 'female':
                result = 655.1 + (9.563 * int(weight)) + (1.850 * int(height)) - (4.676 * int(age))
                # print(result,"######################") 
                return render(request,'base/calorie_cal.html',{'result':result})
    
        return render(request,'base/calorie_cal.html')
    
def calorie_counter(request):
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(foodname=food_consumed)
        user = request.user
        consume = Consume(user=user, foodconsumed=consume)
        consume.save()
        foods = Food.objects.all()
    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'base/calorie_counter.html', {'foods': foods, 'consumed_food': consumed_food})

def ovulation(request):
    if request.method == 'POST':
            date = request.POST.get('date') #first date of last month period d/m/y
            cycle_length = request.POST.get('cycle_length')#length of menstrual cycle in days
            # date = datetime.datetime.strptime(date,"%d/%m/%y")
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            print(date)
            cycle_length = int(cycle_length)
            estimated_ovulation_day = cycle_length - 14
            ovulation_day = datetime.timedelta(days=estimated_ovulation_day)
            ovulation_date = date + ovulation_day
            ovulation_date = ovulation_date.strftime('%d-%m-%Y')
            return render(request,'base/ovulation.html',{'ovulation_date':ovulation_date})
    return render(request,'base/ovulation.html')

def menstruation(request):
    if request.method == 'POST':
            date = request.POST.get('date') #first date of last month period d/m/y
            cycle_length = request.POST.get('cycle_length')#length of menstrual cycle in days
            # date = datetime.datetime.strptime(date,"%d/%m/%y")
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            print(date)
            cycle_length = int(cycle_length)
            estimated_period_date = date + datetime.timedelta(days=cycle_length)
            estimated_period_date = estimated_period_date.strftime('%d-%m-%Y')
            return render(request,'base/menstruation.html',{'men_date':estimated_period_date})
    return render(request,'base/menstruation.html')

