class CharacterEpisodeCountChart {
    constructor(_config, _data) {
        this.config = {
            parentElement: _config.parentElement,
            containerWidth: _config.containerWidth || 500,
            containerHeight: _config.containerHeight || 350,
            margin: { top: 50, right: 50, bottom: 50, left: 50 }
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
            .range([0, vis.width]);

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

        vis.yAxisG.append('text')
            .text('Number of Episodes')
            .style('transform', 'translate(-50px, 150px) rotate(90deg)')

        vis.svg.append('text')
            .text('Number of Episodes Each Character Appears In')
            .style('transform', 'translate(0px, 30px)')
            .style('font-weight', 'bold')
            .style('font-size', '150%');

        vis.updateVis();
    }

    updateVis() {
        let vis = this;

        vis.xScale.domain(vis.data.map(d => d.character));
        vis.yScale.domain([0, d3.max(vis.data, d => d.count)]);

        vis.renderVis();
    }

    renderVis() {
        let vis = this;

        const bar = vis.svg.selectAll('rect')
            .data(vis.data)
            .join('rect')
            .attr('width', vis.xScale.bandwidth())
            .attr('x', d => vis.xScale(d.character))
            .attr('y', d => vis.yScale(d.count))
            .attr('pointer-events', 'all')
            .attr('transform', `translate(${vis.config.margin.left}, ${vis.config.margin.top})`)
            .attr('fill', '#5f00f8')
            .attr('height', d => vis.height - vis.yScale(d.count))
            .on('mouseover', function (event, d) {
                d3.select(this)
                    .transition()
                    .duration(150)
                    .attr('stroke', 'black')
                    .attr('stroke-width', 2)
                    .style('cursor', 'pointer');

                d3.select('#characterEpisodeCountTooltip')
                    .style('opacity', 1)
                    .style('z-index', 10000)
                    .html(`<div class="tooltip-label">Character: ${d.character}<br>Episodes: ${d.count}</div>`);
            })
            .on('mousemove', function (event) {
                d3.select('#characterEpisodeCountTooltip')
                    .style('left', (event.pageX + 10) + 'px')
                    .style('top', (event.pageY + 10) + 'px');
            })
            .on('mouseleave', function (event) {
                d3.select(this)
                    .transition()
                    .duration(150)
                    .attr('stroke-width', 0)
                    .style('cursor', 'default');

                d3.select('#characterEpisodeCountTooltip')
                    .style('left', 0)
                    .style('top', 0)
                    .style('opacity', 0);
            })
            .on('click', function(event, d) {
                const customEvent = new CustomEvent('selectCharacter', { detail: d.character} );
                document.dispatchEvent(customEvent);
            });

        vis.xAxisG.call(vis.xAxis)
            .selectAll('text')
            .attr('transform', 'rotate(-45)')
            .style('text-anchor', 'end')
            .style('font-weight', 'bold');

        vis.yAxisG.call(vis.yAxis);
    }
}