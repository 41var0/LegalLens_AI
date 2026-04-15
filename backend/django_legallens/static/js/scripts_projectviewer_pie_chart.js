/**
 * Sacado de
 * https://jsfiddle.net/ya3ya6/yd3rzo42/
 * https://stackoverflow.com/a/63635905
 */

var canvas = document.getElementById("pastelito");
var ctx = canvas.getContext("2d");
var lastend = 0;
var data = [DONE_TASKS, TODO_TASK, INPROG_TASK];
var myTotal = 0;
var myColor = ['#71DD4B', '#b53940', '#dd9755'];
var labels = ['Terminadas', 'Pendientes', 'En progreso'];

for(var e = 0; e < data.length; e++)
{
  myTotal += data[e];
}

// make the chart 10 px smaller to fit on canvas
var off = 10
var w = (canvas.width - off) / 2
var h = (canvas.height - off) / 2
for (var i = 0; i < data.length; i++) {
  ctx.fillStyle = myColor[i];
  ctx.strokeStyle ='white';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(w,h);
  var len =  (data[i]/myTotal) * 2 * Math.PI
  var r = h - off / 2
  ctx.arc(w , h, r, lastend,lastend + len,false);
  ctx.lineTo(w,h);
  ctx.fill();
  ctx.stroke();
  lastend += Math.PI*2*(data[i]/myTotal);
}



var legend = document.getElementById("leyenda");

for (let i = 0; i < labels.length; i++) {
  let li = document.createElement("li");
  li.innerHTML = `
    <span style="
      display:inline-block;
      width:12px;
      height:12px;
      background:${myColor[i]};
      margin-right:8px;
    "></span>
    ${labels[i]} (${data[i]})
  `;
  legend.appendChild(li);
}