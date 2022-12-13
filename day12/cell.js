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


    }

    getconnected(){
        // check upper neighbor
        if (this.y-1>=0){
            if (this.h == grid[this.y-1][this.x].h||this.h == grid[this.y-1][this.x].h-1 || this.h == grid[this.y-1][this.x].h+1){
                this.connected.push(grid[this.y-1][this.x]);
            }
        }
        // check lower neighbor
        if (this.y+1<=grid.length-1){
            if (this.h == grid[this.y+1][this.x].h||this.h == grid[this.y+1][this.x].h-1 || this.h == grid[this.y+1][this.x].h+1){
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

}