module arithmetic_top (
  input logic [15:0] sw,
  input logic btnc,
  output logic [8:0] led
  );
  //Answer provided
  logic [7:0] a, b;
  
  assign a = sw[7:0];
  always_comb
    if(btnc)
        b = ~sw[15:8];
    else 
        b = sw[15:8];

  add_8 add(.a(a), .b(b), .s(led[7:0]), .co(led[8]), .cin(btnc));

  //half of sw should be a and half should be b
  //when btnc is high it should subtract a-b and not add
  //Led [7:0] should show the results. Led[8] should be high if overflow has occurred.
  endmodule
