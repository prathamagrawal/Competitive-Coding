// C++ program to illustrate the
// iterators in vector
#include <iostream>
#include <vector>
#include<cstring>
#include<string.h>
using namespace std;


vector<int> solve (int N, vector<string> command) {
   // Your code goes here
   //tri - scope animal number
   char scope='0',animal,val;
   vector<int> ans; //stores final answer
   vector<vector<char> > order; //stores the reversed order of printing and the scope
   vector<vector<char> > tri; //stores assignees animals scope, animal, value
   for(auto i : command ){
      if(i[0] == '{'){
         scope++;
      }
      else if(i[0] == '}'){
         scope--;
      }
      else if(i[0] == 'a'){
         animal = i[7];
         val = i[9];
         tri.push_back({scope, animal, val});
      }
      else if(i[0] == 'p'){
         order.push_back({i[6],scope});
      }
   }
   int flag=0;
   for(auto i : order){
      for(auto j : tri){
         if(i[0] == j[1] && i[1] == j[0]){
            ans.push_back((int)j[2]);
            flag=0;
            break;
         }else if(i[1] > j[2]){
            ans.push_back((int)j[2]);
            flag=0;
            break;
         }
         else{
            flag=1;
         }
      }
      // if(flag){
      //    printf("undefined");
      // }
   }
   reverse(ans.begin(),ans.end());
return ans;
}

int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n'); 
    vector<string> command(N);
    for(int i_command = 0; i_command < N; i_command++)
    {
       getline(cin,command[i_command]);
    }

    vector<int> out_;
    out_ = solve(N, command);
    cout << out_[0];
    for(int i_out_ = 1; i_out_ < out_.size(); i_out_++)
    {
    	cout << "\n" << out_[i_out_];
    }
}