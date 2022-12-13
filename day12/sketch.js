 

let result;
function preload() {
  result = loadStrings('data.txt');
}


let grid =[]

let alphaHeight =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


let sz =10
function setup(){
  createCanvas(1680, 410);

  background(0)

  // create grid

  
  
  for(let j = 0; j<result.length; j++){
    grid[j]=[]
    row = result[j].split('')
    for(let i =0; i<row.length;i++){
      myh = alphaHeight.indexOf(row[i])
      grid[j][i] = new Cell(i,j,myh, row[i])
    }
    
  }

  
  print(grid)
  print(grid[0][0])
  console.table(grid)
  showgrid()
  connect()
}


function showgrid(){
  textSize(sz)
  for(let y = 0; y<grid.length; y++){
    for(let x =0; x<grid[y].length; x++){
      fill(0,255,0)
      noStroke()
      text(grid[y][x].l,x*sz,y*sz)
    }
}
}



function connect(){
  for(let j =0; j<grid.length; j++){
    for(let i =0; i<grid[j].length; i++){
      grid[j][i].getconnected();
    }
  }
}




/*
bfs(start vertex, goal vertex)
make frontier an empty queue
enqueue start onto frontier
until frontier is empty
    dequeue parent off frontier
    for each undiscovered child of parent
	enqueue child onto frontier
	stop if child is the goal



*/