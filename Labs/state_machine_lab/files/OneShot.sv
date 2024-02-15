module OneShot(
  input wire logic clk, reset, in,
  output logic out
  
);

    logic inputhold;

    always_ff @(posedge clk) begin
        out <= 0;
        inputhold <= 0;
        if ((!in) || reset) begin
          out <= 0;
          inputhold <= 0;
        end else if (in && !inputhold) begin
          out <= 1;
          inputhold <= 1;
        end else begin
          out <= 0;
          inputhold <= 1;
        end
    end
    
endmodule
