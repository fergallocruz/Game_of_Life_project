// set the dimensions and margins of the graph
var margin = {top: 10, right: 30, bottom: 20, left: 50},
    width = 800 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#my_dataviz")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// ---------------------------//
//       AXIS  AND SCALE      //
// ---------------------------//
var entidades_all = data.map((n) => {
  return n.entidad_res;
});
var entidades = [];
var concentration = {};
$.each(entidades_all, function (i, el) {
  if ($.inArray(el, entidades) === -1) {
    concentration[el] = 0;
    entidades.push(el);
  }
  concentration[el] += 1;
});

var municipios = data.map((n) => {
  return n.municipio_res;
});
var color = d3.scaleOrdinal()
    .domain(entidades)
    .range(d3.schemeSet1);

  // create a tooltip
  var Tooltip = d3.select("#my_dataviz")
    .append("div")
    .style("opacity", 0)
    .attr("class", "tooltip")
    .style("background-color", "white")
    .style("border", "solid")
    .style("border-width", "2px")
    .style("border-radius", "5px")
    .style("padding", "5px")

  // Three function that change the tooltip when user hover / move / leave a cell
  var mouseover = function(d) {
    Tooltip
      .style("opacity", 1)
    d3.select(this)
      .style("stroke", "black")
      .style("opacity", 1)
  }
  var mousemove = function(d) {
    Tooltip
      .html("There has been " + concentration[d.entidad_res] + " covid infections at " + d.entidad_res )
      .style("left", (d3.mouse(this)[0]+70) + "px")
      .style("top", (d3.mouse(this)[1]) + "px")
  }
  var mouseleave = function(d) {
    Tooltip
      .style("opacity", 0)
    d3.select(this)
      .style("stroke", "none")
      .style("opacity", 0.8)
  }

// X axis
  // Add X axis
  var x = d3.scaleBand()
      .domain(entidades)
      .range([0, width])
      .padding([0.2])
  svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x).tickSizeOuter(0));

// Add Y axis
var y = d3.scaleLinear()
  .domain([0, 200])
  .range([ height, 0]);
svg.append("g")
  .call(d3.axisLeft(y));

// Bars
svg.selectAll("mybar")
  .data(data)
  .enter()
  .append("rect")
    .attr("id", "rectBasicTooltip")
    .attr("x", function(d) { return x(d.entidad_res); })
    .attr("y", function(d) { return y(concentration[d.entidad_res]); })
    .attr("width", x.bandwidth())
    .attr("height", function(d) { return height - y(concentration[d.entidad_res]); })
    .attr("fill", function(d) { return color(d.entidad_res); })
    .on("mouseover", mouseover)
    .on("mousemove", mousemove)
    .on("mouseleave", mouseleave)

