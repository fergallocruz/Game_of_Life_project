info_set = {};
estados = [];
data.map((n) => {
  if (!estados.includes(n.entidad_um)) {
    estados.push(n.entidad_um);
    info_set[n.entidad_um] = {
      ESTATAL: 0,
      IMSS: 0,
      "IMSS-BIENESTAR": 0,
      ISSSTE: 0,
      PEMEX: 0,
      PRIVADA: 0,
      SSA: 0,
      UNIVERSITARIO: 0,
    };
  }
  info_set[n.entidad_um][n.sector] += 1;
});

// set the dimensions and margins of the graph
var margin = { top: 10, right: 10, bottom: 20, left: 10 },
  width = 1000 - margin.left - margin.right,
  height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3
  .select("#my_dataviz")
  .append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// List of subgroups = header of the csv files = soil condition here
var subgroups = Object.keys(info_set[estados[0]]);

// List of groups = species here = value of the first column called group -> I show them on the X axis
var groups = d3
  .map(info_set, function (d) {
    return d.key;
  })
  .keys();

// Add X axis
var x = d3.scaleBand().domain(groups).range([0, width]).padding([0.02]);

svg
  .append("g")
  .attr("transform", "translate(0," + height + ")")
  .call(d3.axisBottom(x).tickSize(0));

// Add Y axis
var y = d3.scaleLinear().domain([0, 100]).range([height, 0]);
svg.append("g").call(d3.axisLeft(y));

// Another scale for subgroup position?
var xSubgroup = d3
  .scaleBand()
  .domain(subgroups)
  .range([0, x.bandwidth()])
  .padding([0.05]);

// color palette = one color per subgroup
var color = d3.scaleOrdinal().domain(subgroups).range([
  "#63a6d6", // <= lower bound of our color scale
  "#124488", // <= upper bound of our color scale
]);

// Show the bars
svg
  .append("g")
  .selectAll("g")
  // Enter in data = loop group per group
  .data(estados)
  .enter()
  .append("g")
  .attr("transform", function (d) {
    return "translate(" + x(d) + ",0)";
  })
  .selectAll("rect")
  .data(function (d) {
    return subgroups.map(function (key) {
      return { key: key, value: info_set[d][key] };
    });
  })
  .enter()
  .append("rect")
  .attr("x", function (d) {
    return xSubgroup(d.key);
  })
  .attr("y", function (d) {
    return y(d.value);
  })
  .attr("width", xSubgroup.bandwidth())
  .attr("height", function (d) {
    return height - y(d.value);
  })
  .attr("fill", function (d) {
    return color(d.key);
  });

var svgLegned3 = d3
  .select("#legends")
  .append("svg")
  .attr("width", width)
  .attr("height", 100);

var legendVals1 = d3
  .scaleOrdinal()
  .domain(subgroups)
  .range(
    subgroups.map(function (key) {
      return color(key);
    })
  );
var legend3 = svgLegned3
  .selectAll("#legends")
  .data(legendVals1.domain())
  .enter()
  .append("g")
  .attr("class", "legends3")
  .attr("transform", function (d, i) {
    if(i%2){
      return "translate(" +  ((xSubgroup(d)*22)-100) + ","+ 50+")";
    }
    return "translate(" +  ((xSubgroup(d)*22)-100) + ",0)";
  });

legend3
  .append("rect")
  .attr("x", 0)
  .attr("y", 0)
  .attr("width", 10)
  .attr("height", 10)
  .style("fill", function (d, i) {
    return color(i);
  });

legend3
  .append("text")
  .attr("x", 20)
  .attr("y", 10)
  //.attr("dy", ".35em")
  .text(function (d, i) {
    return d;
  })
  .attr("class", "textselected")
  .style("text-anchor", "start")
  .style("font-size", 15);
