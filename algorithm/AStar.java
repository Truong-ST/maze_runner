package maze;
import java.util.*;

public class AStar {
	public static final int d1 = 10;  //khoang cach 2 o ngang, doc
	public static final int d2 = 14;  //khoang cach 2 o cheo
	
	static class Cell{
		int h = 0;          //heuristic cost
		int f = 0;          //f = g+h
		int i,j;
		Cell parent;
		boolean isPath = false;
		Cell(int i, int j){
			this.i = i;
			this.j = j;
		}
		@Override
		public String toString(){
            return "["+this.i+", "+this.j+"]";
        }
	}
	
	static Cell [][] grid = new Cell[5][5];
	static PriorityQueue<Cell> open;
	static boolean close[][];
	static int startI, startJ;
	static int endI, endJ;
	
	public static void setBlocked(int i, int j) {
		grid[i][j] = null;
	}
	public static void setStartCell(int i, int j) {
		startI = i;
		startJ = j;
	}
	public static void setEndCell(int i, int j) {
		endI = i;
		endJ = j;
	}
	static void checkAndUpdateCost(Cell current, Cell t, int cost){
        if(t == null || close[t.i][t.j])return;
        int t_final_cost = t.h + cost;    
        boolean inOpen = open.contains(t);
        if(!inOpen || t_final_cost<t.f){
            t.f = t_final_cost;
            t.parent = current;
            if(!inOpen)open.add(t);
        }
    }
	
	public static void AStar1() {
		open.add(grid[startI][startJ]);
		Cell current;
		while(true) {
			current = open.poll();
			if(current == null) break;
			close[current.i][current.j] = true;
			if(current.equals(grid[endI][endJ])) return;
			
			Cell t;
			if(current.i - 1 >= 0) {
				t = grid[current.i - 1][current.j];
				checkAndUpdateCost(current, t, current.f + d1); //sang trai
				if(current.j - 1 >= 0) {
					t = grid[current.i - 1][current.j - 1]; 
					checkAndUpdateCost(current, t, current.f + d2); //cheo len
				}
				if(current.j + 1 < grid[0].length) {
					t = grid[current.i - 1][current.j + 1]; 
					checkAndUpdateCost(current, t, current.f + d2); //cheo xuong
				}	
			}
			
			if(current.i + 1 < grid.length) {
				t = grid[current.i + 1][current.j];
				checkAndUpdateCost(current, t, current.f + d1); //sang phai
				if(current.j - 1 >= 0) {
					t = grid[current.i + 1][current.j - 1];
					checkAndUpdateCost(current, t, current.f + d2); //cheo len
				}
				if(current.j + 1 < grid[0].length) {
					t = grid[current.i + 1][current.j + 1];
					checkAndUpdateCost(current, t, current.f + d2); //cheo xuong
				}	
			}
			
			if(current.j - 1 >= 0) {
				t = grid[current.i][current.j - 1];
				checkAndUpdateCost(current, t, current.f + d1); //len tren
			}
			
			if(current.j + 1 < grid[0].length) {
				t = grid[current.i][current.j + 1];
				checkAndUpdateCost(current, t, current.f + d1); //xuong duoi
			}
		}
	}
	public static void test(int x, int y, int si, int sj, int ei, int ej, int [][]blocked) {
		grid = new Cell[x][y];
		close = new boolean [x][y];		
		open = new PriorityQueue<>((Object o1, Object o2) -> {
            Cell c1 = (Cell)o1;
            Cell c2 = (Cell)o2;
            return c1.f<c2.f?-1:
                    c1.f>c2.f?1:0;
        });
		
		setStartCell(si,sj);
		setEndCell(ei,ej);
		for(int i=0; i<x; i++) {
			for(int j=0; j<y; j++) {
				grid[i][j] = new Cell(i,j);
				grid[i][j].h = Math.abs(i-endI) + Math.abs(j-endJ);
			}
		}
		
		grid[si][sj].f = 0;
		
		for(int i=0; i<blocked.length; i++) {
			setBlocked(blocked[i][0], blocked[i][1]);
		}
		
		//Display
		System.out.println("Me cung: ");
		for(int i=0; i<x; i++) {
			for(int j=0; j<y; j++) {
				if(i==si && j==sj) System.out.print("BD ");
				else if(i==ei && j==ej) System.out.print("KT ");
				else if(grid[i][j] != null) System.out.print("1  ");
				else System.out.print("0  ");
			}	
			System.out.println();
		}
		System.out.println();
		
		AStar1();
		//Hien thi ket qua
		System.out.println("Scores for cell: ");
		for(int i=0; i<x; i++) {
			for(int j=0; j<y; j++) {
				if(grid[i][j] != null) System.out.printf("%-3d", grid[i][j].f);
				else System.out.print("BL ");
			}
			System.out.println();
		}
		System.out.println();	
		
		
		
		if(close[endI][endJ]) {
			System.out.println("Duong di: ");
			Cell current = grid[endI][endJ];
			System.out.print(current);
			while(current.parent != null) {
				current.isPath = true;
				System.out.print(" <-  " + current.parent);
				current = current.parent;
			}
			System.out.println();
			for(int i=0; i<x; i++) {
				for(int j=0; j<y; j++) {
					if(i==si && j==sj) System.out.print("BD ");
					else if(i==ei && j==ej) System.out.print("KT ");
					
					else if(grid[i][j] == null) System.out.print("0  ");
					else if(grid[i][j].isPath == true) System.out.print("*  ");
					
					else System.out.print("1  ");
				}	
				System.out.println();
			}
			
		}
		else System.out.println("Khong tim duoc duong di");
	}
	
	
	public static void main(String[] args) {
		test(5,5,0,0,3,2,new int[][] {{0,4},{2,2},{3,1},{3,3}});
	}
}
