class WordCloud {
    constructor(_words, _wordMap, _character) {
        this.words = _words;
        this.wordMap = _wordMap;
        this.character = _character;

        this.initVis();
    }

    initVis() {
        let vis = this;

        let layout = d3.layout.cloud()
            .size([2000, 800])
            .words(vis.words.map(function (d) {
                if (vis.character == 'HOUSE') {
                    return { 
                        text: d, size: Math.round(vis.wordMap[d]/10)
                    };
                } else {
                    let size = Math.round(vis.wordMap[d]/3);
                    if (size < 10) size = 10;
                    return {
                        text: d, size: size
                    };
                }
            }))
            .timeInterval(10)
            .padding(2)
            .rotate(function () { return ~~(Math.random() * 2) * 90; })
            .font("Impact")
            .fontSize(function (d) { return d.size; })
            .on("end", draw);

        layout.start();

        function draw(words) {
            d3.select("#wordCloudContainer").append("svg")
                .attr('id', 'wordCloud')
                .attr("width", layout.size()[0])
                .attr("height", layout.size()[1])
                .append("g")
                .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
                .selectAll("text")
                .data(words)
                .enter().append("text")
                .style("font-size", function (d) { return d.size + "px"; })
                .style("font-family", "Impact")
                .style('fill', (d) => {
                    if (d.size > 90) return '#001df8';
                    else if (d.size > 80) return '#0068ff';
                    else if (d.size > 70) return '#0090ff';
                    else if (d.size > 60) return '#00adff';
                    else if (d.size > 50) return '#00c5fd';
                    else if (d.size > 40) return '#00dbbf';
                    else if (d.size > 30) return '#00ee7d';
                    else if (d.size > 20) return '#4cfd3a';
                    else return 'black';
                })
                .style('margin', '0 auto')
                .attr("text-anchor", "middle")
                .attr("transform", function (d) {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                })
                .text(function (d) { return d.text; });
        }
    }
}