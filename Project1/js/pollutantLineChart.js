class PollutantLineChart {
    constructor(_config, _data) {
        this.config = {
            parentElement: _config.parentElement,
            containerWidth: _config.containerWidth || 500,
            containerHeight: _config.containerHeight || 140,
            margin: { top: 10, right: 50, bottom: 30, left: 50 }
        }

        this.data = _data;

        this.initVis();
    }

    initVis() {
        let vis = this;

        vis.width = vis.config.containerWidth - vis.config.margin.left - vis.config.margin.right;
        vis.height = vis.config.containerHeight - vis.config.margin.top - vis.config.margin.bottom;

        vis.xScale = d3.scaleLinear()
            .range([0, vis.width]);

        vis.yScale = d3.scaleLinear()
            .range([vis.height, 0])
            .nice();

        vis.xAxis = d3.axisBottom(vis.xScale)
            .tickFormat(d3.format("d"));

        vis.yAxis = d3.axisLeft(vis.yScale);

        vis.svg = d3.select(vis.config.parentElement)
            .attr('width', vis.config.containerWidth)
            .attr('height', vis.config.containerHeight);

        vis.chart = vis.svg.append('g')
            .attr('transform', `translate(${vis.config.margin.left},${vis.config.margin.top})`);

        vis.xAxisG = vis.chart.append('g')
            .attr('class', 'axis x-axis')
            .attr('transform', `translate(0,${vis.height})`);

        vis.yAxisG = vis.chart.append('g')
            .attr('class', 'axis y-axis');

        vis.updateVis();
    }

    updateVis() {
        let vis = this;

        vis.xValue = d => d['Year'];
        vis.yValueCO = d => (d['Days CO'] / d['Days with AQI']) * 100;
        vis.yValueNO2 = d => (d['Days NO2'] / d['Days with AQI']) * 100;
        vis.yValueOzone = d => (d['Days Ozone'] / d['Days with AQI']) * 100;
        vis.yValueSO2 = d => (d['Days SO2'] / d['Days with AQI']) * 100;
        vis.yValuePM25 = d => (d['Days PM2.5'] / d['Days with AQI']) * 100;
        vis.yValuePM10 = d => (d['Days PM10'] / d['Days with AQI']) * 100;

        vis.lineCO = d3.line()
            .x(d => vis.xScale(vis.xValue(d)))
            .y(d => vis.yScale(vis.yValueCO(d)));

        vis.lineNO2 = d3.line()
            .x(d => vis.xScale(vis.xValue(d)))
            .y(d => vis.yScale(vis.yValueNO2(d)));

        vis.lineOzone = d3.line()
            .x(d => vis.xScale(vis.xValue(d)))
            .y(d => vis.yScale(vis.yValueOzone(d)));

        vis.lineSO2 = d3.line()
            .x(d => vis.xScale(vis.xValue(d)))
            .y(d => vis.yScale(vis.yValueSO2(d)));

        vis.linePM25 = d3.line()
            .x(d => vis.xScale(vis.xValue(d)))
            .y(d => vis.yScale(vis.yValuePM25(d)));

        vis.linePM10 = d3.line()
            .x(d => vis.xScale(vis.xValue(d)))
            .y(d => vis.yScale(vis.yValuePM10(d)));

        vis.xScale.domain(d3.extent(vis.data, vis.xValue));
        vis.yScale.domain([0, 100]);

        vis.renderVis();
    }

    renderVis() {
        let vis = this;

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line')
            .attr('stroke', 'red')
            .attr('d', vis.lineCO);

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line')
            .attr('stroke', 'blue')
            .attr('d', vis.lineNO2);

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line')
            .attr('stroke', 'green')
            .attr('d', vis.lineOzone);

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line')
            .attr('stroke', 'purple')
            .attr('d', vis.lineSO2);

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line')
            .attr('stroke', 'orange')
            .attr('d', vis.linePM25);

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line')
            .attr('stroke', 'black')
            .attr('d', vis.linePM10);

        vis.xAxisG.call(vis.xAxis);
        vis.yAxisG.call(vis.yAxis);
    }
}