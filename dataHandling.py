import pandas
import plotly.express as px

df = pandas.read_csv('data.csv')
print(df.groupby('l')['attempt'].mean())

students = ["TRL_123", "TRL_987", "TRL_abc", "TRL_imb", "TRL_mda", "TRL_mno", "TRL_rst", "TRL_xsl", "TRL_xyz", "TRL_zet", "TRL_zny"]
fig = px.scatter(x=students, y=df.groupby('student_id')['attempt'].mean(), color=students)
fig.show()