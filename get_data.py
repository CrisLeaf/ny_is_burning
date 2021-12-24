import requests

class NCEIData:
	"""
	References:
	https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation
	"""
	
	def __init__(self, dataset_name, data_types, stations, start_date_time, end_date_time,
				 location):
		self._base_api_url = "https://www.ncei.noaa.gov/access/services/data/v1/?"
		self._dataset_name = self.call_api(dataset_name, data_types, stations, start_date_time,
										   end_date_time, location)
		
	def call_api(self, dataset_name, data_types, stations, start_date_time, end_date_time,
				 location):
		full_url = self._base_api_url + "dataset=" + dataset_name + "&dataTypes=" + data_types + \
				   "&stations=" + stations + "&startDate=" + start_date_time + "&endDate=" + \
				   end_date_time + "&boundingBox=" + location + "&units=standard"
		response = requests.get(full_url)
		return response.text
	
	def get_data(self):
		return self._dataset_name
	
	def write_data_file(self, file_name):
		with open(file_name, "w") as file:
			file.write(self._dataset_name)
		
if __name__ == "__main__":
	params = {
		"dataset_name": "daily-summaries",
		"data_types": "TAVG, TMAX, TMIN, TOBS, DAEV, EVAP, MDEV, DASF, MDSF, PRCP, SNOW, SNWD, "
					  "ACMH, ACSH, PSUN, TSUN, WESD, WT01, WT02, WT03, WT04, WT05, WT06, WT07, "
					  "WT08, WT09, WT11, WT13, WT14, WT15, WT16, WT17, WT18, WT19, WT21, WT22, "
					  "AWND, DAWM, FMTM, MDWM, PGTM, WDF1, WDF2, WDF5, WDFG, WDFM, WDMV, WSF1, "
					  "WSF2, WSF5, WSFG, WSFM",
		"stations": "USW00094728",
		"start_date_time": "1869-01-01",
		"end_date_time": "2020-12-15",
		"location": "90,-180,-90,180"
	}
	ncei_data = NCEIData(**params)
	print(ncei_data.get_data())
	ncei_data.write_data_file("weather_data.csv")
	print("Done!")