#include <stdlib.h>
#include <iostream>
#include <verilated.h>
#include <verilated_vcd_c.h>
#include "Vfunction2.h"


void check(int expected_value, Vfunction2 *dut){
  int real_value = dut->led;
  int sw = dut->sw;
  int btnl = dut->btnl;
  if(real_value != expected_value){
    printf("ERROR: expected led = %d, instead led = %d while sw = %d and btnl = %d\n", expected_value, real_value, sw, btnl);
  }
  else{
    printf("CORRECT: led = %d while sw = %d and btnl = %d\n", expected_value, sw, btnl);
  }
}
void set_values(int btnl, int sw, Vfunction2 *dut){
  dut->btnl = btnl;
  dut->sw = sw;
  dut->eval();
}

int main(int argc, char **argv, char **env)
{
    Vfunction2 *dut = new Vfunction2;

    Verilated::traceEverOn(true);
    //Signals: btnl, sw
    set_values(0, 0, dut);
    check(0, dut);

    set_values(0, 1234, dut);
    check(1234, dut);

    set_values(1, 8734, dut);
    check(60, dut);

    set_values(1, 12098, dut);
    check(109, dut);

    delete dut;
    exit(EXIT_SUCCESS);
}
