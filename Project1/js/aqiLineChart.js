class AQILineChart {
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
        vis.yValueMax = d => d['Max AQI'];
        vis.yValue90 = d => d['90th Percentile AQI'];
        vis.yValueMedian = d => d['Median AQI'];

        vis.lineMax = d3.line()
            .x(d => vis.xScale(vis.xValue(d)))
            .y(d => vis.yScale(vis.yValueMax(d)));

        vis.line90 = d3.line()
            .x(d => vis.xScale(vis.xValue(d)))
            .y(d => vis.yScale(vis.yValue90(d)));

        vis.lineMedian = d3.line()
            .x(d => vis.xScale(vis.xValue(d)))
            .y(d => vis.yScale(vis.yValueMedian(d)));

        vis.xScale.domain(d3.extent(vis.data, vis.xValue));
        vis.yScale.domain([0, 300]);

        vis.renderVis();
    }

    renderVis() {
        let vis = this;

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line')
            .attr('stroke', 'red')
            .attr('d', vis.lineMax);

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line')
            .attr('stroke', 'blue')
            .attr('d', vis.line90);

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line')
            .attr('stroke', 'green')
            .attr('d', vis.lineMedian);

        vis.xAxisG.call(vis.xAxis);
        vis.yAxisG.call(vis.yAxis);
    }
}