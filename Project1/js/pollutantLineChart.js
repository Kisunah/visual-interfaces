class PollutantLineChart {
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

        vis.xScale = d3.scaleLinear()
            .range([0, vis.width - 100]);

        vis.yScale = d3.scaleLinear()
            .range([vis.height, 0])
            .nice();

        vis.xAxis = d3.axisBottom(vis.xScale)
            .ticks(5)
            .tickFormat(d3.format("d"));

        vis.yAxis = d3.axisLeft(vis.yScale);

        vis.svg = d3.select(vis.config.parentElement)
            .attr('width', vis.config.containerWidth)
            .attr('height', vis.config.containerHeight);

        // Ensures the old ticks are removed from the x-axis before updating the charts data
        vis.svg.selectAll('*').data([]).exit().remove();

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
            .text('Percentage of Pollutant');

        // Append rectangles and text respective to their lines as a legend for the chart
        vis.legend = vis.chart.append('g')
            .attr('class', 'lineLegend')
            .attr('transform', `translate(${vis.width - 50}, ${50})`);

        vis.legend.append('rect')
            .attr('width', 10)
            .attr('height', 10)
            .attr('y', 0)
            .attr('fill', 'red');

        vis.legend.append('text')
            .attr('y', 10)
            .attr('x', 15)
            .text('CO');

        vis.legend.append('rect')
            .attr('width', 10)
            .attr('height', 10)
            .attr('y', 15)
            .attr('fill', 'blue');

        vis.legend.append('text')
            .attr('y', 25)
            .attr('x', 15)
            .text('NO2');

        vis.legend.append('rect')
            .attr('width', 10)
            .attr('height', 10)
            .attr('y', 30)
            .attr('fill', 'green');

        vis.legend.append('text')
            .attr('y', 40)
            .attr('x', 15)
            .text('Ozone');

        vis.legend.append('rect')
            .attr('width', 10)
            .attr('height', 10)
            .attr('y', 45)
            .attr('fill', 'purple');

        vis.legend.append('text')
            .attr('y', 55)
            .attr('x', 15)
            .text('SO2');

        vis.legend.append('rect')
            .attr('width', 10)
            .attr('height', 10)
            .attr('y', 60)
            .attr('fill', 'orange');

        vis.legend.append('text')
            .attr('y', 70)
            .attr('x', 15)
            .text('PM2.5');

        vis.legend.append('rect')
            .attr('width', 10)
            .attr('height', 10)
            .attr('y', 75)
            .attr('fill', 'black');

        vis.legend.append('text')
            .attr('y', 85)
            .attr('x', 15)
            .text('PM10');

        vis.updateVis();
    }

    updateVis() {
        let vis = this;

        vis.svg.selectAll('path').data([]).exit().remove();

        vis.xValue = d => d['Year'];
        vis.yValueCO = d => (d['Days CO'] / d['Days with AQI']) * 100;
        vis.yValueNO2 = d => (d['Days NO2'] / d['Days with AQI']) * 100;
        vis.yValueOzone = d => (d['Days Ozone'] / d['Days with AQI']) * 100;
        vis.yValueSO2 = d => (d['Days SO2'] / d['Days with AQI']) * 100;
        vis.yValuePM25 = d => (d['Days PM2.5'] / d['Days with AQI']) * 100;
        vis.yValuePM10 = d => (d['Days PM10'] / d['Days with AQI']) * 100;

        vis.xScale.domain(d3.extent(vis.data, vis.xValue));
        vis.yScale.domain([0, 100]);

        // Create the lines for each data set
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

        vis.renderVis();
    }

    renderVis() {
        let vis = this;

        // Append the lines to the chart
        vis.chart.selectAll('path')
            .data([vis.data])
            .join('path')
            .attr('class', 'chart-line co')
            .attr('stroke', 'red')
            .attr('d', vis.lineCO);

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line no2')
            .attr('stroke', 'blue')
            .attr('d', vis.lineNO2);

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line ozone')
            .attr('stroke', 'green')
            .attr('d', vis.lineOzone);

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line so2')
            .attr('stroke', 'purple')
            .attr('d', vis.lineSO2);

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line pm25')
            .attr('stroke', 'orange')
            .attr('d', vis.linePM25);

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line pm10')
            .attr('stroke', 'black')
            .attr('d', vis.linePM10);

        vis.xAxisG.call(vis.xAxis);
        vis.yAxisG.call(vis.yAxis);
    }

    updateChart(newData) {
        let vis = this;

        vis.xScale.domain(d3.extent(newData, vis.xValue));
        vis.xAxisG.call(vis.xAxis);

        vis.svg.selectAll('.co')
            .transition().duration(2000)
            .attr('d', vis.lineCO(newData));

        vis.svg.selectAll('.no2')
            .transition().duration(2000)
            .attr('d', vis.lineNO2(newData));

        vis.svg.selectAll('.ozone')
            .transition().duration(2000)
            .attr('d', vis.lineOzone(newData));

        vis.svg.selectAll('.so2')
            .transition().duration(2000)
            .attr('d', vis.lineSO2(newData));

        vis.svg.selectAll('.pm25')
            .transition().duration(2000)
            .attr('d', vis.linePM25(newData));

        vis.svg.selectAll('.pm10')
            .transition().duration(2000)
            .attr('d', vis.linePM10(newData));
    }
}