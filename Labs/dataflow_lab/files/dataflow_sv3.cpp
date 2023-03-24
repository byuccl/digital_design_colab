#include <stdlib.h>
#include <iostream>
#include <bitset>
#include <verilated.h>
#include <verilated_vcd_c.h>
#include "Vdataflow_sv3.h"

#define MAX_SIM_TIME 30
vluint64_t sim_time = 0;

void printError(int sim_time, int expected, int simulated)
{
    {
        std::cout << "ERROR at " << sim_time << "ns: " << std::endl;
        std::cout << "Expected Value: " << std::bitset<16>(expected).to_string() << std::endl;
        std::cout << "Simulated Value: " << std::bitset<16>(simulated).to_string() << std::endl;
    }
}

void change_sw(Vdataflow_sv3 *dut, vluint64_t sim_time)
{
    if (sim_time % 2 == 0)
    {
        switch (sim_time)
        {
        case 2:
            dut->btnr = 0;
            dut->sw = 0;
            break;
        case 4:
            dut->sw = 1;
            break;
        case 6:
            dut->btnr = 0;
            dut->sw = 11;
            break;
        case 8:
            dut->btnr = 0;
            dut->sw = 234;
            break;
        case 10:
            dut->btnr = 0;
            dut->sw = 0;
            break;
        case 12:
            dut->btnr = 1;
            dut->sw = 0;
            break;
        case 14:
            dut->sw = 1;
            break;
        case 16:
            dut->sw = 2;
            break;
        case 18:
            dut->sw = 3;
            break;
        case 20:
            dut->sw = 4;
            break;
        case 22:
            dut->sw = 5;
            break;
        case 24:
            dut->sw = 6;
            break;
        case 26:
            dut->sw = 7;
            break;
        default:
            dut->btnr = 0;
            dut->sw = 0;
        }
    }
}

void check_sw(Vdataflow_sv3 *dut, vluint64_t sim_time)
{
    if (sim_time % 2 == 1)
    {
        switch (sim_time)
        {
        case 3:
            if (dut->led != 0)
                printError(sim_time, 0, dut->led);
            break;
        case 5:
            if (dut->led != 1)
                printError(sim_time, 8, dut->led);
            break;
        case 7:
            if (dut->led != dut->sw)
                printError(sim_time, dut->sw, dut->led);
            break;
        case 9:
            if (dut->led != dut->sw)
                printError(sim_time, dt->sw, dut->led);
            break;
        case 11:
            if (dut->led != dut->sw)
                printError(sim_time, dut->sw, dut->led);
            break;
        case 13:
            if (dut->led != 0)
                printError(sim_time, dut->sw, dut->led);
            break;
        case 15:
            if (dut->led != 1)
                printError(sim_time, 1, dut->led);
            break;
        case 17:
            if (dut->led != 0)
                printError(sim_time, 0, dut->led);
            break;
        case 19:
            if (dut->led != 0)
                printError(sim_time, 0, dut->led);
            break;
        case 21:
            if (dut->led != 1)
                printError(sim_time, 1, dut->led);
            break;
        case 23:
            if (dut->led != 1)
                printError(sim_time, 1, dut->led);
            break;
        case 25:
            if (dut->led != 1)
                printError(sim_time, 1, dut->led);
            break;
        case 27:
            if (dut->led != 1)
                printError(sim_time, 1, dut->led);
            break;
        default:
            if (dut->led != 0)
                std::cout << "Error at " << sim_time << "ns" << std::endl;
        }
    }
}

int main(int argc, char **argv, char **env)
{
    Vdataflow_sv3 *dut = new Vdataflow_sv3;

    Verilated::traceEverOn(true);
    VerilatedVcdC *m_trace = new VerilatedVcdC;
    dut->trace(m_trace, 5);
    m_trace->open("waveform3.vcd");

    while (sim_time < MAX_SIM_TIME)
    {
        change_sw(dut, sim_time);
        check_sw(dut, sim_time);
        // dut->clk ^= 1;
        dut->eval();
        m_trace->dump(sim_time);
        sim_time++;
    }

    m_trace->close();
    delete dut;
    exit(EXIT_SUCCESS);
}
