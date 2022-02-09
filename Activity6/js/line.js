class Line {

  constructor(_config) {
    this.config = {
      parentElement: _config.parentElement,
      containerWidth: _config.containerWidth || 500,
      containerHeight: _config.containerHeight || 140,
      margin: { top: 10, bottom: 30, right: 10, left: 30 }
    }

    // Call a class function
    this.initVis();
  }

  initVis() {
    let vis = this;

    vis.width = vis.config.containerWidth - vis.config.margin.left - vis.config.margin.right;
    vis.height = vis.config.containerHeight - vis.config.margin.top - vis.config.margin.bottom;

    vis.svg = d3.select(vis.config.parentElement)
      .attr('width', vis.config.containerWidth)
      .attr('height', vis.config.containerHeight);

    vis.chart = vis.svg.append('g')
      .attr('transform', `translate(${vis.config.margin.left}, ${vis.config.margin.top})`);

    vis.xScale = d3.scaleTime()
      .range([0, vis.width]);
    
    vis.yScale = d3.scaleTime()
      .range([0, vis.height]);

    vis.xAxis = d3.axisBottom(vis.xScale)
      .ticks(6)
      .tickSizeOuter(0)
      .tickPadding(10);
    vis.yAxis = d3.axisTop(vis.yScale)
      .ticks(6)
      .tickSizeOuter(0)
      .tickPadding(10);

    vis.xAxixGroup = vis.chart.append('g')
      .attr('class', 'axis x-axis')
      .call(vis.xAxis);
    vis.yAxisGroup = vis.chart.append('g')
      .attr('class', 'axis y-axis')
      .call(vis.yAxis);

    updateVis(); //leave this empty for now...
  }


  //leave this empty for now
 updateVis() { 
   
   renderVis(); 

 }


 //leave this empty for now...
 renderVis() { 

  }



}