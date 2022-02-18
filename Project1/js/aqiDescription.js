class AqiDescription {
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

        vis.xAxis = d3.axisBottom(vis.xScale);

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

        vis.chart.append('text')
            .attr('transform', `translate(${vis.width - 80}, ${vis.height + 10})`)
            .attr('class', 'axisLabel')
            .text('Type of Day');

        vis.chart.append('text')
            .attr('transform', 'translate(-35, -15)')
            .attr('class', 'axisLabel')
            .text('Number of Days');

        vis.updateVis();
    }

    updateVis() {
        let vis = this;

        vis.xScale.domain(vis.data.map(d => d.Name));
        vis.yScale.domain([0, 366]);

        vis.renderVis();
    }

    renderVis() {
        let vis = this;

        vis.tooltip = vis.chart.append('g')
            .attr('class', 'tooltip')
            .style('display', 'none');

        vis.tooltip.append('text')
            .attr('class', 'tooltipText')
            .attr('id', 'descriptionTooltip');

        const bar = vis.svg.selectAll('rect')
            .data(vis.data)
            .join('rect')
            .attr('width', vis.xScale.bandwidth())
            .attr('x', d => vis.xScale(d.Name))
            .attr('y', vis.yScale(0))
            .attr('pointer-events', 'all')
            .attr('transform', `translate(${vis.config.margin.left}, ${vis.config.margin.top})`)
            .on('mouseover', (event) => {
                vis.tooltip.style('display', 'block');

                let xPos = d3.pointer(event, this)[0];

                let eachBand = vis.xScale.step();
                let index;
                if (event.target.parentElement.id == 'aqiDescription1') {
                    index = Math.floor((xPos / eachBand)) - 6;
                } else {
                    index = Math.floor((xPos / eachBand)) - 18;
                }
                let val = vis.xScale.domain()[index];

                let dataItem;
                vis.data.forEach((item) => {
                    if (item.Name == val) {
                        dataItem = item;
                    }
                });

                vis.tooltip.select('#descriptionTooltip')
                    .attr('transform', `translate(${vis.xScale(val)}, ${vis.yScale(dataItem.Days) - 5})`)
                    .text(`${dataItem.Days} Days`);
            })
            .on('mouseleave', () => {
                vis.tooltip.style('display', 'none');
            })
            .transition().duration(2000)
            .attr('fill', (d) => {
                if (d.Days < 100) {
                    return 'pink';
                } else if (d.Days < 200) {
                    return 'red';
                } else if (d.Days < 300) {
                    return 'darkred';
                } else {
                    return 'black';
                }
            })
            .attr('height', d => vis.height - vis.yScale(d.Days))
            .attr('y', d => vis.yScale(d.Days));

        vis.xAxisG.call(vis.xAxis);
        vis.yAxisG.call(vis.yAxis);
    }

    updateChart(newData) {
        let vis = this;

        if (newData.length == 0) {
            for (let i = 0; i < 6; i++) {
                newData.push({
                    Days: 0
                });
            }
        }

        vis.svg.selectAll('rect')
            .data(newData)
            .transition().duration(2000)
            .attr('height', d => vis.height - vis.yScale(d.Days))
            .attr('y', d => vis.yScale(d.Days))
            .attr('fill', (d) => {
                if (d.Days < 100) {
                    return 'pink';
                } else if (d.Days < 200) {
                    return 'red';
                } else if (d.Days < 300) {
                    return 'darkred';
                } else {
                    return 'black';
                }
            });
    }
}