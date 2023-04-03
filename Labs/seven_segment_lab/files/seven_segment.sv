module seven_segment(input wire [3:0] data, output reg [6:0] segment);
  // hex_value: 4-bit input representing the hex value to be displayed
  // segments: 7-bit output representing the segments of the seven-segment display

  always_comb begin
    case (data)
      4'b0000: segment = 7'b1000000;
      4'b0001: segment = 7'b1111001;
      4'b0010: segment = 7'b0100100;
      4'b0011: segment = 7'b0110000;
      4'b0100: segment = 7'b0011001;
      4'b0101: segment = 7'b0010010;
      4'b0110: segment = 7'b0000010;
      4'b0111: segment = 7'b1111000;
      4'b1000: segment = 7'b0000000;
      4'b1001: segment = 7'b0010000;
      4'b1010: segment = 7'b0001000;
      4'b1011: segment = 7'b0000011;
      4'b1100: segment = 7'b1000110;
      4'b1101: segment = 7'b0100001;
      4'b1110: segment = 7'b0000110;
      4'b1111: segment = 7'b0001110;
      default: segment = 7'b1111111;
    endcase
  end
endmodule
