module function1 (
 output logic [15:0] led,
 input logic  btnd,
 input logic [15:0] sw
);
//Answer provided
// Code goes here
assign led = btnd ? sw << 3 : sw;

endmodule 
