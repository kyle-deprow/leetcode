#include <iostream>
#include <iomanip>
#include <utility>
#include <string>
#include <vector>
#include <stack>

class Solution {
  long resolves(int a, int b, char op){
    if(op == '+') return a + b;
    else if(op == '-') return a - b;
    else if(op == '*') return static_cast<long>(a*b);
    return a/b;
  }

public:
  int evalRPN(std::vector<std::string>& tokens) {
    std::stack<long> charStack;
    int n = tokens.size();
    for(int i = 0; i < n; i++){
      // check if element is an operator by determining if char
      // value is less than the ASCII numeric for 0
      if(tokens[i].size() == 1 && tokens[i][0] < 48){
        // take first two integers off the top of stack and perform
        // op
        long integer2 = charStack.top();
        charStack.pop();
        long integer1 = charStack.top();
        charStack.pop();
        
        std::string op = tokens[i];
        long resolvedAns = resolves(integer1, integer2 , op[0]);
        // Store result back on top of stack
        charStack.push(resolvedAns);
      }
      // not an operator, store on top of the the stack
      else charStack.push(std::stol(tokens[i]));
    }
    return charStack.top();
  }
};