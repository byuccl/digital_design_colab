
module bitwiseAnd(
    input logic [7:0] sw,
    input logic btnc,
    output logic [3:0] led
    );

    assign led = btnc ? sw[7:4]&sw[3:0] : 8'd0;

endmodule