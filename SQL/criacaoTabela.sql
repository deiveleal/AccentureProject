/*
    "Country": "Afghanistan",
    "CountryCode": "AF",
    "Lat": "33.94",
    "Lon": "67.71",
    "Confirmed": 0,
    "Deaths": 0,
    "Recovered": 0,
    "Active": 0,
    "Date": "2020-01-22T00:00:00Z",
*/
/*
[
    {
        "Country": "Mexico",
        "Slug": "mexico",
        "ISO2": "MX"
    },
*/
CREATE TABLE PAIS
(
	ID				int 			not null auto_increment, #	pk
	NOME			varchar(50)     not null,
	SLUG			varchar(50)     null,
	SIGLA           varchar(2)      null,
	CONSTRAINT PK_PAIS PRIMARY KEY (ID)
);

/*
[{"Country":"Brazil","CountryCode":"BR","Province":"","City":"","CityCode":"","Lat":"-14.24","Lon":"-51.93","Cases":0,"Status":"confirmed","Date":"2020-01-22T00:00:00Z"},
*/
create table dados_paises
(
	id			int 			not null auto_increment, #	pk
	country			varchar(40)		not null,
	countryCode		char(2)			not null,
	lat			decimal			not null,
	lon			decimal 		not null,
	confirmed		int			null,
	deaths			int			null,
	recovered		int			null,
	active			int			null,
	date			datetime		not null,
	
	constraint 		pk_id			primary key (id),
	CONSTRAINT FK_DADOS_PAISES_PAIS FOREIGN KEY (ID_PAIS)
		REFERENCES PAIS (ID)
);
