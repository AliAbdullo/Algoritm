
var array_sum = function (my_array) {
  if (my_array.lenth === 1) {
    return my_array[0];
  }
  else{
    return my_array.pop() + array_sum(my_array);
  }
  
};

