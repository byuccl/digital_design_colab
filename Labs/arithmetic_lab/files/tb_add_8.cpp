#include <stdlib.h>
#include <iostream>
#include <verilated.h>
#include <verilated_vcd_c.h>
#include "Vadd_8.h"


void check(int expected_s, int expected_co, Vadd_8 *dut){
  int s = dut->s;
  int co = dut->co;
  int a = dut->a;
  int b = dut->b;
  int cin = dut->cin;
  if(s != expected_s){
    printf("ERROR: expected s = %d, instead s = %d while a = %d, b = %d and cin = %d\n", expected_s, s, a, b, cin);
  }
  else{
    printf("CORRECT s = %d while a = %d, b = %d and cin = %d\n", s, a, b, cin);
  }
  if(co != expected_co){
    printf("ERROR: expected co = %d, instead co = %d while a = %d, b = %d and cin = %d\n", expected_co, co, a, b, cin);
  }
  else{
    printf("CORRECT co = %d while a = %d, b = %d and cin = %d\n", co, a, b, cin);
  }
}

void set_values(int a, int b, int cin, Vadd_8 *dut){
  dut->a = a;
  dut->b = b;
  dut->cin = cin;
  dut->eval();
}

int main(int argc, char **argv, char **env)
{
    Vadd_8 *dut = new Vadd_8;

    Verilated::traceEverOn(true);
    //Signals: a, b, cin
    //Outputs: s, co
    set_values(0, 0, 0, dut);
    check(0, 0, dut);

    set_values(0, 0, 1, dut);
    check(1, 0, dut);

    set_values(40, 40, 0, dut);
    check(80, 0, dut);

    set_values(40, 40, 1, dut);
    check(81, 0, dut);

    set_values(255, 1, 0, dut);
    check(0, 1, dut);

    set_values(255, 1, 1, dut);
    check(1, 1, dut);    

    delete dut;
    exit(EXIT_SUCCESS);
}
