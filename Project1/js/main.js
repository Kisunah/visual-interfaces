d3.csv('data/aqiData.csv')
    .then(_data => {
        console.log('Data loading complete');

        let data = _data;

        let hamiltonCountyData = [];
        let orangeCountyData = [];
        let hamiltonCountyData2021 = [];
        let stateList = [];
        data.forEach((item) => {
            if (item.State == 'Ohio' && item.County == 'Hamilton') hamiltonCountyData.push(item);
            if (item.State == 'California' && item.County == 'Orange') orangeCountyData.push(item);

            if (item.State == 'Ohio' && item.County == 'Hamilton' && item.Year == 2021) hamiltonCountyData2021.push(item);

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

        county1.addEventListener('change', (event) => {
            let selectedCounty1Data = [];
            data.forEach((item) => {
                if (item.State == state1.value && item.County == event.target.value) selectedCounty1Data.push(item);
            });

            let aqiLineChart = new AQILineChart({
                'parentElement': '#aqiChart1',
                'containerHeight': 500,
                'containerWidth': 700
            }, selectedCounty1Data);

            let pollutantLineChart1 = new PollutantLineChart({
                'parentElement': '#pollutantChart1',
                'containerHeight': 500,
                'containerWidth': 700
            }, selectedCounty1Data);

            let NoMeasurementChart1 = new NoMeasurementChart({
                'parentElement': '#noMeasurementChart1',
                'containerHeight': 500,
                'containerWidth': 700
            }, selectedCounty1Data);
        });

        county2.addEventListener('change', (event) => {
            let selectedCounty2Data = [];
            data.forEach((item) => {
                if (item.State == state2.value && item.County == event.target.value) selectedCounty2Data.push(item);
            });

            let aqiLineChart2 = new AQILineChart({
                'parentElement': '#aqiChart2',
                'containerHeight': 500,
                'containerWidth': 700
            }, selectedCounty2Data);

            let pollutantLineChart2 = new PollutantLineChart({
                'parentElement': '#pollutantChart2',
                'containerHeight': 500,
                'containerWidth': 700
            }, selectedCounty2Data);

            let NoMeasurementChart2 = new NoMeasurementChart({
                'parentElement': '#noMeasurementChart2',
                'containerHeight': 500,
                'containerWidth': 700
            }, selectedCounty2Data);

        });

        let aqiLineChart1 = new AQILineChart({
            'parentElement': '#aqiChart1',
            'containerHeight': 500,
            'containerWidth': 700
        }, []);

        let pollutantLineChart1 = new PollutantLineChart({
            'parentElement': '#pollutantChart1',
            'containerHeight': 500,
            'containerWidth': 700
        }, []);

        let noMeasurement1 = new NoMeasurementChart({
            'parentElement': '#noMeasurementChart1',
            'containerHeight': 500,
            'containerWidth': 700
        }, []);

        let aqiLineChart2 = new AQILineChart({
            'parentElement': '#aqiChart2',
            'containerHeight': 500,
            'containerWidth': 700
        }, []);

        let pollutantLineChart2 = new PollutantLineChart({
            'parentElement': '#pollutantChart2',
            'containerHeight': 500,
            'containerWidth': 700
        }, []);

        let noMeasurement2 = new NoMeasurementChart({
            'parentElement': '#noMeasurementChart2',
            'containerHeight': 500,
            'containerWidth': 700
        }, []);

        let hamiltonCountyDataDescription = [];
        hamiltonCountyData.forEach((item) => {
            if (item['Year'] == 2021) {
                goodObject = {
                    Name: 'Good Days',
                    Days: item['Good Days'],
                    TotalDays: item['Days with AQI']
                };
                hamiltonCountyDataDescription.push(goodObject);

                moderateObject = {
                    Name: 'Moderate Days',
                    Days: item['Moderate Days'],
                    TotalDays: item['Days with AQI']
                };
                hamiltonCountyDataDescription.push(moderateObject);

                sensitiveObject = {
                    Name: 'Unhealthy for Sensitive Groups Days',
                    Days: item['Unhealthy for Sensitive Groups Days'],
                    TotalDays: item['Days with AQI']
                };
                hamiltonCountyDataDescription.push(sensitiveObject);

                unhealthyObject = {
                    Name: 'Unhealthy Days',
                    Days: item['Unhealthy Days'],
                    TotalDays: item['Days with AQI']
                };
                hamiltonCountyDataDescription.push(unhealthyObject);

                veryUnhealthyObject = {
                    Name: 'Very Unhealthy Days',
                    Days: item['Very Unhealthy Days'],
                    TotalDays: item['Days with AQI']
                };
                hamiltonCountyDataDescription.push(veryUnhealthyObject);

                hazardousObject = {
                    Name: 'Hazardous Days',
                    Days: item['Hazardous Days'],
                    TotalDays: item['Days with AQI']
                };
                hamiltonCountyDataDescription.push(hazardousObject);

                COObject = {
                    Name: 'CO',
                    Days: item['Days CO']
                };
                hamiltonCountyData2021.push(COObject);

                NO2Object = {
                    Name: 'NO2',
                    Days: item['Days NO2']
                };
                hamiltonCountyData2021.push(NO2Object);

                OzoneObject = {
                    Name: 'Ozone',
                    Days: item['Days Ozone']
                };
                hamiltonCountyData2021.push(OzoneObject);

                SO2Object = {
                    Name: 'SO2',
                    Days: item['Days SO2']
                };
                hamiltonCountyData2021.push(SO2Object);

                PM25Object = {
                    Name: 'PM2.5',
                    Days: item['Days PM2.5']
                };
                hamiltonCountyData2021.push(PM25Object);

                PM10Object = {
                    Name: 'PM10',
                    Days: item['Days PM10']
                };
                hamiltonCountyData2021.push(PM10Object);
            }
        });

        let aqiDescription1 = new AqiDescription({
            'parentElement': '#aqiDescription1',
            'containerHeight': 500,
            'containerWidth': 700
        }, hamiltonCountyDataDescription);

        let pollutant20211 = new Pollutant2021({
            'parentElement': '#pollutant20211',
            'containerHeight': 500,
            'containerWidth': 700
        }, hamiltonCountyData2021);

        let aqiDescription = new AqiDescription({
            'parentElement': '#aqiDescription2',
            'containerHeight': 500,
            'containerWidth': 700
        }, hamiltonCountyDataDescription);

        let pollutant2021 = new Pollutant2021({
            'parentElement': '#pollutant20212',
            'containerHeight': 500,
            'containerWidth': 700
        }, hamiltonCountyData2021);
    })
    .catch(err => {
        console.error('Error loading the data');
    });