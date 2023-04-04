module mod_counter #(parameter MOD_VALUE=10, WID=4) (
    input wire logic clk, reset, increment,
    output logic rollover,
    output logic [WID-1:0] count
    );
    
    always_ff @(posedge clk)
        if (reset)
            count <= 0;
        else if (increment)
        begin
            if (count == MOD_VALUE-1)
                count <= 0;
            else
                count <= count + 1;
        end
            
    assign rollover = ((count == MOD_VALUE-1) && (increment == 1))?1'b1:1'b0;
        
endmodule