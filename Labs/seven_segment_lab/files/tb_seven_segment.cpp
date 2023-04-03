#include <stdlib.h>
#include <iostream>
#include <verilated.h>
#include <verilated_vcd_c.h>
#include "Vseven_segment.h"


void check(int expected_segment, Vseven_segment *dut){
  int data = dut->data;
  int segment = dut->segment;
  if(segment != expected_segment){
    printf("ERROR: expected segment = %d, instead segment = %d while data = %d\n", expected_segment, segment, data);
  }
  else{
    printf("CORRECT segment = %d while data = %d\n", segment, data);
  }
}

void set_values(int data, Vseven_segment *dut){
  dut->data = data;
  dut->eval();
}

int main(int argc, char **argv, char **env)
{
    Vseven_segment *dut = new Vseven_segment;

    Verilated::traceEverOn(true);
    //Signals: a, b, cin
    //Outputs: s, co
    set_values(0, dut);
    check(64, dut);

    set_values(1, dut);
    check(121, dut);

    set_values(2, dut);
    check(36, dut);

    set_values(3, dut);
    check(48, dut);

    set_values(4, dut);
    check(25, dut);

    set_values(5, dut);
    check(18, dut);  
    
    set_values(6, dut);
    check(2, dut);

    set_values(7, dut);
    check(120, dut);

    set_values(8, dut);
    check(0, dut);
    
    set_values(9, dut);
    check(16, dut);

    set_values(10, dut);
    check(8, dut);

    set_values(11, dut);
    check(3, dut);

    set_values(12, dut);
    check(70, dut);

    set_values(13, dut);
    check(33, dut);

    set_values(14, dut);
    check(6, dut);

    set_values(15, dut);
    check(14, dut);
    delete dut;
    exit(EXIT_SUCCESS);
}
