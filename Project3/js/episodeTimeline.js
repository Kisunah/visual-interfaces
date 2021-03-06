class EpisodeTimeline {
    constructor(_config, _data) {
        this.config = {
            parentElement: _config.parentElement,
            containerWidth: _config.containerWidth || 2000,
            containerHeight: _config.containerHeight || 500,
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

        vis.svg.append('text')
            .text('Number of Lines for a Specific Character for Each Episode')
            .style('transform', 'translate(650px, 30px)')
            .style('font-weight', 'bold')
            .style('font-size', '150%');

        vis.updateVis();
    }

    updateVis() {
        let vis = this;

        vis.xScale.domain(vis.data.map(d => d.episode));
        vis.yScale.domain([0, d3.max(vis.data, d => d.count)]);

        vis.renderVis();
    }

    renderVis() {
        let vis = this;

        document.addEventListener('selectEpisode', (event) => {
            let selected = d3.selectAll('.selected')._groups[0][0];
            selected?.classList.toggle('selected');
            if (event.detail != '') {
                d3.select(`#${event.detail}`).classed("selected", d3.select(`#${event.detail}`).classed("selected") ? false : true);
            }
        });

        const bar = vis.svg.selectAll('rect')
            .data(vis.data)
            .join('rect')
            .attr('width', vis.xScale.bandwidth())
            .attr('x', d => vis.xScale(d.episode))
            .attr('y', d => vis.yScale(d.count))
            .attr('pointer-events', 'all')
            .attr('transform', `translate(${vis.config.margin.left}, ${vis.config.margin.top})`)
            .attr('id', d => d.episode)
            .attr('fill', function (d) {
                let season = d.episode.split('E')[0];

                switch (season) {
                    case 'S1':
                        return '#4cfd3a';
                    case 'S2':
                        return '#00ee7d';
                    case 'S3':
                        return '#00dbbf';
                    case 'S4':
                        return '#00c5fd';
                    case 'S5':
                        return '#00adff';
                    case 'S6':
                        return '#0090ff';
                    case 'S7':
                        return '#0068ff';
                    case 'S8':
                        return '#001df8';
                }
            })
            .attr('height', d => vis.height - vis.yScale(d.count))
            .on('mouseover', function (event, d) {
                d3.select(this)
                    .transition()
                    .duration(150)
                    .attr('stroke', 'black')
                    .attr('stroke-width', 2)
                    .style('cursor', 'pointer');

                d3.select('#episodeTimelineTooltip')
                    .style('opacity', 1)
                    .style('z-index', 10000)
                    .html(`<div class="tooltip-label">Episode: ${d.episode}<br>Lines: ${d.count}</div>`);
            })
            .on('mousemove', function (event) {
                d3.select('#episodeTimelineTooltip')
                    .style('left', (event.pageX + 10) + 'px')
                    .style('top', (event.pageY + 10) + 'px');
            })
            .on('mouseleave', function (event) {
                d3.select(this)
                    .transition()
                    .duration(150)
                    .attr('stroke-width', 0)
                    .style('cursor', 'default');

                d3.select('#episodeTimelineTooltip')
                    .style('left', 0)
                    .style('top', 0)
                    .style('opacity', 0);
            })
            .on('click', function (event, d) {
                const customEvent = new CustomEvent('selectEpisode', { detail: d.episode });
                document.dispatchEvent(customEvent);
            });

        vis.xAxisG.call(vis.xAxis)
            .selectAll('text')
            .style('transform', 'rotate(-90deg) translate(-6px, -13px)')
            .style('text-anchor', 'end')
            .style('font-weight', 'bold');

        vis.yAxisG.call(vis.yAxis);
    }

    updateChart(newData) {
        let vis = this;

        vis.yScale.domain([0, d3.max(vis.data, d => d.count)]);
        vis.yAxisG.call(vis.yAxis);

        vis.svg.selectAll('rect')
            .data(newData)
            .transition()
            .duration(1000)
            .attr('y', d => vis.yScale(d.count))
            .attr('height', d => vis.height - vis.yScale(d.count));
    }
}