
//-----------------------------------option-------------------------------------

var file="data_fdi.csv";
var SHOW_NAME = true;
var SHOW_VALUE = true;
var SHOW_PERCENT = true;
var SHOW_SI_VIZ= true;
var SHOW_SCIENTIFIC_VIZ= false;

var symbol= "\u0024"   //look of unicode symbol list at http://www.fileformat.info/info/unicode/category/index.html
var Size=750

var with_units = true
var with_title = true
var title="Foreign Direct Investment (FDI) of G20 members"


var show_tooltip_for_small_bubbles = true

//-------------------------------------------------------------------------------

var gloabalObj = []

d3.text(file, function(r){

    var firstline = r.split('\n')[0]
    
    if(!firstline.startsWith("name,value")){

        d3.text(file, function(r){

            var result = "name,value,color\n" + r;  
            gloabalObj = d3.csv.parse(result);
            myDataIsReady()

        });
        
    }else{
            d3.csv(file, function(data) {
        
                gloabalObj = data
                myDataIsReady()
            });
    }

});


function myDataIsReady() {

    var tots = d3.sum(gloabalObj, function(d) { 
            return d.value; 
        });

    gloabalObj.forEach(function(d) {
        d.percentage = d.value  / tots;
		
    });
	
	
    var root = {children: gloabalObj};

    var bubble = d3.layout.pack()
                          .sort(null)
                          .size([Size,Size])
                          .padding(1.5);


    bubble.nodes(root)


    var svg = d3.select("body")
                .append("svg")
                .attr("width",Size)
                .attr("height", Size)
                .attr("class","bubble");


    if(with_title){

            svg.append("text")
                    .attr("x", 200*Size/1500)
                    .attr("y", 100*Size/1500) 
                    .style("font-size", 56*Size/1500 )  
                    .text(title);
    }

    // Define the div for the tooltip
    var div = d3.select("body").append("div")	
        .attr("class", "tooltip")				
        .style("opacity", 0);

    var node = svg.selectAll(".node")
                .data(bubble.nodes(root)
                .filter(function(d){ return !d.children;}))
                .enter()
                .append("g")
                .attr("class","node")
                // .attr("title",function(d){return d.name})
                .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; })
                .on("mouseover", function(d) {
                    // console.log(d.r <= 20*Size/350)
                    // console.log((d.r) *13/(68*Size/750) < d.value.toFixed(0).length)
                    // console.log(d.r <= 30*Size/350)
                    

                    if( (d.r <= 20*Size/350 || (d.r) *13/(68*Size/750) < d.value.toFixed(0).length || d.r <= 30*Size/350 ) && show_tooltip_for_small_bubbles)		
                        div.transition()		
                            .duration(200)		
                            .style("opacity", 1);		
                        div.html(d.name+'<br/>'+viz(d.value.toFixed(0).toString()) +" "+ symbol +'<br/>' + (d.percentage*100 ).toFixed(1).toString() + " %") 
                            .style("left", (d.x+d.r) + "px")		
                            .style("top", (d.y-d.r) + "px");	
                        })					
                .on("mouseout", function(d) {
                     if( (d.r <= 20*Size/350 || (d.r) *13/(68*Size/750) < d.value.toFixed(0).length || d.r <= 30*Size/350 ) && show_tooltip_for_small_bubbles)		
                        div.transition()		
                            .duration(500)		
                            .style("opacity", 0);	
                });

    var colour = d3.scale.category10();
    var circle = node.append("circle")
        .attr("r", function(d) { return d.r; })
        .style("fill", function(d) { 
            return d.color ? d.color : colour(d.r); 
            });

              

	

	function getTextWidth(text, fontSize, fontFace) {
        var a = document.createElement('canvas');
        var b = a.getContext('2d');
        b.font = fontSize + 'px ' + fontFace;
        return b.measureText(text).width;
    } 
        

	function getMinLength(text,radius) {
        
        l= text.length

        for(i=l; i> 0; i--){
            
            t = text.substring(0,i) +".."
            if(getTextWidth(t, (Size/50), 'Helvetica Neue') <= radius*2) return i-5
        }
    } 

    function between(x, min, max) {
    return x >= min && x <= max;
    }

    function si_viz(v){
        // console.log(v)
        var l = v.length

        if(between(l, 4, 6) ){
            return v.substring(0,l-3) + ' K'

        }else if( between(l, 7, 9) ){
            return v.substring(0,l-6) + ' M'
                
        }else if(between(l, 10, 13)){
            return v.substring(0,l-9) + ' G'	              
        }
		else if(between(l, 0, 4)){
            return v.substring(0,4)
		}
	}

	
	function scientific_viz(v){	
		var v =parseFloat(v)
		// console.log(v)
		return v.toExponential(2).replace("e",'\u22c5'+'10').substr(0, 7)+'^'+v.toExponential(0).substr(3, 10)
	}	
			
	function viz(dv){
		if(SHOW_SI_VIZ){
			// console.log(SHOW_SI_VIZ)
			return si_viz(dv)
		}
		if(SHOW_SCIENTIFIC_VIZ){
		    // console.log(SHOW_SCIENTIFIC_VIZ)
			return scientific_viz(dv)	
		}
		else{return dv}
	}		

	if(SHOW_NAME){
				

        	node.append("text")
				.attr("dy", function(){if(SHOW_VALUE)return '-1em'; else return '0em'})
				.style("text-anchor", "middle")
				.style("font-family","Helvetica Neue")
				.style("font-weight","Bold")
                .style("font-size",Size/50)
				.attr("class","n_name")
                .text(function(d) {
                    
                    if(d.r <= 20*Size/350){
                        return ""
                    }else{
                        never_fit = true

                        text_width = getTextWidth(d.name, (Size/50), 'Helvetica Neue')
                        // console.log(d.name,' ',text_width+5 ,'<=', d.r*2)
                        if(text_width+5 <= d.r*2){
                            never_fit = false
                        }
                        
                        if(never_fit){
                            // console.log(d.name)
                            // console.log(getMinLength(d.name,d.r))
                            return (d.name.substring(0,getMinLength(d.name,d.r))+"..")
                        }
                        else return (d.name)
                    }

                })
                .attr("fill",function(d){ 
                        if(d.color){

                            r = hexToRgb(d.color).r 
                            g = hexToRgb(d.color).g
                            b = hexToRgb(d.color).b 

                            var o = Math.round(((parseInt(r) * 299) + (parseInt(g) * 587) + (parseInt(b) * 114)) /1000);
                        
                            if (o > 125 )
                                    col = '#000000' 
                            else col = '#ffffff'

                            return col
                        }

                });
	}

	if(SHOW_VALUE){
			node.append("text")
				.attr("dy", "0.3em")
				.style("text-anchor", "middle")
				.style("font-size",(Size/45).toFixed(0).toString()+"px")
				.attr("class","n_val")
                .text(function(d) {

                    
                    x = ( (d.r) *13/(68*Size/750)) 
                    if(x>= d.value.toFixed(0).length){
                        if(with_units) return (viz(d.value.toFixed(0).toString()) +" "+ symbol)
                        else return (d.value.toFixed(0).toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ") +" "+ symbol)
                        
                    }
                    else{
                        return ("")
                    } ; 
                })
                .attr("fill",function(d){ 
                        if(d.color){

                            r = hexToRgb(d.color).r 
                            g = hexToRgb(d.color).g
                            b = hexToRgb(d.color).b 

                            var o = Math.round(((parseInt(r) * 299) + (parseInt(g) * 587) + (parseInt(b) * 114)) /1000);
                        
                            if (o > 125 )
                                    col = '#000000' 
                            else col = '#ffffff'
                            return col
                        }

                });
	}

	if(SHOW_PERCENT){

			node.append("text")
				.attr("dy",function(){if(SHOW_VALUE)return '1.8em'; else return '1.6em'})
				.style("text-anchor", "middle")
				.style("font-size",(Size/50).toFixed(0).toString()+"px")
				.attr("class","n_percent")
                .text(function(d) {
                    x = ( (d.r) * 13 /(68*Size/750)) 
                    percent = (d.percentage*100 ).toFixed(1).toString() + " %"
                    if(!(d.r <= 20*Size/350) && SHOW_VALUE == false){
                            return (percent)
                    }
                    else if(d.r <= 30*Size/350){
                        // console.log(d.name)
                        return ""
                        
                    }else{
                        never_fit = true

                        text_width = getTextWidth(percent, (Size/50), 'Helvetica Neue')

                        if(text_width+3 <= d.r*2){
                            never_fit = false
                        }
                        
                        if(never_fit){
                            // console.log(d.name)
                            // console.log(getMinLength(d.name,d.r))
                            return (d.name.substring(0,getMinLength(percent,d.r))+"..")
                        }
                        else return (percent)
                    }
                })
                .attr("fill",function(d){ 
                        if(d.color){

                            r = hexToRgb(d.color).r 
                            g = hexToRgb(d.color).g
                            b = hexToRgb(d.color).b 

                            var o = Math.round(((parseInt(r) * 299) + (parseInt(g) * 587) + (parseInt(b) * 114)) /1000);
                        
                            if (o > 125 )
                                    col = '#000000' 
                            else col = '#ffffff'

                            return col
                        }

                });


	}


    function hexToRgb(hex) {
        var shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
        hex = hex.replace(shorthandRegex, function(m, r, g, b) {
            return r + r + g + g + b + b;
        });

        var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return result ? {
            r: parseInt(result[1], 16),
            g: parseInt(result[2], 16),
            b: parseInt(result[3], 16)
        } : null;
    }

	//  legend
	
	var svg1 = d3.select("body")
                .append("svg")
                .attr("width",Size)
                .attr("height", Size)
                .attr("class","legends")
                .attr("transform", "translate(70,0)");
	
	var nodess = bubble.nodes(root)
    nodess.shift()


	var legendG = svg1.selectAll(".legend") 
	  .data(nodess)
	  .enter().append("g")
	  .attr("transform", function(d,i){
		return "translate("+0+"," + (i * Size/33 + Size/50) + ")"; 
	  })
	  .attr("class", "legend");   

	legendG.append("rect") 
	  .attr("width", Size/50)
	  .attr("height", Size/50)
        .style("fill", function(d) { 
            return d.color ? d.color : colour(d.r); 
            });

	legendG.append("text") 
	  .text(function(d){
		return d.name + "  " + d.value.toFixed(1)+symbol+" - "+(d.percentage*100 ).toFixed(1).toString() + " %";
	  })
	  .style("font-size", Size/50)
	  .attr("y", Size/62)
	  .attr("x", Size/33)
}