#include <stdlib.h>
#include <iostream>
#include <verilated.h>
#include <verilated_vcd_c.h>
#include "Vexpression.h"


void check(int expected_value, Vexpression *dut){
  int real_value = dut->Q;
  if(real_value != expected_value){
    printf("ERROR: expected Q = %d, instead Q = %d while A = %d and B = %d and  C = %d and  D = %d\n",
     expected_value, real_value, dut->A, dut->B, dut->C, dut->D);
  }
  else{
       printf("CORRECT: expected Q = %d, Recieved Q = %d while A = %d and B = %d and  C = %d and  D = %d\n", 
       expected_value, real_value, dut->A, dut->B, dut->C, dut->D);

  }
}

void set_values(int A, int B, int C, int D, Vexpression *dut){
  dut->A = A;
  dut->B = B; 
  dut->C = C; 
  dut->D = D; 
  dut->eval();
}

int main(int argc, char **argv, char **env)
{
    Vexpression *dut = new Vexpression;

    Verilated::traceEverOn(true);
    //Signals: A, B, C, D
    set_values(0, 0, 0, 0, dut);
    check(1, dut);

    //Signals: A, B, C, D
    set_values(0, 0, 0, 1, dut);
    check(1, dut);

    //Signals: A, B, C, D
    set_values(0, 0, 1, 0, dut);
    check(1, dut);

    //Signals: A, B, C, D
    set_values(0, 0, 1, 1, dut);
    check(1, dut);

    //Signals: A, B, C, D
    set_values(0, 1, 0, 0, dut);
    check(1, dut);

    //Signals: A, B, C, D
    set_values(0, 1, 0, 1, dut);
    check(0, dut);

    //Signals: A, B, C, D
    set_values(0, 1, 1, 0, dut);
    check(1, dut);

    //Signals: A, B, C, D
    set_values(0, 1, 1, 1, dut);
    check(0, dut);

    //Signals: A, B, C, DVcircuit
   set_values(1, 0, 0, 1 , dut);
    check(1, dut);
    
    //Signals: A, B, C, D
    set_values(1, 0, 1, 0 , dut);
    check(1, dut);

    //Signals: A, B, C, D
    set_values(1, 0, 1, 1 , dut);
    check(1, dut);

     //Signals: A, B, C, D
    set_values(1, 1, 0, 0, dut);
    check(1, dut);

     //Signals: A, B, C, D
    set_values(1, 1, 0, 1, dut);
    check(1, dut);

    //Signals: A, B, C, D
    set_values(1, 1, 1, 0, dut);
    check(1, dut);

     //Signals: A, B, C, D
    set_values(1, 1, 1, 1, dut);
    check(1, dut);

    delete dut;
    exit(EXIT_SUCCESS);
}
