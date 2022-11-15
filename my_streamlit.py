import streamlit as st
import pandas as pd
import numpy as np

option = st.sidebar.selectbox(
	'silahkan pilih:',
	('home','Dataframe','chart')
)

if option == 'home' or option == '':
	st.write("""# Halaman Utama""")
elif option == 'Dataframe':
	st.write("""# Dataframe""")

	df = pd.Dataframe({
		'Column 1':[1,2,3,4],
		'Column 2':[10,12,14,16]
		})
	df
elif option == 'chart':
	st.write("""# Draw Charts""")
	chart_data = pd.Dataframe(
		np.random.randn(20,2),
		Columns=['a','b']
		)

	st.line_chart(chart_data)
	chart_data