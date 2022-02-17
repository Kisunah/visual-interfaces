class NoMeasurementChart {
    constructor(_config, _data) {
        this.config = {
            parentElement: _config.parentElement,
            containerWidth: _config.containerWidth || 500,
            containerHeight: _config.containerHeight || 140,
            margin: { top: 50, right: 50, bottom: 30, left: 50 }
        }

        this.data = _data;

        this.initVis();
    }

    initVis() {
        let vis = this;

        vis.width = vis.config.containerWidth - vis.config.margin.left - vis.config.margin.right;
        vis.height = vis.config.containerHeight - vis.config.margin.top - vis.config.margin.bottom;

        vis.xScale = d3.scaleBand()
            .padding(0.1)
            .range([0, vis.width - 100]);

        vis.yScale = d3.scaleLinear()
            .range([vis.height, 0])
            .nice();

        vis.xAxis = d3.axisBottom(vis.xScale)
            .tickFormat(d3.format('d'));

        vis.yAxis = d3.axisLeft(vis.yScale);

        vis.svg = d3.select(vis.config.parentElement)
            .attr('width', vis.config.containerWidth)
            .attr('height', vis.config.containerHeight);

        // Ensures the old ticks are removed from the x-axis before updating the charts data        
        vis.svg.selectAll('.axis').data([]).exit().remove();

        vis.chart = vis.svg.append('g')
            .attr('transform', `translate(${vis.config.margin.left},${vis.config.margin.top})`);

        vis.xAxisG = vis.chart.append('g')
            .attr('class', 'axis x-axis')
            .attr('transform', `translate(0,${vis.height})`);

        vis.yAxisG = vis.chart.append('g')
            .attr('class', 'axis y-axis');

        // Append a lable for the x-axis
        vis.chart.append('text')
            .attr('transform', `translate(${vis.width - 80}, ${vis.height + 10})`)
            .attr('class', 'axisLabel')
            .text('Years');

        // Append a label for the y-axis
        vis.chart.append('text')
            .attr('transform', `translate(-35, -15)`)
            .attr('class', 'axisLabel')
            .text('Number of Days Without a Measurement');

        vis.updateVis();
    }

    updateVis() {
        let vis = this;

        // vis.xScale.domain(vis.data.map(d => d['Year']));
        let years = [];
        for (let i = 1980; i < 2021; i++) {
            years.push(i);
        }
        vis.xScale.domain(years);
        vis.yScale.domain([0, 366]);

        // Function for dividing up the years to be applied to the axis so there aren't too many that are overlapping each other
        let ticks = [];
        vis.data.forEach((item, index) => {
            if (index % 5 == 0) {
                ticks.push(item.Year);
            }
        });

        vis.xAxis.tickValues(ticks);

        vis.renderVis();
    }

    renderVis() {
        let vis = this;

        const bar = vis.svg.selectAll('rect')
            .data(vis.data)
            .join('rect')
            .attr('x', d => vis.xScale(parseInt(d['Year'])))
            .attr('y', d => vis.yScale(vis.isLeapYear(parseInt(d['Year'])) - parseInt(d['Days with AQI'])))
            .attr('transform', `translate(${vis.config.margin.left}, ${vis.config.margin.top})`)
            .attr('fill', (d) => {
                if (vis.isLeapYear(parseInt(d['Year'])) - d['Days with AQI'] < 100) {
                    return 'lightblue';
                } else if (vis.isLeapYear(parseInt(d['Year'])) - d['Days with AQI'] < 200) {
                    return 'blue';
                } else if (vis.isLeapYear(parseInt(d['Year'])) - d['Days with AQI'] < 300) {
                    return '#11143d';
                } else {
                    return 'black';
                }
            })
            .attr('width', vis.xScale.bandwidth())
            .attr('height', d => vis.height - vis.yScale(vis.isLeapYear(parseInt(d['Year'])) - d['Days with AQI']));
        vis.xAxisG.call(vis.xAxis);
        vis.yAxisG.call(vis.yAxis);
    }

    isLeapYear(year) {
        if (year % 400 === 0) return 366;
        if (year % 100 === 0) return 365;
        if (year % 4 === 0) return 366;
        else return 365
    }

    updateChart(newData) {
        let vis = this;

        vis.svg.selectAll('rect')
            .data(newData)
            .transition().duration(2000)
            .attr('height', d => vis.height - vis.yScale(vis.isLeapYear(parseInt(d['Year'])) - d['Days with AQI']))
            .attr('y', d => vis.yScale(vis.isLeapYear(parseInt(d['Year'])) - parseInt(d['Days with AQI'])))
    }
}