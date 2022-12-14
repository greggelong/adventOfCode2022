class Cell{
    constructor(x,y,h,l){
        this.x = x;
        this.y = y;
        this.h = h; // make a number
        this.l = l; // original letter
        this.connected = []
        this.visited = false
        this.start = false
        this.end = false
        this.parent = null


    }
/*
    getconnected(){

        // can go lower many levels lower and still be connected
        // check upper neighbor
        // if it is the same height, or one lower, or one higher it is connected 
        if (this.y-1>=0){
            if (this.h == grid[this.y-1][this.x].h||this.h == grid[this.y-1][this.x].h-1 || this.h == grid[this.y-1][this.x].h+1){
                this.connected.push(grid[this.y-1][this.x]);
            }
        }
        // check lower neighbor
        if (this.y+1<=grid.length-1){
            if (this.h == grid[this.y+1][this.x].h||this.h ==grid[this.y+1][this.x].h-1 || this.h == grid[this.y+1][this.x].h+1){
                this.connected.push(grid[this.y+1][this.x]);
            }
        } 

        // check right neighbor
        if (this.x+1<=grid[0].length-1){
            if (this.h == grid[this.y][this.x+1].h||this.h == grid[this.y][this.x+1].h-1 || this.h == grid[this.y][this.x+1].h+1){
                this.connected.push(grid[this.y][this.x+1]);
            }
        } 

        // check left neighbor
        if (this.x-1>=0){
            if (this.h == grid[this.y][this.x-1].h||this.h == grid[this.y][this.x-1].h-1 || this.h == grid[this.y][this.x-1].h+1){
                this.connected.push(grid[this.y][this.x-1]);
            }
        } 
    }

*/
    getconnected(){

        // can go lower many levels lower and still be connected
        // check upper neighbor
        // if this . h is > or equal to neighbor h  or it is one less 
        if (this.y-1>=0){
            if (this.h  >= grid[this.y-1][this.x].h  || this.h+1 == grid[this.y-1][this.x].h){
                this.connected.push(grid[this.y-1][this.x]);
            }
        }
        // check lower neighbor
        if (this.y+1<=grid.length-1){
            if (this.h >= grid[this.y+1][this.x].h|| this.h+1 == grid[this.y+1][this.x].h){
                this.connected.push(grid[this.y+1][this.x]);
            }
        } 

        // check right neighbor
        if (this.x+1<=grid[0].length-1){
            if (this.h >=grid[this.y][this.x+1].h||this.h+1 == grid[this.y][this.x+1].h){
                this.connected.push(grid[this.y][this.x+1]);
            }
        } 

        // check left neighbor
        if (this.x-1>=0){
            if (this.h >= grid[this.y][this.x-1].h|| this.h+1 == grid[this.y][this.x-1].h){
                this.connected.push(grid[this.y][this.x-1]);
            }
        } 
    }

}