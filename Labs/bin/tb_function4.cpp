#include <stdlib.h>
#include <iostream>
#include <bitset>
#include <verilated.h>
#include <verilated_vcd_c.h>
#include "Vfunction4.h"

#define MAX_SIM_TIME 20
vluint64_t sim_time = 0;

void printError(int sim_time, int expected, int simulated)
{
    {
        std::cout << "ERROR at " << sim_time << "ns: " << std::endl;
        std::cout << "Expected Value: " << std::bitset<16>(expected).to_string() << std::endl;
        std::cout << "Simulated Value: " << std::bitset<16>(simulated).to_string() << std::endl;
    }
}

void change_sw(Vfunction4 *dut, vluint64_t sim_time)
{
    if (sim_time % 2 == 0)
    {
        switch (sim_time)
        {
        case 2:
            dut->btnu = 0;
            dut->hour=0;
            dut->student=0;
            dut->prof=0;
            dut->pm=0;
            dut->sw = 511;
            break;
        case 4:
            dut->btnu = 0;
            dut->hour=11;
            dut->student=0;
            dut->prof=1;
            dut->pm=0;
            dut->sw = 511;
            break;
        case 6:
            dut->btnu = 1;
            dut->hour=11;
            dut->student=0;
            dut->prof=1;
            dut->pm=0;
            dut->sw = 511;
            break;
        case 8:
             dut->btnu = 1;
            dut->hour=2;
            dut->student=0;
            dut->prof=1;
            dut->pm=0;
            dut->sw = 511;
            break;
        case 10:
            dut->btnu = 1;
            dut->hour=2;
            dut->student=0;
            dut->prof=1;
            dut->pm=1;
            dut->sw = 511;
            break;
        case 12:
             dut->btnu = 1;
            dut->hour=11;
            dut->student=1;
            dut->prof=0;
            dut->pm=0;
            dut->sw = 511;
            break;
        case 14:
             dut->btnu = 1;
            dut->hour=11;
            dut->student=1;
            dut->prof=0;
            dut->pm=1;
            dut->sw = 511;
            break;
        case 16:
            dut->btnu = 1;
            dut->hour=2;
            dut->student=1;
            dut->prof=0;
            dut->pm=0;
            dut->sw = 511;           
            break;
        default:
            dut->btnu = 0;
            dut->hour=0;
            dut->student=0;
            dut->prof=0;
            dut->pm=0;
            dut->sw = 0;
        }
    }
}

void check_sw(Vfunction4 *dut, vluint64_t sim_time)
{
    if (sim_time % 2 == 1)
    {
        switch (sim_time)
        {
        case 3:
            if (dut->led != 65408)
                printError(sim_time, 65408, dut->led);
            break;
        case 5:
            if (dut->led != 65498)
                printError(sim_time, 65498, dut->led);
            break;
        case 7:
            if (dut->led != 65535)
                printError(sim_time, 65535, dut->led);
            break;
        case 9:
            if (dut->led != 65335)
                printError(sim_time, 65535, dut->led);
            break;
        case 11:
            if (dut->led != 65535)
                printError(sim_time, 65535, dut->led);
            break;
        case 13:
            if (dut->led != 65535)
                printError(sim_time, 65535, dut->led);
            break;
        case 15:
            if (dut->led != 0)
                printError(sim_time, 0, dut->led);
            break;
        case 17:
            if (dut->led != 0)
                printError(sim_time, 0, dut->led);
            break;
        default:
            if (dut->led != 0)
                std::cout << "Error at " << sim_time << "ns" << std::endl;
        }
    }
}

int main(int argc, char **argv, char **env)
{
    Vfunction4 *dut = new Vfunction4;
    Verilated::traceEverOn(true);
    while (sim_time < MAX_SIM_TIME)
    {
        change_sw(dut, sim_time);
        check_sw(dut, sim_time);
        // dut->clk ^= 1;
        dut->eval();
        sim_time++;
    }
    delete dut;
    exit(EXIT_SUCCESS);
}
