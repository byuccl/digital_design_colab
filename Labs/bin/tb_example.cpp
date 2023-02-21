#include <stdlib.h>
#include <iostream>
// #include <verilated.h>
#include <verilated_vcd_c.h>
#include "Vfunction1.h"

#define MAX_SIM_TIME 20
vluint64_t sim_time = 0;

int main(int argc, char **argv, char **env)
{
    Vfunction1 *dut = new Vfunction1;

    Verilated::traceEverOn(true);
    VerilatedVcdC *m_trace = new VerilatedVcdC;
    dut->trace(m_trace, 5);
    m_trace->open("waveform.vcd");
    dut->load = 1;
    dut->d = 1;
    while (sim_time < MAX_SIM_TIME)
    {
        dut->clk ^= 1;
        dut->eval();
        m_trace->dump(sim_time);
        sim_time++;
    }

    m_trace->close();
    delete dut;
    exit(EXIT_SUCCESS);
}
