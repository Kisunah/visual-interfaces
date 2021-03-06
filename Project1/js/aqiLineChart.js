class AQILineChart {
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
            .text('AQI');

        // Append rectangles and text respective to their lines as a legend for the chart
        vis.legend = vis.chart.append('g')
            .attr('class', 'lineLegend')
            .attr('transform', `translate(${vis.width - 50},${50})`);

        vis.legend.append('rect')
            .attr('width', 10)
            .attr('height', 10)
            .attr('y', 0)
            .attr('fill', 'red');

        vis.legend.append('text')
            .attr('y', 10)
            .attr('x', 15)
            .text('Max AQI')

        vis.legend.append('rect')
            .attr('width', 10)
            .attr('height', 10)
            .attr('y', 15)
            .attr('fill', 'blue');

        vis.legend.append('text')
            .attr('y', 25)
            .attr('x', 15)
            .text('90th Percentile AQI');

        vis.legend.append('rect')
            .attr('width', 10)
            .attr('height', 10)
            .attr('y', 30)
            .attr('fill', 'green');

        vis.legend.append('text')
            .attr('y', 40)
            .attr('x', 15)
            .text('Median AQI');

        vis.trackingArea = vis.chart.append('rect')
            .attr('width', vis.width - 90)
            .attr('height', vis.height)
            .attr('fill', 'none')
            .attr('class', 'trackingArea')
            .attr('pointer-events', 'all');

        vis.updateVis();
    }

    updateVis() {
        let vis = this;

        vis.xValue = d => d['Year'];
        vis.yValueMax = d => d['Max AQI'];
        vis.yValue90 = d => d['90th Percentile AQI'];
        vis.yValueMedian = d => d['Median AQI'];

        // Create the lines for each data set
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
        vis.yScale.domain([0, d3.max(vis.data, d => parseInt(d['Max AQI']))]);

        vis.bisectDate = d3.bisector(vis.xValue).left;

        vis.renderVis();
    }

    renderVis() {
        let vis = this;

        // Append the lines to the chart
        vis.chart.selectAll('path')
            .data([vis.data])
            .join('path')
            .attr('class', 'chart-line lineMax')
            .attr('stroke', 'red')
            .attr('d', vis.lineMax);

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line line90')
            .attr('stroke', 'blue')
            .attr('d', vis.line90);

        vis.chart.append('path')
            .data([vis.data])
            .attr('class', 'chart-line lineMedian')
            .attr('stroke', 'green')
            .attr('d', vis.lineMedian);

        vis.xAxisG.call(vis.xAxis);
        vis.yAxisG.call(vis.yAxis);

        vis.tooltip = vis.chart.append('g')
            .attr('class', 'tooltip')
            .style('display', 'none');

        vis.tooltip.append('circle')
            .attr('id', 'circle1')
            .attr('r', 4);

        vis.tooltip.append('circle')
            .attr('id', 'circle2')
            .attr('r', 4);

        vis.tooltip.append('circle')
            .attr('id', 'circle3')
            .attr('r', 4);

        vis.tooltip.append('text')
            .attr('class', 'tooltipText')
            .attr('id', 'text1');

        vis.tooltip.append('text')
            .attr('class', 'tooltipText')
            .attr('id', 'text2');

        vis.tooltip.append('text')
            .attr('class', 'tooltipText')
            .attr('id', 'text3');

        vis.trackingArea
            .on('mouseenter', () => {
                vis.tooltip.style('display', 'block');
            })
            .on('mouseleave', () => {
                vis.tooltip.style('display', 'none');
            })
            .on('mousemove', (event) => {
                const xPos = d3.pointer(event, this)[0];
                let date;
                if (event.target.parentElement.parentElement.id == 'aqiChart1') {
                    date = vis.xScale.invert(xPos) - 40;
                } else {
                    date = vis.xScale.invert(xPos) - 120;
                }

                const index = vis.bisectDate(vis.data, date, 1);
                const a = vis.data[index - 1];
                const b = vis.data[index];
                const d = b && (date - a.date > b.date - date) ? b : a;

                // Update tooltip
                vis.tooltip.select('#circle1')
                    .attr('transform', `translate(${vis.xScale(parseInt(d.Year))},${vis.yScale(parseInt(d['Max AQI']))})`);

                vis.tooltip.select('#circle2')
                    .attr('transform', `translate(${vis.xScale(parseInt(d.Year))},${vis.yScale(parseInt(d['90th Percentile AQI']))})`);

                vis.tooltip.select('#circle3')
                    .attr('transform', `translate(${vis.xScale(parseInt(d.Year))},${vis.yScale(parseInt(d['Median AQI']))})`);

                vis.tooltip.select('#text1')
                    .attr('transform', `translate(${vis.xScale(parseInt(d.Year))},${(vis.yScale(parseInt(d['Max AQI'])) - 20)})`)
                    .text(`${d.Year}: ${d['Max AQI']}`);

                vis.tooltip.select('#text2')
                    .attr('transform', `translate(${vis.xScale(parseInt(d.Year))},${(vis.yScale(parseInt(d['90th Percentile AQI'])) - 20)})`)
                    .text(`${d.Year}: ${d['90th Percentile AQI']}`);

                vis.tooltip.select('#text3')
                    .attr('transform', `translate(${vis.xScale(parseInt(d.Year))},${(vis.yScale(parseInt(d['Median AQI'])) - 20)})`)
                    .text(`${d.Year}: ${d['Median AQI']}`);
            })
            .on('click', (event) => {
                const xPos = d3.pointer(event, this)[0];
                let date;
                if (event.target.parentElement.parentElement.id == 'aqiChart1') {
                    date = vis.xScale.invert(xPos) - 40;
                } else {
                    date = vis.xScale.invert(xPos) - 120;
                }

                const index = vis.bisectDate(vis.data, date, 1);
                const a = vis.data[index - 1];
                const b = vis.data[index];
                const d = b && (date - a.date > b.date - date) ? b : a;

                let year = document.getElementById('year');
                year.value = d.Year;
                year.dispatchEvent(new Event('change'));
            });
    }

    updateChart(newData) {
        let vis = this;

        vis.xScale.domain(d3.extent(newData, vis.xValue));
        vis.xAxisG.call(vis.xAxis);

        vis.yScale.domain([0, d3.max(newData, d => parseInt(d['Max AQI']))]);
        vis.yAxisG.call(vis.yAxis);

        vis.svg.selectAll('.lineMax')
            .transition().duration(2000)
            .attr('d', vis.lineMax(newData));

        vis.svg.selectAll('.line90')
            .transition().duration(2000)
            .attr('d', vis.line90(newData));

        vis.svg.selectAll('.lineMedian')
            .transition().duration(2000)
            .attr('d', vis.lineMedian(newData));

        vis.trackingArea
            .on('mouseenter', () => {
                vis.tooltip.style('display', 'block');
            })
            .on('mouseleave', () => {
                vis.tooltip.style('display', 'none');
            })
            .on('mousemove', (event) => {
                const xPos = d3.pointer(event, this)[0];
                let date;
                if (event.target.parentElement.parentElement.id == 'aqiChart1') {
                    date = vis.xScale.invert(xPos) - 40;
                } else {
                    date = vis.xScale.invert(xPos) - 120;
                }

                const index = vis.bisectDate(newData, date, 1);
                const a = newData[index - 1];
                const b = newData[index];
                const d = b && (date - a.date > b.date - date) ? b : a;

                // Update tooltip
                vis.tooltip.select('#circle1')
                    .attr('transform', `translate(${vis.xScale(parseInt(d.Year))},${vis.yScale(parseInt(d['Max AQI']))})`);

                vis.tooltip.select('#circle2')
                    .attr('transform', `translate(${vis.xScale(parseInt(d.Year))},${vis.yScale(parseInt(d['90th Percentile AQI']))})`);

                vis.tooltip.select('#circle3')
                    .attr('transform', `translate(${vis.xScale(parseInt(d.Year))},${vis.yScale(parseInt(d['Median AQI']))})`);

                vis.tooltip.select('#text1')
                    .attr('transform', `translate(${vis.xScale(parseInt(d.Year))},${(vis.yScale(parseInt(d['Max AQI'])) - 5)})`)
                    .text(`${d.Year}: ${d['Max AQI']}`);

                vis.tooltip.select('#text2')
                    .attr('transform', `translate(${vis.xScale(parseInt(d.Year))},${(vis.yScale(parseInt(d['90th Percentile AQI'])) - 25)})`)
                    .text(`${d.Year}: ${d['90th Percentile AQI']}`);

                vis.tooltip.select('#text3')
                    .attr('transform', `translate(${vis.xScale(parseInt(d.Year))},${(vis.yScale(parseInt(d['Median AQI'])) - 25)})`)
                    .text(`${d.Year}: ${d['Median AQI']}`);
            })
            .on('click', (event) => {
                const xPos = d3.pointer(event, this)[0];
                let date;
                if (event.target.parentElement.parentElement.id == 'aqiChart1') {
                    date = vis.xScale.invert(xPos) - 40;
                } else {
                    date = vis.xScale.invert(xPos) - 120;
                }

                const index = vis.bisectDate(newData, date, 1);
                const a = newData[index - 1];
                const b = newData[index];
                const d = b && (date - a.date > b.date - date) ? b : a;

                let year = document.getElementById('year');
                year.value = d.Year;
                year.dispatchEvent(new Event('change'));
            });
    }
}