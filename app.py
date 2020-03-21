from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route("/confirmed.json")
def Confirmed():
    df=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
    df.groupby(['Country/Region'])[df.columns[len(df.columns)-1]].transform('sum')
    new_df = df.drop_duplicates(subset=['Country/Region'])
    new_df.set_index('Country/Region',inplace=True)
    Current_update_death=new_df.iloc[:,-1]
    data=Current_update_death.to_json(orient='index')
    return data


@app.route("/deaths.json")
def Death():
    df=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv')
    df.groupby(['Country/Region'])[df.columns[len(df.columns)-1]].transform('sum')
    new_df = df.drop_duplicates(subset=['Country/Region'])
    new_df.set_index('Country/Region',inplace=True)
    Current_update_death=new_df.iloc[:,-1]
    data=Current_update_death.to_json(orient='index')
    return data


@app.route("/recovered.json")
def Recovered():
    df=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv')
    df.groupby(['Country/Region'])[df.columns[len(df.columns)-1]].transform('sum')
    new_df = df.drop_duplicates(subset=['Country/Region'])
    new_df.set_index('Country/Region',inplace=True)
    Current_update_death=new_df.iloc[:,-1]
    data=Current_update_death.to_json(orient='index')
    return data

@app.route("/confirmed.json/<country>")
def ConfirmedbyCountry(country):
    df=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
    df.groupby(['Country/Region'])[df.columns[len(df.columns)-1]].transform('sum')
    new_df = df.drop_duplicates(subset=['Country/Region'])
    new_df = new_df.drop(['Province/State'],axis=1)

    new_df=new_df.loc[new_df['Country/Region'] == country]
    data=new_df.to_json(orient='index')
    return data

@app.route("/deaths.json/<country>")
def DeathsbyCountry(country):
    df=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv')
    df.groupby(['Country/Region'])[df.columns[len(df.columns)-1]].transform('sum')
    new_df = df.drop_duplicates(subset=['Country/Region'])
    new_df = new_df.drop(['Province/State'],axis=1)

    new_df=new_df.loc[new_df['Country/Region'] == country]
    data=new_df.to_json(orient='index')
    return data

@app.route("/recovered.json/<country>")
def RecoveredbyCountry(country):
    df=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv')
    df.groupby(['Country/Region'])[df.columns[len(df.columns)-1]].transform('sum')
    new_df = df.drop_duplicates(subset=['Country/Region'])
    new_df = new_df.drop(['Province/State'],axis=1)

    new_df=new_df.loc[new_df['Country/Region'] == country]
    data=new_df.to_json(orient='index')
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0')