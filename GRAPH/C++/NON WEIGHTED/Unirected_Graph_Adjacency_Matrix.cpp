#include <bits/stdc++.h>
using namespace std;

void add_edge(vector<vector<int>> &mat, int i, int j){
    if (mat[i][j] == 0 ){
        mat[i][j] = 1;
        mat[j][i] = 1;
    }
};

void display_matrix(vector<vector<int>> &mat){
    int v = mat.size();
    for(int i=0; i<v; i++){
        for(int j=0; j<v; j++)
            cout<<mat[i][j]<<' ';
        cout<<endl;
    }
};

int main(){
    int v = 4;
    vector<vector<int>> mat(v, vector<int>(v, 0));
    
    add_edge(mat, 0, 1);
    add_edge(mat, 0, 2);
    add_edge(mat, 1, 2);
    add_edge(mat, 2, 3);

    display_matrix(mat);
    return 0;
}