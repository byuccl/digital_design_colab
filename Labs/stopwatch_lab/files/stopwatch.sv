
module stopwatch(
    input wire logic clk, reset, run,
    output logic [3:0] digit0, digit1, digit2, digit3
    );
    
    //internal signals
    logic [19:0] count;
    logic [3:0] rollover;
    logic pulse;
    
    //counter to roll over every .01 seconds and then for each digit
    mod_counter #(1000000, 20) C4(.count(count), .rollover(pulse), .clk(clk), .reset(reset), .increment(run));
    mod_counter C0(.count(digit0), .rollover(rollover[0]), .clk(clk), .reset(reset), .increment(pulse));
    mod_counter C1(.count(digit1), .rollover(rollover[1]), .clk(clk), .reset(reset), .increment(rollover[0]));
    mod_counter C2(.count(digit2), .rollover(rollover[2]), .clk(clk), .reset(reset), .increment(rollover[1]));
    mod_counter #(6, 4) C3(.count(digit3), .rollover(rollover[3]), .clk(clk), .reset(reset), .increment(rollover[2]));
    
endmodule