 

let result;
function preload() {
  result = loadStrings('data.txt');
}


let grid =[]
let start;
let finish;
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
  // connect the grid neighbors 
  connect()
  bfs()
  print("did it finish")

  // bfs( ) yes it finished
  // yes it found a path

  // get the path using parents

  let path =[]
  let end = grid[20][145]
  path.push(end) // path push finish
  let next = end.parent;
  while(next!= null){
    path.push(next);
    next = next.parent
  }

  print(path)
  print(path.length)

  fill(255,0,0)
  for(let i = 0; i<path.length;i++){
    rect(path[i].x*sz,path[i].y*sz,sz,sz)
  }




  
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
  //before connecting make sure that the hight of start and finish 
  grid[20][0].h =0
  grid[20][145].h =25
  // using the class connect all traversable neighbors
  for(let j =0; j<grid.length; j++){
    for(let i =0; i<grid[j].length; i++){
      grid[j][i].getconnected();
    }
  }
}

/*
Breadth-First-Search(Graph, root):


    for each node n in Graph:            

        n.distance = INFINITY        

        n.parent = NIL


    create empty queue Q      


    root.distance = 0

    Q.enqueue(root)                      


    while Q is not empty:        

    

        current = Q.dequeue()

    

        for each node n that is adjacent to current:

            if n.distance == INFINITY:

                n.distance = current.distance + 1

                n.parent = current

                Q.enqueue(n)

*/

function bfs(){
  start = grid[20][0];
  print(start.l)
  finish= grid[20][145];
  print(finish.l)

  let q =[] ; // q.push() to enqueue (go in the back of the line) and q.shift() to dequeue (leave from the front of line) fifo

  // set start to visited
  start.visited = true
  // put start on the q
  q.push(start)

  while (q.length>0){  // while q is not zero
    let current = q.shift()  // dequeue 
    print(current.l)
    rect(current.x*sz,current.y*sz,sz,sz)
    if (current === finish){
      // break
      print("found a path to finish")
      break;
    }else{
      // else add neighbors
      let neighList = current.connected
      for (let i =0; i<neighList.length; i++){
        let neighbor = neighList[i]
        if(neighbor.visited === false){
          neighbor.visited = true
          //set neighbor parent to current
          neighbor.parent = current;
          
          q.push(neighbor)
        }
      }
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