#include<iostream>

using namespace std;

int table[4][5] = {
	{10,0,20,11,15},
	{12,7,9,20,25},
	{0,14,16,18,5},
	{5,15,15,10,0}
};
int val[100][100];

void create_table(int row, int column){
	for(int i=0; i<row+1; i++){
		if(i==row){
			for(int j=0; j<column; j++){
				cout << "Demand ke-" << j+1 << ": ";
				cin >> table[i][j];
			}
		}
		else{
			for(int j=0; j<column+1; j++){
				if(j==column){
					cout << "Supply ke-" << i+1 << ": ";
				}
				else{
					cout << "j" << j+1 << ": ";
				}
				cin >> table[i][j];
			}
		}
	}
}

int print_table(int row, int column){
	for(int i=0; i<row+1; i++){
		for(int j=0; j<column+1; j++){
			cout << val[i][j] << "\t";
		}
		cout << endl;
	}
	cout << endl;
	int sum = 0;
	for(int i=0; i<row; i++){
		for(int j=0; j<column; j++){
			sum += val[i][j]*table[i][j];
		}
	}
	cout << "The sum is: " << sum << endl;
}

void pojok_kiri_atas(int row, int column){
	for(int i=0; i<row; i++){
		for(int j=0; j<column; j++){
			if(table[row][j]>table[i][column]){
				val[i][j] = table[i][column];
				table[row][j] -= table[i][column];
				table[i][column] = 0;
			}
			else{
				val[i][j] = table[row][j];
				table[i][column] -= table[row][j];
				table[row][j] = 0;
			}
		}
	}
}

int main(){
	int row=3, column=4;
	//cout << "Number of rows: ";
	//cin >> row;
	//cout << "Number of column: ";
	//cin >> column;
	//create_table(row, column);
	pojok_kiri_atas(row, column);
	print_table(row, column);
}
