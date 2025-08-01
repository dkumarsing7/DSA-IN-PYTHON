#include<bits/stdc++.h>
using namespace std; 

void add_edge(vector<vector<int>> &mat, int i, int j){
    auto it = find(mat[i].begin(), mat[i].end(), j);
    if(it == mat[i].end()){
        mat[i].push_back(j);
        if(i != j)
        mat[j].push_back(i);
    }
};

void display_Adj_List(vector<vector<int>> &mat){
    int v = mat.size();
    for(int i=0; i<v; i++){
        if(!mat[i].empty()){
            cout<< i << " : ";
            for(auto j : mat[i])
                cout<< j << " ";
            cout<<endl;
        }
    }
};

int main(){
    int v = 4 ;
    vector<vector<int>> mat(v);
    
    add_edge(mat, 0, 2);
    add_edge(mat, 0, 2);
    add_edge(mat, 2, 2);
    add_edge(mat, 2, 3);
    
    display_Adj_List(mat);
}

