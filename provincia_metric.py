import streamlit as st
import pandas as pd
# import locale
# from locale import atof

st.sidebar.title("Tabs")
tabs = ["Provincia", "Greenspace"]
selected_tab = st.sidebar.radio("", tabs)


if selected_tab == "Provincia":
	st.sidebar.title("Provincia")
#	st.sidebar.text("This is for Provincia.")

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
	#st.dataframe(final_data)
	def convert_df(df):
	   return final_data_transpose.to_csv().encode('utf-8')
	#print(final_data.T)


	col1, col2, col3 = st.columns(3)
	col1.metric("Basic Price", "{:,.2f}".format(basic_price))
	col2.metric("AC Copper Piping", "{:,.2f}".format(ac_copper_piping))
	col3.metric("Club", "{:,.2f}".format(club))
	col1.metric("Water-Elec-Gas", "{:,.2f}".format(water_elec_gas))
	col2.metric("Legal", "{:,.2f}".format(legal))
	col3.metric("Car Parking", "{:,.2f}".format(car_parking))
	col1.metric("Floor Rise", "{:,.2f}".format(floor_premium))
	col2.metric("East Facing", "{:,.2f}".format(final_east_premium))
	col3.metric("CGST and SGST", "{:,.2f}".format(sgst_cgst))
	col1.metric("Total Base Price", "{:,.2f}".format(total_base_price))
	col2.metric("Total PLC Cost", "{:,.2f}".format(floor_premium+final_east_premium))
	col3.metric("Total Unit Cost", "{:,.2f}".format(total_base_price+floor_premium+final_east_premium+sgst_cgst))
	col1.metric("Registration", "{:,.2f}".format(registration_cost))
	col2.metric("Corpus", "{:,.2f}".format(corpus_fund))
	col3.metric("Maintainence", "{:,.2f}".format(maintainence_cost))
	col1.metric("Final House Price", "{:,.2f}".format(final_cost_of_house))


	csv = convert_df(final_data_transpose)
	st.download_button(
	   "Press to Download Excel File",
	   csv,
	   filename+".csv",
	   "text/csv",
	   key='download-csv'
	)

elif selected_tab == "Greenspace":
	st.sidebar.title("Greenspace")
	#st.sidebar.text("This is the Greenspace")

	# Get two numbers from the user
	sideb1 = st.sidebar
	sqft1 = sideb1.number_input("Enter SqFt :",value=1945)
	sqft_price1 = sideb1.number_input("Enter SqFt Price: ",value=6799)
	floor_num1 = sideb1.number_input("Enter Floor Number: ",value=15)
	#east_price1 = sideb1.number_input("East Facing Premium: ",value=0,key=4)
	#corner_premium_price = sideb.number_input("Corner Premium:")
	per_floor_price1=sideb1.number_input("Per Floor Price: ",value=20)
	filename1=sideb1.text_input("Filename: ",value='Greenspace')

	# Calculate the sum
	#sum = sqft + floor_num+east
	basic_price1= sqft1*sqft_price1
	amenities=1000000
	legal1 = 17700
	gas_elec=200000
	total_base_price1 = basic_price1+legal1+amenities+gas_elec


	floor_premium1 = sqft1 *per_floor_price1*(floor_num1-4)
	price_for_gst1 = total_base_price1+floor_premium1
	sgst_cgst1 = price_for_gst1*0.025 + price_for_gst1*0.025 
	total_base_price_with_gst1 = price_for_gst1+sgst_cgst1
	registration_cost1 = total_base_price_with_gst1*0.076
	corpus_fund1 = sqft1*60
	maintainence_cost1 = sqft1*60
	final_cost_of_house1 =total_base_price_with_gst1+registration_cost1+corpus_fund1+maintainence_cost1

	import pandas as pd
	print(basic_price1)

	final_data1=pd.DataFrame([basic_price1])
	#final_data['Basic Price']=basic_price
	print(final_data1)
	final_data1.columns=['Basic Price']
	final_data1['Gas_Elect']=gas_elec
	final_data1['Amenities']=amenities
	final_data1['Legal']=legal1
	final_data1['Floor Rise']=floor_premium1
	#final_data1['East Facing']=final_east_premium1
	final_data1['CGST and SGST']=sgst_cgst1
	final_data1['Total Base Price']=total_base_price1
	final_data1['Total Unit Cost']=total_base_price1+floor_premium1+sgst_cgst1
	final_data1['Registration']=registration_cost1
	final_data1['Corpus']=corpus_fund1
	final_data1['Maintainence']=maintainence_cost1
	final_data1['Total Final Cost of House']=final_cost_of_house1
	#final_data=final_data.applymap(atof)
	lst = list(final_data1.columns)
	for c in lst:
	    final_data1[c] = final_data1[c].astype(int).apply(lambda x: f'{x:,}')
	print(final_data1)

	final_data_transpose1=final_data1.T

	# Display the result
	#st.write(f"The sum of the two numbers is: {st.dataframe(final_data)")
	#st.dataframe(final_data1)
	def convert_df1(df):
	   return final_data_transpose1.to_csv().encode('utf-8')
	print(final_data1.T)


	
	col1, col2, col3 = st.columns(3)
	col2.metric("Basic Price", "{:,.2f}".format(basic_price1))
	col3.metric("Amenities", "{:,.2f}".format(amenities))
	col1.metric("Water-Elec-Gas", "{:,.2f}".format(gas_elec))
	col2.metric("Legal", "{:,.2f}".format(legal1))
	col3.metric("Floor Rise", "{:,.2f}".format(floor_premium1))
	col1.metric("CGST and SGST", "{:,.2f}".format(sgst_cgst1))
	col2.metric("Total Base Price", "{:,.2f}".format(total_base_price1))
	col3.metric("Total Unit Cost", "{:,.2f}".format(total_base_price1+floor_premium1+sgst_cgst1))
	col1.metric("Registration", "{:,.2f}".format(registration_cost1))
	col1.metric("Corpus", "{:,.2f}".format(corpus_fund1))
	col2.metric("Maintainence", "{:,.2f}".format(maintainence_cost1))
	col3.metric("Final House Price", "{:,.2f}".format(final_cost_of_house1))

	csv1 = convert_df1(final_data_transpose1)
	st.download_button(
	   "Press to Download Excel File",
	   csv1,
	   filename1+".csv",
	   "text/csv",
	   key='download-csv1'
	)
