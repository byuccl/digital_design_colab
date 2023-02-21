module function2(
   input logic[15:0] sw,
   input logic btnl,
   output logic[15:0] led
);

assign led[15:8] = btnl ? 8'h00 : sw[15:8];
assign led[7:0] = btnl ? sw[15:8]^sw[7:0] : sw[7:0];

endmodule
