int priority_array[4] = {1,2,3,4}; //1 -> HIGH Priority, 4 -> LOW priority
int priority = 0;

void error_code (int code){
  switch(code){
    case 1: 
      priority =  priority_array[1]; // lvl 2 priority
    break;
    default:
    break;
    
  }
}
