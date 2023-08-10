module StateMachine(
  input wire logic btnd, btnu, btnc, btnl, btnr,
  input wire logic [15:0] sw,
  input wire logic clk,
  output logic [15:0] led
);

logic Q, oneshotQ, oneshotbtnc, reset;

assign Q = btnu | btnc | btnl | btnr;

typedef enum { SETUP, IDLE, COMB1, COMB2, COMB3, UNLOCKED, ERR} StateType;
StateType ns, cs;
OneShot OS1(.in(btnc), .clk(clk), .reset(reset), .out(oneshotbtnc));
OneShot OS2(.in(Q), .clk(clk), .reset(reset),  .out(oneshotQ));

always_comb 
begin
  ns = ERR;
  led = 0;
  reset = 0;
  if (btnd) begin
    ns = SETUP;
  end else case (cs)
    SETUP: begin
      led = 1;
      reset = 1;
      ns = IDLE;
    end
    IDLE: begin
      led = 2;
      if (oneshotbtnc) begin
        ns = COMB1;
      end else begin
        ns = IDLE;
      end
    end
    COMB1: begin
      led = 3;
      if (oneshotQ && (sw == 16'b0000000000000001)) begin
        ns = COMB2;
      end else if (oneshotQ) begin
        ns = IDLE;
      end else begin
        ns = COMB1;
      end
    end
    COMB2: begin
      led = 4;
      if (oneshotQ && (sw == 16'b1111001111001111)) begin
        ns = COMB3;
      end else if (oneshotQ) begin
        ns = IDLE;
      end else begin
        ns = COMB2;
      end
    end
    COMB3: begin
      led = 5;
      if (oneshotQ && (sw == 16'b0100101010100111)) begin
        ns = UNLOCKED;
      end else if (oneshotQ) begin
        ns = IDLE;
      end else begin
        ns = COMB3;
      end
    end
    UNLOCKED: begin
      led = 'hffff;
      if (oneshotbtnc) begin
        ns = IDLE;
      end else begin
        ns = UNLOCKED;
      end
    end
  endcase
end


always_ff @(posedge clk) begin
  cs <= ns;
end
  


endmodule