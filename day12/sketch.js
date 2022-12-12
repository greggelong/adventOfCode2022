 

let result;
function preload() {
  result = loadStrings('data.txt');
}


let grid =[]




let sz =10
function setup(){
  createCanvas(1680, 410);

  background(0)

  // create grid

  

  for(let j = 0; j<result.length; j++){
    grid[j] = result[j].split('')
    
  }


print(grid)
print(grid[0][0])
console.table(grid)
showgrid()
}


function showgrid(){
  textSize(sz)
  for(let y = 0; y<grid.length; y++){
    for(let x =0; x<grid[y].length; x++){
      fill(0,255,0)
      noStroke()
      text(grid[y][x],x*sz,y*sz)
    }
}
}