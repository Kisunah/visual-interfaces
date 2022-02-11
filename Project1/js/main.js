d3.csv('data/aqiData.csv')
    .then(_data => {
        console.log('Data loading complete');

        let data = _data;

        let hamiltonCountyData = [];
        data.forEach((item) => {
            if (item.State == 'Ohio' && item.County == 'Hamilton') hamiltonCountyData.push(item);
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
    })
    .catch(err => {
        console.error('Error loading the data');
    });