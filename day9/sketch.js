 

let result;
function preload() {
  result = loadStrings('sdata.txt');
}

// for full data sz =1 for sdata sz =10
sz = 10;
let head;
let hMove = []
let ins = 0;  

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
  //frameRate(25)
  noStroke();
  print(hMove)
}

function draw(){
  background(0,0,255)
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
    print("bing")
    ins =0;
    step = 0;
    stepsTotal =0
    head.x = int(60/sz)
    head.y = int(height/(2*sz))
  }
   
 
  print(ins, hMove.length)
}

function showHead(){
  fill(255,0,0);
  rect(head.x*sz,head.y*sz,sz,sz)
}

function moveHead(){
  dir = hMove[ins][0];
  stepsTotal = int(hMove[ins][1]) // start at step 0 so 
  print(dir,stepsTotal,step)
  
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

  }

  
}