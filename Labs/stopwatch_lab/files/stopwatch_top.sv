module stopwatch_top(
    input wire logic clk, btnc, sw,
    output logic [3:0] anode,
    output logic [7:0] segment
    );
    
    //internal signals
    logic [15:0] data;
    
    SevenSegmentControl SS0(.clk(clk), .reset(btnc), .dataIn(data), .digitDisplay(4'b1111), .digitPoint(4'b1111), .anode(anode), .segment(segment));
    stopwatch SW0(.clk(clk), .reset(btnc), .run(sw), .digit0(data[3:0]), .digit1(data[7:4]), .digit2(data[11:8]), .digit3(data[15:12]));
    
    
endmodule

