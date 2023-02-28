
module bitwiseAnd(
    input logic [3:0] sw1, sw2,
    input logic btnc,
    output logic [3:0] led
    );

    assign led = btnc ? sw1 & sw2 : 4'h0;

endmodule
