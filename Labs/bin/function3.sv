module function3(
   input logic[12:0] sw,
   input logic btnr, A, B, C,
   output logic[15:0] led
);

assign led[15:3] = btnr ? 13'd0 : sw;
assign led[2:1] = btnr? 2'b00 : {C,B};
assign led[0] = btnr ? (A&~B)|(C) : A;

endmodule
