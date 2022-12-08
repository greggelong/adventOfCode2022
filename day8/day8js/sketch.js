 

let result;
function preload() {
  result = loadStrings('data.txt');
}

let sz = 10;
let x =0;
let y =0;

let grid =[];


function setup() {
  createCanvas(990, 990);
  //rectMode(CENTER)
  background(0,255,255);
  colorMode(HSB,10) // 0 red - purple 9
  //noStroke();

  
  for( let i =0; i<result.length; i++){
     let row = result[i].split('')
     grid.push(row)
    
  }
  
  //print(result)
  showGrid()
  showvis()

  
   
}


function showGrid(){
  
  for (let y =0; y<grid.length;y++){
    for (let x =0; x<grid[y].length; x++){
      fill(grid[y][x],9,9)
      //fill(7,9,9)
      rect(x*sz,y*sz,sz,sz);
      
      //print(x,y)
    }
    
  
  } 
}


function showvis(){
  let total = 0
  let best =0
  let bx =0
  let by =0
  for (let y =1; y<grid.length-1;y++){
    for (let x =1; x<grid[y].length-1; x++){
      if(checkifvisable(x,y)){
        fill(255)
        total++
        rect(x*sz,y*sz,sz,sz)
        
      }
      if(getscore(x,y) > best){
        best = getscore(x,y)
        bx = x
        by = y
        
      }
      //fill(grid[y][x],9,9)
      //fill(7,9,9)
      
      //print(x,y)
    }
    
  
  } 
  print("total: ", total+392)  // (4* side len) -4
  print("best scenic score: ", best)
  print("best x ", bx)
  print("best y ",by )

  fill(0)
  rect(bx*sz,by*sz,sz,sz)
}


function checkifvisable(x,y){
  let nv = true 
  let sv = true
  let ev = true
  let wv = true
  myheight = grid[y][x];
  // check north
  for (let i = y-1; i>=0; i--){
    if (grid[i][x] >= myheight){
      nv = false
    }
  }

  // check south
  for (let i = y+1; i<grid.length; i++){
    if (grid[i][x] >= myheight){
      sv = false
    }
  }

  // check east
  for (let i = x+1; i<grid.length; i++){
    if (grid[y][i] >= myheight){
      ev = false
    }
  }

  // check west
  for (let i = x-1; i>=0; i--){
    if (grid[y][i] >= myheight){
      wv = false
    }
  }


  if(nv ||sv || ev|| wv){
    return true
  }


}



function getscore(x,y){
  let nv = 0
  let sv = 0
  let ev = 0
  let wv = 0 
  myheight = grid[y][x];
  // check north
  for (let i = y-1; i>=0; i--){
    if (grid[i][x] >= myheight){
      nv++
      break
    }
    nv++
  }

  // check south
  for (let i = y+1; i<grid.length; i++){
    if (grid[i][x] >= myheight){
      sv++
      break
    }
    sv++
  }

  // check east
  for (let i = x+1; i<grid.length; i++){
    if (grid[y][i] >= myheight){
      sv++
      break
    }
    ev++
  }

  // check west
  for (let i = x-1; i>=0; i--){
    if (grid[y][i] >= myheight){
      wv++
      break
    }
    wv++
  }


  return nv*sv*ev*wv


}
 