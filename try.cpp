
#include <bits/stdc++.h>
using namespace std;
int main() {
    map<string, vector<string>> mp;
    mp["deepak"] = {"dee", "pak"};
    for(auto& [k, v] : mp) {
        cout<<k<< " : ";
        cout<<v<<endl;
    }
    return 0;
}