 

let result;
function preload() {
  result = loadStrings('data.txt');
}

// for full data sz =1 for sdata sz =10
sz = 1;
let head;
let tail;
let hMove = []
let ins = 0;  
let tailpos =[];

let stepsTotal =0;
let step =0;
function setup(){
  createCanvas(500,500)
  background(0,0,255)
  for (let i =0; i<result.length;i++){
    let instruction = result[i].split(' ')
     hMove.push(instruction)
  }
  head = createVector(int(60/sz), int(height/(2*sz)))
  tail =  createVector(int(60/sz), int(height/(2*sz)))
  //frameRate(1)
  noStroke();
  print(hMove, head, tail)
}

function draw(){
  //background(0,0,255)
  showHead()
  moveHead()
  
  if (step < stepsTotal){
    step++
  }
 
  if (ins<hMove.length && step==stepsTotal){
    ins++
    step =0;
    stepsTotal =0;

  
  }
  if (ins === hMove.length){
    noLoop()
    print("bing")
    print(tailpos)
    let unique_array = Array.from(new Set(tailpos))
    print(unique_array)
    print(unique_array.length)
    ins =0;
    step = 0;
    stepsTotal =0
    head.x = int(60/sz)
    head.y = int(height/(2*sz))
    tail.x = int(60/sz)
    tail.y = int(height/(2*sz))
  }

  
   
 
  //print(ins, hMove.length, "hedx", (head.x)+2)
}

function showHead(){
  fill(255,0,0);
  rect(head.x*sz,head.y*sz,sz,sz)
  fill(0,255,0);
  rect(tail.x*sz,tail.y*sz,sz,sz)
}

function moveHead(){
  dir = hMove[ins][0];
  stepsTotal = int(hMove[ins][1]) // start at step 0 so 
  //print(dir,stepsTotal,step)
  
  if (step < stepsTotal){   // 
    //
    switch (dir){
      case 'R':
        head.x += 1;
      
        break;
      case 'L':
        head.x -=1
        
        break;
      case 'U':
        head.y -=1;
      
        break;
      case 'D':
        head.y +=1;
        
        break;
    }

    updateTail()

  }

  
  
}


function updateTail(){
    // move 8 directions but need to check check 12
    if (tail.equals(head.x,head.y+2)){
      // move north
      tail.y -=1;
    }
    else if(tail.equals(head.x,head.y-2)){
      // move south
      tail.y +=1;
    }
    else if(tail.equals(head.x-2,head.y)){
      // move east
      tail.x +=1;
      print("tail move east")
    }
    else if(tail.equals(head.x+2,head.y)){
      // move west
      tail.x -=1;

    }
    else if (tail.equals(head.x-1,head.y+2)){
      // move north east a
      tail.y-=1;
      tail.x+=1
    }
    else if(tail.equals(head.x-2,head.y+1)){
      // north east b
      tail.y-=1;
      tail.x+=1;
    }
    else if (tail.equals(head.x+1,head.y+2)){
      // move north west a
      tail.y-=1;
      tail.x-=1
    }
    else if(tail.equals(head.x+2,head.y+1)){
      // north west b
      tail.y-=1;
      tail.x-=1;
    }
    else if (tail.equals(head.x-2,head.y-1)){
      // move south east a
      tail.y+=1;
      tail.x+=1
    }
    else if(tail.equals(head.x-1,head.y-2)){
      // south east b
      tail.y+=1;
      tail.x+=1;
    }
    else if (tail.equals(head.x+2,head.y-1)){
      // move south west a
      tail.y+=1;
      tail.x-=1
    }
    else if(tail.equals(head.x+1,head.y-2)){
      // south west b
      tail.y+=1;
      tail.x-=1;
    }
    let coord = str(tail.x)+","+str(tail.y)
    tailpos.push(coord)
}



function case1(){
  // returns boolean true when tail is within range of head and doesn't need to move
  // 9 cases the same or 9 neighbors
  let n =0
  for (let j=-1;j<2;j++){
    for(let i=-1;i<2;i++){
      if(tail.equals(head.x+i,head.y+j)){
        n=n+1
        print(n)
      }
    
    }

  }
  if (n>0){
    return(true)
  }

}