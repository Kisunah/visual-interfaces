d3.csv('data/aqiData.csv')
    .then(_data => {
        console.log('Data loading complete');

        let data = _data;

        let stateList = [];
        data.forEach((item) => {
            if (stateList.indexOf(item.State) == -1) {
                stateList.push(item.State);
            }
        });

        let countyList = [];
        stateList.forEach((state) => {
            let object = {
                State: state,
                Counties: []
            };
            data.forEach((item) => {
                if (state == item.State) {
                    if (object.Counties.indexOf(item.County) == -1) {
                        object.Counties.push(item.County);
                    }
                }
            });
            countyList.push(object);
        });

        let state1 = document.getElementById('state1');
        let county1 = document.getElementById('county1');
        let state2 = document.getElementById('state2');
        let county2 = document.getElementById('county2');

        stateList.sort();
        stateList.forEach((state) => {
            let option = document.createElement('option');
            option.value = state;
            option.innerHTML = state;
            state1.appendChild(option);
        });

        // I don't know why it wouldn't let me append the option element to both state1 and state2 in the same forEach loop
        stateList.forEach((state) => {
            let option = document.createElement('option');
            option.value = state;
            option.innerHTML = state;
            state2.appendChild(option);
        });

        // Populate the year select elements
        let year1 = document.getElementById('year1');
        let year2 = document.getElementById('year2');
        for (let i = 2021; i > 1980; i--) {
            let option1 = document.createElement('option');
            option1.value = i;
            option1.innerHTML = i;

            let option2 = document.createElement('option');
            option2.value = i;
            option2.innerHTML = i;

            year1.appendChild(option1);
            year2.appendChild(option2);
        }

        selectedState1CountyList = [];
        state1.addEventListener('change', (event) => {
            county1.innerHTML = '<option value=""></option>';
            countyList.forEach((item) => {
                if (item.State == event.target.value) {
                    selectedState1CountyList = item.Counties;
                }
            });

            selectedState1CountyList.sort();
            selectedState1CountyList.forEach((county) => {
                let option = document.createElement('option');
                option.value = county;
                option.innerHTML = county;
                county1.appendChild(option);
            });
        });


        selectedState2CountyList = [];
        state2.addEventListener('change', (event) => {
            county2.innerHTML = '<option value=""></option>';
            countyList.forEach((item) => {
                if (item.State == event.target.value) {
                    selectedState2CountyList = item.Counties
                }
            });

            selectedState2CountyList.sort();
            selectedState2CountyList.forEach((county) => {
                let option = document.createElement('option');
                option.value = county;
                option.innerHTML = county;
                county2.appendChild(option);
            });
        });

        this.selectedCounty1Data;
        county1.addEventListener('change', (event) => {
            let selectedCounty1Data = [];
            data.forEach((item) => {
                if (item.State == state1.value && item.County == event.target.value) selectedCounty1Data.push(item);
            });

            this.aqiLineChart1
            if (document.getElementById('aqiChart1').children.length == 0) {
                this.aqiLineChart1 = new AQILineChart({
                    'parentElement': '#aqiChart1',
                    'containerHeight': 500,
                    'containerWidth': 700
                }, selectedCounty1Data);
            } else {
                this.aqiLineChart1.updateChart(selectedCounty1Data);
            }

            this.pollutantLineChart1;
            if (document.getElementById('pollutantChart1').children.length == 0) {
                this.pollutantLineChart1 = new PollutantLineChart({
                    'parentElement': '#pollutantChart1',
                    'containerHeight': 500,
                    'containerWidth': 700
                }, selectedCounty1Data);
            } else {
                this.pollutantLineChart1.updateChart(selectedCounty1Data);
            }

            this.noMeasurement1;
            if (document.getElementById('noMeasurementChart1').children.length == 0) {
                while (selectedCounty1Data.length < 42) {
                    selectedCounty1Data.sort((a, b) => {
                        return a.Year - b.Year
                    });

                    let length = selectedCounty1Data.length;
                    for (i = 0; i < selectedCounty1Data.length; i++) {
                        if (parseInt(selectedCounty1Data[i].Year) != 1980 + i) {
                            selectedCounty1Data.push({
                                State: state1.value,
                                County: event.target.value,
                                Year: `${1980 + i}`,
                                'Days with AQI': '0'
                            });
                            break;
                        }
                    }

                    if (selectedCounty1Data.length == length) {
                        let lastYear = parseInt(selectedCounty1Data[selectedCounty1Data.length - 1].Year);
                        selectedCounty1Data.push({
                            State: state1.value,
                            County: event.target.value,
                            Year: `${lastYear + 1}`,
                            'Days with AQI': '0'
                        })
                    }
                }

                selectedCounty1Data.sort((a, b) => {
                    return a.Year - b.Year
                });

                this.noMeasurement1 = new NoMeasurementChart({
                    'parentElement': '#noMeasurementChart1',
                    'containerHeight': 500,
                    'containerWidth': 700
                }, selectedCounty1Data);

            } else {
                this.noMeasurement1.updateChart(selectedCounty1Data);
            }

            this.selectedCounty1Data = selectedCounty1Data;
            selectedCounty1DescriptionData = [];
            selectedCounty1PollutantData = [];
            selectedCounty1Data.forEach((item) => {
                if (item['Year'] == 2021) {
                    goodObject = {
                        Name: 'Good',
                        Days: item['Good Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty1DescriptionData.push(goodObject);

                    moderateObject = {
                        Name: 'Moderate',
                        Days: item['Moderate Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty1DescriptionData.push(moderateObject);

                    sensitiveObject = {
                        Name: 'Sensitive',
                        Days: item['Unhealthy for Sensitive Groups Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty1DescriptionData.push(sensitiveObject);

                    unhealthyObject = {
                        Name: 'Unhealthy',
                        Days: item['Unhealthy Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty1DescriptionData.push(unhealthyObject);

                    veryUnhealthyObject = {
                        Name: 'Very Unhealthy',
                        Days: item['Very Unhealthy Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty1DescriptionData.push(veryUnhealthyObject);

                    hazardousObject = {
                        Name: 'Hazardous',
                        Days: item['Hazardous Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty1DescriptionData.push(hazardousObject);

                    COObject = {
                        Name: 'CO',
                        Days: item['Days CO']
                    };
                    selectedCounty1PollutantData.push(COObject);

                    NO2Object = {
                        Name: 'NO2',
                        Days: item['Days NO2']
                    };
                    selectedCounty1PollutantData.push(NO2Object);

                    OzoneObject = {
                        Name: 'Ozone',
                        Days: item['Days Ozone']
                    };
                    selectedCounty1PollutantData.push(OzoneObject);

                    SO2Object = {
                        Name: 'SO2',
                        Days: item['Days SO2']
                    };
                    selectedCounty1PollutantData.push(SO2Object);

                    PM25Object = {
                        Name: 'PM2.5',
                        Days: item['Days PM2.5']
                    };
                    selectedCounty1PollutantData.push(PM25Object);

                    PM10Object = {
                        Name: 'PM10',
                        Days: item['Days PM10']
                    };
                    selectedCounty1PollutantData.push(PM10Object);
                }
            });
            this.aqiDescription1;
            if (document.getElementById('aqiDescription1').children.length == 0) {
                this.aqiDescription1 = new AqiDescription({
                    'parentElement': '#aqiDescription1',
                    'containerHeight': 500,
                    'containerWidth': 700
                }, selectedCounty1DescriptionData);
            } else {
                this.aqiDescription1.updateChart(selectedCounty1DescriptionData);
            }

            this.pollutant1;
            if (document.getElementById('pollutant1').children.length == 0) {
                this.pollutant1 = new Pollutant({
                    'parentElement': '#pollutant1',
                    'containerHeight': 500,
                    'containerWidth': 700
                }, selectedCounty1PollutantData);
                window.scrollTo(0, 0);
            } else {
                this.pollutant1.updateChart(selectedCounty1PollutantData);
            }
        });

        year1.addEventListener('change', (event) => {
            selectedCounty1DescriptionData = [];
            selectedCounty1PollutantData = [];
            this.selectedCounty1Data.forEach((item) => {
                if (item['Year'] == event.target.value) {
                    goodObject = {
                        Name: 'Good',
                        Days: item['Good Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty1DescriptionData.push(goodObject);

                    moderateObject = {
                        Name: 'Moderate',
                        Days: item['Moderate Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty1DescriptionData.push(moderateObject);

                    sensitiveObject = {
                        Name: 'Sensitive',
                        Days: item['Unhealthy for Sensitive Groups Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty1DescriptionData.push(sensitiveObject);

                    unhealthyObject = {
                        Name: 'Unhealthy',
                        Days: item['Unhealthy Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty1DescriptionData.push(unhealthyObject);

                    veryUnhealthyObject = {
                        Name: 'Very Unhealthy',
                        Days: item['Very Unhealthy Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty1DescriptionData.push(veryUnhealthyObject);

                    hazardousObject = {
                        Name: 'Hazardous',
                        Days: item['Hazardous Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty1DescriptionData.push(hazardousObject);

                    COObject = {
                        Name: 'CO',
                        Days: item['Days CO']
                    };
                    selectedCounty1PollutantData.push(COObject);

                    NO2Object = {
                        Name: 'NO2',
                        Days: item['Days NO2']
                    };
                    selectedCounty1PollutantData.push(NO2Object);

                    OzoneObject = {
                        Name: 'Ozone',
                        Days: item['Days Ozone']
                    };
                    selectedCounty1PollutantData.push(OzoneObject);

                    SO2Object = {
                        Name: 'SO2',
                        Days: item['Days SO2']
                    };
                    selectedCounty1PollutantData.push(SO2Object);

                    PM25Object = {
                        Name: 'PM2.5',
                        Days: item['Days PM2.5']
                    };
                    selectedCounty1PollutantData.push(PM25Object);

                    PM10Object = {
                        Name: 'PM10',
                        Days: item['Days PM10']
                    };
                    selectedCounty1PollutantData.push(PM10Object);
                }
            });

            this.aqiDescription1.updateChart(selectedCounty1DescriptionData);
            this.pollutant1.updateChart(selectedCounty1PollutantData);
        });

        this.selectedCounty2Data;
        county2.addEventListener('change', (event) => {
            let selectedCounty2Data = [];
            data.forEach((item) => {
                if (item.State == state2.value && item.County == event.target.value) selectedCounty2Data.push(item);
            });

            this.aqiLineChart2;
            if (document.getElementById('aqiChart2').children.length == 0) {
                this.aqiLineChart2 = new AQILineChart({
                    'parentElement': '#aqiChart2',
                    'containerHeight': 500,
                    'containerWidth': 700
                }, selectedCounty2Data);
            } else {
                this.aqiLineChart2.updateChart(selectedCounty2Data);
            }

            this.pollutantLineChart2;
            if (document.getElementById('pollutantChart2').children.length == 0) {
                this.pollutantLineChart2 = new PollutantLineChart({
                    'parentElement': '#pollutantChart2',
                    'containerHeight': 500,
                    'containerWidth': 700
                }, selectedCounty2Data);
            } else {
                this.pollutantLineChart2.updateChart(selectedCounty2Data);
            }

            this.noMeasurement2;
            if (document.getElementById('noMeasurementChart2').children.length == 0) {
                while (selectedCounty2Data.length < 42) {
                    selectedCounty2Data.sort((a, b) => {
                        return a.Year - b.Year
                    });

                    let length = selectedCounty2Data.length;
                    for (i = 0; i < selectedCounty2Data.length; i++) {
                        if (parseInt(selectedCounty2Data[i].Year) != 1980 + i) {
                            selectedCounty2Data.push({
                                State: state1.value,
                                County: event.target.value,
                                Year: `${1980 + i}`,
                                'Days with AQI': '0'
                            });
                            break;
                        }
                    }

                    if (selectedCounty2Data.length == length) {
                        let lastYear = parseInt(selectedCounty2Data[selectedCounty2Data.length - 1].Year);
                        selectedCounty2Data.push({
                            State: state1.value,
                            County: event.target.value,
                            Year: `${lastYear + 1}`,
                            'Days with AQI': '0'
                        })
                    }
                }

                selectedCounty2Data.sort((a, b) => {
                    return a.Year - b.Year
                });

                this.noMeasurement2 = new NoMeasurementChart({
                    'parentElement': '#noMeasurementChart2',
                    'containerHeight': 500,
                    'containerWidth': 700
                }, selectedCounty2Data);
            } else {
                this.noMeasurement2.updateChart(selectedCounty2Data)
            }

            this.selectedCounty2Data = selectedCounty2Data;
            let selectedCounty2DescriptionData = [];
            let selectedCounty2PollutantData = [];
            selectedCounty2Data.forEach((item) => {
                if (item['Year'] == 2021) {
                    goodObject = {
                        Name: 'Good',
                        Days: item['Good Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty2DescriptionData.push(goodObject);

                    moderateObject = {
                        Name: 'Moderate',
                        Days: item['Moderate Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty2DescriptionData.push(moderateObject);

                    sensitiveObject = {
                        Name: 'Sensitive',
                        Days: item['Unhealthy for Sensitive Groups Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty2DescriptionData.push(sensitiveObject);

                    unhealthyObject = {
                        Name: 'Unhealthy',
                        Days: item['Unhealthy Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty2DescriptionData.push(unhealthyObject);

                    veryUnhealthyObject = {
                        Name: 'Very Unhealthy',
                        Days: item['Very Unhealthy Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty2DescriptionData.push(veryUnhealthyObject);

                    hazardousObject = {
                        Name: 'Hazardous',
                        Days: item['Hazardous Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty2DescriptionData.push(hazardousObject);

                    COObject = {
                        Name: 'CO',
                        Days: item['Days CO']
                    };
                    selectedCounty2PollutantData.push(COObject);

                    NO2Object = {
                        Name: 'NO2',
                        Days: item['Days NO2']
                    };
                    selectedCounty2PollutantData.push(NO2Object);

                    OzoneObject = {
                        Name: 'Ozone',
                        Days: item['Days Ozone']
                    };
                    selectedCounty2PollutantData.push(OzoneObject);

                    SO2Object = {
                        Name: 'SO2',
                        Days: item['Days SO2']
                    };
                    selectedCounty2PollutantData.push(SO2Object);

                    PM25Object = {
                        Name: 'PM2.5',
                        Days: item['Days PM2.5']
                    };
                    selectedCounty2PollutantData.push(PM25Object);

                    PM10Object = {
                        Name: 'PM10',
                        Days: item['Days PM10']
                    };
                    selectedCounty2PollutantData.push(PM10Object);
                }
            });

            this.aqiDescription2;
            if (document.getElementById('aqiDescription2').children.length == 0) {
                this.aqiDescription2 = new AqiDescription({
                    'parentElement': '#aqiDescription2',
                    'containerHeight': 500,
                    'containerWidth': 700
                }, selectedCounty2DescriptionData);
            } else {
                this.aqiDescription2.updateChart(selectedCounty2DescriptionData);
            }

            this.pollutant2;
            if (document.getElementById('pollutant2').children.length == 0) {
                this.pollutant2 = new Pollutant({
                    'parentElement': '#pollutant2',
                    'containerHeight': 500,
                    'containerWidth': 700
                }, selectedCounty2PollutantData);
                window.scrollTo(0, 0);
            } else {
                this.pollutant2.updateChart(selectedCounty2PollutantData);
            }
        });

        year2.addEventListener('change', (event) => {
            let selectedCounty2DescriptionData = [];
            let selectedCounty2PollutantData = [];
            this.selectedCounty2Data.forEach((item) => {
                if (item['Year'] == event.target.value) {
                    goodObject = {
                        Name: 'Good',
                        Days: item['Good Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty2DescriptionData.push(goodObject);

                    moderateObject = {
                        Name: 'Moderate',
                        Days: item['Moderate Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty2DescriptionData.push(moderateObject);

                    sensitiveObject = {
                        Name: 'Sensitive',
                        Days: item['Unhealthy for Sensitive Groups Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty2DescriptionData.push(sensitiveObject);

                    unhealthyObject = {
                        Name: 'Unhealthy',
                        Days: item['Unhealthy Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty2DescriptionData.push(unhealthyObject);

                    veryUnhealthyObject = {
                        Name: 'Very Unhealthy',
                        Days: item['Very Unhealthy Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty2DescriptionData.push(veryUnhealthyObject);

                    hazardousObject = {
                        Name: 'Hazardous',
                        Days: item['Hazardous Days'],
                        TotalDays: item['Days with AQI']
                    };
                    selectedCounty2DescriptionData.push(hazardousObject);

                    COObject = {
                        Name: 'CO',
                        Days: item['Days CO']
                    };
                    selectedCounty2PollutantData.push(COObject);

                    NO2Object = {
                        Name: 'NO2',
                        Days: item['Days NO2']
                    };
                    selectedCounty2PollutantData.push(NO2Object);

                    OzoneObject = {
                        Name: 'Ozone',
                        Days: item['Days Ozone']
                    };
                    selectedCounty2PollutantData.push(OzoneObject);

                    SO2Object = {
                        Name: 'SO2',
                        Days: item['Days SO2']
                    };
                    selectedCounty2PollutantData.push(SO2Object);

                    PM25Object = {
                        Name: 'PM2.5',
                        Days: item['Days PM2.5']
                    };
                    selectedCounty2PollutantData.push(PM25Object);

                    PM10Object = {
                        Name: 'PM10',
                        Days: item['Days PM10']
                    };
                    selectedCounty2PollutantData.push(PM10Object);
                }
            });

            this.aqiDescription2.updateChart(selectedCounty2DescriptionData);
            this.pollutant2.updateChart(selectedCounty2PollutantData);
        });
    })
    .catch(err => {
        console.error('Error loading the data');
    });