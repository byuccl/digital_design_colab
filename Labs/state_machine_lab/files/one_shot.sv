module OneShot(
  input wire logic clk, reset, in,
  output logic out
  
);
    
    typedef enum { IDLE, ONESHOT, WAIT} ns, cs;

    always_comb begin
        out = 1'b0;
        if(cs == ONESHOT)
            out = 1'b1;
    end


    always_ff @(posedge clk) begin
        cs <= ns;
        if(reset) begin
            ns <= IDLE;
        end
        if(cs == IDLE) begin
            if(in) begin
                ns <= ONESHOT;
            end
        end
        else if(cs == ONESHOT) begin
            ns <= WAIT;
        end
        else if(cs == WAIT) begin
            if(!in)
                ns <= IDLE;
        end
    end
  
  

endmodule
