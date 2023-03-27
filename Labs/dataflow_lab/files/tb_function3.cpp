#include <stdlib.h>
#include <iostream>
#include <verilated.h>
#include <verilated_vcd_c.h>
#include "Vfunction3.h"


void check(int expected_value, Vfunction3 *dut){
  int real_value = dut->led;
  int sw = dut->sw;
  int btnr = dut->btnr;
  int A = dut->A;
  int B = dut->B;
  int C = dut->C;
  if(real_value != expected_value){
    printf("ERROR: expected led = %d, instead led = %d while sw = %d, btnr = %d, A = %d, B = %d and C = %d\n", expected_value, real_value, sw, btnr,A,B,C);
  }
  else{
    printf("CORRECT: led = %d while sw = %d, btnr = %d, A = %d, B = %d and C = %d\n", expected_value, sw, btnr,A,B,C);
  }
}
void set_values(int btnr, int sw, int A, int B, int C, Vfunction3 *dut){
  dut->btnr = btnr;
  dut->sw = sw;
  dut->A = A;
  dut->B = B;
  dut->C = C;
  dut->eval();
}

int main(int argc, char **argv, char **env)
{
    Vfunction3 *dut = new Vfunction3;
    //Signals: btnr, sw, A, B, C
    set_values(0, 0, 0, 0 , 0, dut);
    check(0, dut);

    set_values(0, 1, 1, 1, 1,  dut);
    check(15, dut);

    set_values(1, 8191, 0 , 0, 0, dut);
    check(0, dut);

    set_values(1, 8191, 0 , 0, 1, dut);
    check(1, dut);

    set_values(1, 8191, 0 , 1, 0, dut);
    check(0, dut);

    set_values(1, 0, 0 , 1, 1, dut);
    check(1, dut);

    set_values(1, 8191, 1, 0, 0, dut);
    check(1, dut);

    set_values(1, 0, 1 , 0, 1, dut);
    check(1, dut);

    set_values(1, 8191, 1 , 1, 0, dut);
    check(0, dut);

    set_values(1, 8191, 1 , 1, 1, dut);
    check(1, dut);

    delete dut;
    exit(EXIT_SUCCESS);
}
