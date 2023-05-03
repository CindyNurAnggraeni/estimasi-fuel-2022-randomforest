import pickle
import streamlit as sl

model = pickle.load(open('fuel_randomforest.sav', 'rb'))

sl.title('Estimasi Peringkat Konsumsi Bahan Bakar Pada Tahun 2022')


EngineSize = sl.number_input('Input Total Engine Size(L)')
Cylinders = sl.number_input('Input Total Cylinders')
FuelConsumptionCityL = sl.number_input('Input Total FuelConsumptionCityL')
CO2Emissions = sl.number_input('Input Total CO2 Emissions(g/km)')
CO2Rating = sl.number_input('Input Total CO2 Rating')
SmogRating = sl.number_input('Input Total Smog Rating')


predict = ''

if sl.button('Cek Rating'):
    predict = model.predict(
        [[EngineSize,Cylinders,FuelConsumptionCityL,CO2Emissions,CO2Rating,SmogRating]]
    )
    sl.write ('Estimasi Peringkat Konsumsi Bahan Bakar (Comb (L/100 km)) : ', predict)