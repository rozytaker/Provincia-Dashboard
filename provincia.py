import streamlit as st
import pandas as pd
# import locale
# from locale import atof


# Get two numbers from the user
sideb = st.sidebar
sqft = sideb.number_input("Enter SqFt:",value=1715)
sqft_price = sideb.number_input("Enter SqFt Price:",value=8399)
floor_num = sideb.number_input("Enter Floor Number:",value=22)
east_price = sideb.number_input("East Facing Premium:",value=50)
#corner_premium_price = sideb.number_input("Corner Premium:")
per_floor_price=sideb.number_input("Per Floor Price:",value=20)
filename=sideb.text_input("Filename:",value='provincia')

# Calculate the sum
#sum = sqft + floor_num+east
basic_price= sqft*sqft_price
ac_copper_piping=sqft*40
club=400000
water_elec_gas = sqft*200
legal = 25000
car_parking = 500000
total_base_price = basic_price+ac_copper_piping+club+water_elec_gas+legal+car_parking
#final_corner_premium = sqft * corner_premium_price
final_east_premium = sqft * east_price
floor_premium = sqft *per_floor_price*(floor_num-4)
price_for_gst = total_base_price+final_east_premium+floor_premium
sgst_cgst = price_for_gst*0.025 + price_for_gst*0.025 
total_base_price_with_gst = price_for_gst+sgst_cgst
registration_cost = total_base_price_with_gst*0.076
corpus_fund = sqft*75
maintainence_cost = sqft*84
final_cost_of_house =total_base_price_with_gst+registration_cost+corpus_fund+maintainence_cost

import pandas as pd
print(basic_price)

final_data=pd.DataFrame([basic_price])
#final_data['Basic Price']=basic_price
print(final_data)
final_data.columns=['Basic Price']
final_data['AC Copper']=ac_copper_piping
final_data['Club']=club
final_data['Water-Elec-Gas']=water_elec_gas
final_data['Legal']=legal
final_data['Car Parking']=car_parking
final_data['Floor Rise']=floor_premium
final_data['East Facing']=final_east_premium
final_data['CGST and SGST']=sgst_cgst
final_data['Total Base Price']=total_base_price
final_data['Total PLC Cost']=floor_premium+final_east_premium
final_data['Total Unit Cost']=total_base_price+floor_premium+final_east_premium+sgst_cgst
final_data['Registration']=registration_cost
final_data['Corpus']=corpus_fund
final_data['Maintainence']=maintainence_cost
final_data['Total Final Cost of House']=final_cost_of_house
#final_data=final_data.applymap(atof)
lst = list(final_data.columns)
for c in lst:
    final_data[c] = final_data[c].astype(int).apply(lambda x: f'{x:,}')
print(final_data)

final_data_transpose=final_data.T

# Display the result
#st.write(f"The sum of the two numbers is: {st.dataframe(final_data)")
st.dataframe(final_data)
def convert_df(df):
   return final_data_transpose.to_csv(index=False).encode('utf-8')


csv = convert_df(final_data_transpose)
st.download_button(
   "Press to Download",
   csv,
   filename+".csv",
   "text/csv",
   key='download-csv'
)
