
from flask import Flask,jsonify,request,url_for,render_template
import pandas as pd
import pickle
app=Flask(__name__)

model=pickle.load(open('rand_for.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        # name of dish
        diet = request.form['diet']
        if (diet == 'vegetarian'):
            diet_vegetarian = 1
            non_vegetarian = 0
        else:
            diet_vegetarian = 0
            non_vegetarian = 1

        #prep time
        prep_time=request.form['prep_time']

        # cook time
        cook_time = request.form['cook_time']

        # flavor profile
        flavor_profile=request.form['flavor_profile']
        if(flavor_profile=='sweet'):
            flavor_profile_sweet=1
            flavor_profile_spicy=0
            flavor_profile_bitter=0
            flavor_profile_sour=0
        elif(flavor_profile == 'spicy'):
            flavor_profile_sweet = 0
            flavor_profile_spicy = 1
            flavor_profile_bitter = 0
            flavor_profile_sour = 0
        elif(flavor_profile == 'bitter'):
            flavor_profile_sweet = 0
            flavor_profile_spicy = 0
            flavor_profile_bitter = 1
            flavor_profile_sour = 0
        else:
            flavor_profile_sweet = 0
            flavor_profile_spicy = 0
            flavor_profile_bitter = 0
            flavor_profile_sour = 1

        #coarse
        course=request.form['course']
        if(course=='main_course'):
            course_main_course=1
            course_dessert=0
            course_snack=0
            course_starter=0
        elif(course == 'dessert'):
            course_main_course = 0
            course_dessert = 1
            course_snack = 0
            course_starter = 0
        elif(course == 'snack'):
            course_main_course = 0
            course_dessert = 0
            course_snack = 1
            course_starter = 0
        else:
            course_main_course = 0
            course_dessert = 0
            course_snack = 0
            course_starter = 1

        #region
        region = request.form['region']
        if (region == 'West'):
            region_West=1
            region_South=0
            region_North=0
            region_East=0
            region_North_East=0
        elif (region == 'South'):
            region_West=0
            region_South=1
            region_North=0
            region_East=0
            region_North_East=0
        elif (region == 'North'):
            region_West=0
            region_South=0
            region_North=1
            region_East=0
            region_North_East=0
        elif (region == 'East'):
            region_West=0
            region_South=0
            region_North=0
            region_East=1
            region_North_East=0
        else:
            region_West=0
            region_South=0
            region_North=0
            region_East=0
            region_North_East=1

        prediction=model.predict([[prep_time, cook_time, diet_vegetarian, flavor_profile_bitter,
       flavor_profile_sour, flavor_profile_spicy, flavor_profile_sweet,
       course_main_course, course_snack, course_starter, region_East,
       region_North, region_North_East, region_South, region_West]])

        def pred():
            if (prediction[0] == 23):
                return 'West Bengal'
            elif (prediction[0] == 17):
                return 'Rajasthan'
            elif (prediction[0] == 16):
                return 'Punjab'
            elif (prediction[0] == 21):
                return 'Uttar Pradesh'
            elif (prediction[0] == 5):
                return 'Gujarat'
            elif (prediction[0] == 15):
                return 'Odisha'
            elif (prediction[0] == 11):
                return 'Maharashtra'
            elif (prediction[0] == 22):
                return 'Uttarakhand'
            elif (prediction[0] == 1):
                return 'Assam'
            elif (prediction[0] == 2):
                return 'Bihar'
            elif (prediction[0] == 0):
                return 'Andhra Pradesh'
            elif (prediction[0] == 8):
                return 'Karnataka'
            elif (prediction[0] == 19):
                return 'Telangana'
            elif (prediction[0] == 9):
                return 'Kerala'
            elif (prediction[0] == 18):
                return 'Tamil Nadu'
            elif (prediction[0] == 20):
                return 'Tripura'
            elif (prediction[0] == 12):
                return 'Manipur'
            elif (prediction[0] == 14):
                return 'Nagaland'
            elif (prediction[0] == 13):
                return 'NCT of Delhi'
            elif (prediction[0] == 7):
                return 'Jammu & Kashmir'
            elif (prediction[0] == 3):
                return 'Chhattisgarh'
            elif (prediction[0] == 6):
                return 'Haryana'
            elif (prediction[0] == 10):
                return 'Madhya Pradesh'
            else:
                return 'Goa'

        return render_template('home.html',prediction_text='The predicted state is {}'.format(pred()))

if __name__=="__main__":
    app.run(debug=True)