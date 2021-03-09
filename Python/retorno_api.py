
import requests
import json
import pandas as pd

class Summary:
    __url = "https://api.covid19api.com/summary"
    __payload = {}
    __headers= {}

    def get_url(self):
        return self.__url
    def set_url(self, url):
        self.__url = url

    def dados_raw(self):
        response = requests.request("GET", self.__url, headers=self.__headers, data =self.__payload)
        return response
    
    def retorna_dataframe(self):
        raw_json = self.dados_raw().json()
        df = pd.DataFrame()
        Country = []
        CountryCode = []
        NewConfirmed = []
        TotalConfirmed = []
        NewDeaths = []
        TotalDeaths = []
        NewRecovered = []
        TotalRecovered = []
        Date = []

        for pais in range(len(raw_json['Countries'])):
            Country.append(raw_json["Countries"][pais]['Country'])
            CountryCode.append(raw_json["Countries"][pais]['CountryCode'])
            NewConfirmed.append(raw_json["Countries"][pais]['NewConfirmed'])
            TotalConfirmed.append(raw_json["Countries"][pais]['TotalConfirmed'])            
            NewDeaths.append(raw_json["Countries"][pais]['NewDeaths'])
            TotalDeaths.append(raw_json["Countries"][pais]['TotalDeaths'])           
            NewRecovered.append(raw_json["Countries"][pais]['NewRecovered'])
            TotalRecovered.append(raw_json["Countries"][pais]['TotalRecovered'])
            Date.append(raw_json["Countries"][pais]['Date'])        

        df['Country'] = pd.Series(Country)
        df['CountryCode'] = pd.Series(CountryCode)
        df['NewConfirmed'] = pd.Series(NewConfirmed)
        df['TotalConfirmed'] = pd.Series(TotalConfirmed)
        df['NewDeaths'] = pd.Series(NewDeaths)
        df['TotalDeaths'] = pd.Series(TotalDeaths)
        df['NewRecovered'] = pd.Series(NewRecovered)
        df['TotalRecovered'] = pd.Series(TotalRecovered)
        df['Date'] = pd.Series(Date, dtype='datetime64[ns]') 

        df.to_csv(r'backup_csv/summary.csv')

        return df

class Country:
    __url = "https://api.covid19api.com/countries"
    __payload = {}
    __headers= {}

    def get_url(self):
        return self.__url
    def set_url(self, url):
        self.__url = url

    def dados_raw(self):
        response = requests.request("GET", self.__url, headers=self.__headers, data =self.__payload)
        return response

    def retorna_dataframe(self):
        raw_json = self.dados_raw().json()
        df = pd.DataFrame()
        Country = []
        Slug = []
        ISO2 = []

        for pais in range(len(raw_json)):
            Country.append(raw_json[pais]['Country'])
            Slug.append(raw_json[pais]['Slug'])
            ISO2.append(raw_json[pais]['ISO2'])      

        df['Country'] = pd.Series(Country)
        df['Slug'] = pd.Series(Slug)
        df['ISO2'] = pd.Series(ISO2)

        df.to_csv(r'backup_csv/country.csv')

        return df

class All_Data:
    __url = "https://api.covid19api.com/all"
    __payload = {}
    __headers= {}

    def get_url(self):
        return self.__url
    def set_url(self, url):
        self.__url = url

    def dados_raw(self):
        response = requests.request("GET", self.__url, headers=self.__headers, data =self.__payload)
        return response

    def retorna_dataframe(self):
        raw_json = self.dados_raw().json()
        df = pd.DataFrame()
        Country = []
        CountryCode = []
        Lat = []
        Lon = []
        Confirmed = []
        Deaths = []
        Recovered = []
        Active = []
        Date = []

        for pais in range(len(raw_json)):
            Country.append(raw_json[pais]['Country'])
            CountryCode.append(raw_json[pais]['CountryCode'])
            Lat.append(raw_json[pais]['Lat'])
            Lon.append(raw_json[pais]['Lon'])
            Confirmed.append(raw_json[pais]['Confirmed'])
            Deaths.append(raw_json[pais]['Deaths'])
            Recovered.append(raw_json[pais]['Recovered'])
            Active.append(raw_json[pais]['Active'])
            Date.append(raw_json[pais]['Date'])
    

        df['Country'] = pd.Series(Country)
        df['CountryCode'] = pd.Series(CountryCode)
        df['Lat'] = pd.Series(Lat)
        df['Lon'] = pd.Series(Lon)
        df['Confirmed'] = pd.Series(Confirmed)
        df['Deaths'] = pd.Series(Deaths)
        df['Recovered'] = pd.Series(Recovered)
        df['Active'] = pd.Series(Active)
        df['Date'] = pd.Series(Date)

        df.to_csv(r'backup_csv/all_data.csv')

        return df

class By_Country:
    
    class_country = Country()
    __url = "https://api.covid19api.com/total/country/{0}"
    __payload = {}
    __headers= {}
    __country_data = {}
    __data_by_country = {}
    __country_ok = []
    __list_countries = list(class_country.retorna_dataframe()["Country"])

    def get_url(self):
        return self.__url
    def set_url(self, url):
        self.__url = url

    def dados_raw(self):
        for country in range(len(self.__list_countries)):
            if requests.get(self.__url.format(self.__list_countries[country])).status_code == 200:
                self.__country_data[self.__list_countries[country]] = requests.request("GET", self.__url.format(self.__list_countries[country]),
                headers=self.__headers, data = self.__payload)
                self.__country_ok.append(self.__list_countries[country])
        return self.__country_data

    def retorna_dataframe(self):
        Country = []
        CountryCode = []
        Province = []
        City = []
        CityCode = []
        Lat = []
        Lon = []
        Confirmed = []
        Deaths = []
        Recovered = []
        Active = []
        Date = []

        raw = self.dados_raw()

        for country in self.__country_ok:
            self.__data_by_country[country] = raw[country].json()

        for country in self.__country_ok:
            for pais in range(len(self.__data_by_country[country])):
                Country.append(self.__data_by_country[country][pais]['Country'])
                CountryCode.append(self.__data_by_country[country][pais]['CountryCode'])
                Province.append(self.__data_by_country[country][pais]['Province'])
                City.append(self.__data_by_country[country][pais]['City'])
                CityCode.append(self.__data_by_country[country][pais]['CityCode'])
                Lat.append(self.__data_by_country[country][pais]['Lat'])
                Lon.append(self.__data_by_country[country][pais]['Lon'])
                Confirmed.append(self.__data_by_country[country][pais]['Confirmed'])
                Deaths.append(self.__data_by_country[country][pais]['Deaths'])
                Recovered.append(self.__data_by_country[country][pais]['Recovered'])
                Active.append(self.__data_by_country[country][pais]['Active'])
                Date.append(self.__data_by_country[country][pais]['Date'])

        df = pd.DataFrame()
        df["Country"] = pd.Series(Country)
        df["CountryCode"] = pd.Series(CountryCode)
        df["Province"] = pd.Series(Province)
        df["City"] = pd.Series(City)
        df["CityCode"] = pd.Series(CityCode)
        df["Lat"] = pd.Series(Lat)
        df["Lon"] = pd.Series(Lon)
        df["Confirmed"] = pd.Series(Confirmed)
        df["Deaths"] = pd.Series(Deaths)
        df["Recovered"] = pd.Series(Recovered)
        df["Active"] = pd.Series(Active)
        df["Date"] = pd.Series(Date, dtype='datetime64[ns]')

        df.to_csv(r'backup_csv/by_country.csv')

        return df







