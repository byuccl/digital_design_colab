#include <stdlib.h>
#include <iostream>
#include <verilated.h>
#include <verilated_vcd_c.h>
#include "Vfunction1.h"


void check(int expected_value, Vfunction1 *dut){
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
void set_values(int btnd, int sw, Vfunction1 *dut){
  dut->btnd = btnd;
  dut->sw = sw;
  dut->eval();
}

int main(int argc, char **argv, char **env)
{
    Vfunction1 *dut = new Vfunction1;

    Verilated::traceEverOn(true);
    //Signals: btnr, sw
    set_values(0, 0, dut);
    check(0, dut);

    set_values(0, 11, dut);
    check(11, dut);

    set_values(1, 0, dut);
    check(0, dut);

    set_values(1, 8010, dut);
    check(64080, dut);

    set_values(1, 3, dut);
    check(24, dut);

    delete dut;
    exit(EXIT_SUCCESS);
}
