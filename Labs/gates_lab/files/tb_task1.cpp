#include <stdlib.h>
#include <iostream>
#include <verilated.h>
#include <verilated_vcd_c.h>
#include "Vtask1.h"


void check(int expected_value, Vtask1 *dut){
  int real_value = dut->led;
  int sw = dut->sw;
  int btnd = dut->btnd;
  if(real_value != expected_value){
    printf("ERROR: expected led = %d, instead led = %d while sw = %d and btnd = %d\n", expected_value, real_value, sw, btnd);
  }
  else{
    printf("CORRECT: led = %d while sw = %d and btnd = %d\n", expected_value, sw, btnd);
  }
}

void set_values(int A, int B, int C, int D, Vtask1 *dut){
  dut->A = 0;
  dut->B = 0; 
  dut->C = 0; 
  dut->D = 0; 
  dut->eval();
}

int main(int argc, char **argv, char **env)
{
    Vtask1 *dut = new Vtask1;

    Verilated::traceEverOn(true);
    //Signals: btnr, sw
    set_values(0, 0, dut);
    check(0, dut);

    delete dut;
    exit(EXIT_SUCCESS);
}
