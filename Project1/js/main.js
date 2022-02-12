d3.csv('data/aqiData.csv')
    .then(_data => {
        console.log('Data loading complete');

        let data = _data;

        let hamiltonCountyData = [];
        let hamiltonCountyData2021 = [];
        data.forEach((item) => {
            if (item.State == 'Ohio' && item.County == 'Hamilton') hamiltonCountyData.push(item);
            if (item.State == 'Ohio' && item.County == 'Hamilton' && item.Year == 2021) hamiltonCountyData2021.push(item);
        });

        let aqiLineChart = new AQILineChart({
            'parentElement': '#aqiChart',
            'containerHeight': 400,
            'containerWidth': 600
        }, hamiltonCountyData);

        let pollutantLineChart = new PollutantLineChart({
            'parentElement': '#pollutantChart',
            'containerHeight': 400,
            'containerWidth': 600
        }, hamiltonCountyData);

        let noMeasurement = new NoMeasurementChart({
            'parentElement': '#noMeasurementChart',
            'containerHeight': 400,
            'containerWidth': 600
        }, hamiltonCountyData);

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

        let aqiDescription = new AqiDescription({
            'parentElement': '#aqiDescription',
            'containerHeight': 400,
            'containerWidth': 600
        }, hamiltonCountyDataDescription);

        let pollutant2021 = new Pollutant2021({
            'parentElement': '#pollutant2021',
            'containerHeight': 400,
            'containerWidth': 600
        }, hamiltonCountyData2021);
    })
    .catch(err => {
        console.error('Error loading the data');
    });