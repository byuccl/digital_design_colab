module StateMachine(
  input wire logic btnd, btnu, btnc, btnl, btnr
  input wire logic [15:0] sw,
  input wire logic clk, reset,
  output logic [15:0] led
);

typedef enum { IDLE, COMB1, COMB2, COMB3, UNLOCKED} ns, cs;

input logic oneshot;
OneShot OS1(clk, reset, btnc, oneshot);
  logic [1:0] ns,cs;
  always_ff @(posedge clk) begin
    cs <= ns;
    case()
  end
  


endmodule
