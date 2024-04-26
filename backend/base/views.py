from django.shortcuts import render, redirect
from .models import Food, Consume
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.utils.timezone import timedelta
import datetime
import spacy
import joblib
import pandas as pd
nlp = spacy.load("en_core_web_lg")
data = pd.read_csv('static/yoga.csv')

model = joblib.load('static/word_embedding_model')

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

            if gender == 'male':
                result = 66.47 + (13.75 * int(weight)) + (5.003 * int(height)) - (6.755 * int(age))
                result = round(result)
                return render(request,'base/calorie_cal.html',{'result':result})
            if gender == 'female':
                result = 655.1 + (9.563 * int(weight)) + (1.850 * int(height)) - (4.676 * int(age))
                result = round(result)
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


def delete_fooditem(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('calorie_counter')
    return render(request, 'base/delete_fooditem.html')

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

def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return tokens

def recommend_yoga(user_problem, model):
    user_tokens = preprocess(user_problem)
    similar_yoga = []
    for yoga_name, benefit in zip(data['Asana'],  data['Benefits']):
        benefit_tokens = preprocess(benefit)
        similarity = model.wv.n_similarity(user_tokens, benefit_tokens)
        similar_yoga.append((yoga_name,similarity, benefit))
    similar_yoga.sort(key=lambda x: x[1], reverse=True)
    return similar_yoga



def recommend(request):
    if request.method == 'POST':
        problem = request.POST['problem']
        result = recommend_yoga(problem,model)
        result = result[0:4]
        
        yoga_names = [yoga[0] for yoga in result]
        benefits = [yoga[2] for yoga in result]

        items = list(zip(yoga_names, benefits))

        print(items)
        return render(request,'base/recommend_yoga.html',{'items':items})

    return render(request,'base/recommend_yoga.html')
    



