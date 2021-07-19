
public String function() 
{ 
    String error=null; 
if(!pass(operation1())) { 
return error="operation1failed"; 
} 
if(!pass(operation2())) {
 return error="operation1failed";
 } 
if(!pass(operation3())) { 
return error="operation1failed"; 
}
 if(!pass(operation4())) { 
return error="operation1failed"; 
} 
return error; }
